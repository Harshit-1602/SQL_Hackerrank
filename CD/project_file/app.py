import streamlit as st
import pandas as pd
import numpy as np
import zipfile
import io
import os
import sqlite3
import re
import subprocess
import sys
from datetime import datetime, date

st.set_page_config(page_title="Vermin Inventory Analytics System", layout="wide")

st.title("📦 Vermin Inventory AnalyticsS")

# -----------------------------
# File paths – update these to match your system
# -----------------------------
SAVE_FILE = r"C:\Users\harsh\OneDrive\Desktop\Projects_2026\py\Inventory_Analytics_Data_Custom.xlsx"
PBIX_FILE = r"C:\Users\harsh\OneDrive\Desktop\Projects_2026\py\Inventory_vermin.pbix"   # local .pbix file (for external open only)

def save_tables(tables_dict):
    """Save all tables to Excel (one sheet per table)."""
    if not tables_dict:
        return
    try:
        with pd.ExcelWriter(SAVE_FILE, engine='openpyxl') as writer:
            for name, df in tables_dict.items():
                df.to_excel(writer, sheet_name=name, index=False)
    except Exception as e:
        st.error(f"❌ Failed to save Excel file: {e}")

def load_tables():
    """Load tables from Excel file."""
    if not os.path.exists(SAVE_FILE):
        st.error(f"❌ File '{SAVE_FILE}' not found. Please check the path.")
        return {}
    try:
        excel_file = pd.ExcelFile(SAVE_FILE)
        tables = {}
        for sheet in excel_file.sheet_names:
            df = pd.read_excel(SAVE_FILE, sheet_name=sheet, parse_dates=True)
            tables[sheet] = df
        return tables
    except Exception as e:
        st.error(f"❌ Could not load Excel file: {e}")
        return {}

# -----------------------------
# Initialize session state
# -----------------------------
if "tables" not in st.session_state:
    st.session_state.tables = load_tables()
if "powerbi_embed_url" not in st.session_state:
    st.session_state.powerbi_embed_url = ""

# -----------------------------
# Sidebar – processing and Power BI
# -----------------------------
st.sidebar.header("Controls")

process_current = st.sidebar.button("Process Current Table")
process_all = st.sidebar.button("Process All Tables")

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Power BI Integration")

if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "rb") as f:
        st.sidebar.download_button(
            label="Download Live Excel File",
            data=f,
            file_name=os.path.basename(SAVE_FILE),
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.sidebar.info("Excel file not found – cannot download.")

st.sidebar.markdown("""
**To use in Power BI Desktop:**
1. Click **Get Data** → **Excel**.
2. Select the downloaded file.
3. Choose the sheets you want to load.
4. Click **Load**.
""")

# Optional template download
TEMPLATE_FILE = "inventory_template.pbit"
if os.path.exists(TEMPLATE_FILE):
    with open(TEMPLATE_FILE, "rb") as f:
        st.sidebar.download_button(
            label="Download Power BI Template (.pbit)",
            data=f,
            file_name=TEMPLATE_FILE,
            mime="application/octet-stream"
        )
    st.sidebar.caption("Open the template, then update the data source path.")

# -----------------------------
# Cleaning function
# -----------------------------
def clean_data(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df = df.drop_duplicates()
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].str.strip()
    for col in df.select_dtypes(include=np.number):
        df[col] = df[col].fillna(df[col].median())
    return df

# -----------------------------
# Helper: get next ID for a column (handles both numeric and prefixed string IDs)
# -----------------------------
def get_next_id_value(series):
    """
    Return the next ID value for a pandas Series.
    - For numeric columns: max + 1 (or 1 if empty).
    - For string columns with trailing digits (e.g., "S0012"): increment the numeric part,
      keep the prefix and same number of leading zeros.
    - If empty and string, returns "ID001".
    """
    if pd.api.types.is_numeric_dtype(series):
        # Numeric column: simple integer increment
        max_val = series.max()
        return 0 if pd.isna(max_val) else int(max_val) + 1

    # String column: try to parse as prefix + digits
    series = series.dropna().astype(str)
    if len(series) == 0:
        return "ID001"  # default for empty string column

    pattern = re.compile(r'^(.*?)(\d+)$')
    # Extract all valid matches
    matches = series.apply(lambda x: pattern.match(x)).dropna()
    if len(matches) == 0:
        # No values follow the pattern – default
        return "ID001"

    # Find the value with the largest numeric suffix
    max_num = -1
    max_prefix = ""
    max_digits = ""
    for match in matches:
        prefix = match.group(1)
        digits = match.group(2)
        num = int(digits)
        if num > max_num:
            max_num = num
            max_prefix = prefix
            max_digits = digits
    # Increment and pad to same length
    next_num = max_num + 1
    pad_len = len(max_digits)
    return f"{max_prefix}{next_num:0{pad_len}d}"

# -----------------------------
# Helper to compute safe numeric defaults and bounds
# -----------------------------
def get_numeric_bounds_and_default(series, current_val=None):
    """Return (min_buffered, max_buffered, default_value) for a numeric column."""
    if series.isnull().all():
        return None, None, 0 if pd.api.types.is_integer_dtype(series) else 0.0

    min_val = float(series.min())
    max_val = float(series.max())
    # Add a small buffer
    min_buffered = min_val - abs(min_val)*0.1 if min_val != 0 else -100
    max_buffered = max_val + abs(max_val)*0.1 if max_val != 0 else 100

    if current_val is not None and pd.notna(current_val):
        # Ensure it's a scalar (could be list if we had multiple rows, but we fixed that)
        if isinstance(current_val, (list, np.ndarray)):
            current_val = current_val[0] if len(current_val) > 0 else None
        if current_val is not None:
            default_val = float(current_val)
            # Clamp to bounds
            default_val = max(min_buffered, min(default_val, max_buffered))
        else:
            default_val = (min_val + max_val) / 2
    else:
        # Use median as default, or fallback to midpoint
        median_val = series.median()
        if pd.isna(median_val):
            default_val = (min_val + max_val) / 2
        else:
            default_val = median_val
        default_val = max(min_buffered, min(default_val, max_buffered))

    return min_buffered, max_buffered, default_val

# -----------------------------
# Main Area – Tabs for each sheet + SQL tab + Power BI tab
# -----------------------------
if st.session_state.tables:
    # Create mapping from original sheet name to safe SQL table name
    table_name_map = {}
    safe_names = []
    for name in st.session_state.tables.keys():
        safe = name.lower().replace(" ", "_").replace("-", "_")
        table_name_map[name] = safe
        safe_names.append(safe)

    # Build tab list: all data sheets + "SQL Query" + "Power BI Report"
    tab_names = list(st.session_state.tables.keys()) + ["SQL Query", "Power BI Report"]
    tabs = st.tabs(tab_names)

    for i, tab_name in enumerate(tab_names):
        if tab_name == "SQL Query":
            with tabs[i]:
                st.subheader("🔍 Run SQL Queries on Your Data")

                # Show table name mapping
                st.markdown("**Available tables (use these names in SQL):**")
                mapping_df = pd.DataFrame(list(table_name_map.items()), columns=["Original Sheet", "SQL Table Name"])
                st.dataframe(mapping_df, width='stretch')

                # SQL input area with validation
                query = st.text_area("Enter your SQL query:", height=150, key="sql_query")

                # Optional: warn about destructive commands
                if query.strip().lower().startswith(("drop", "delete", "update", "insert", "alter")):
                    st.warning("⚠️ This query modifies data. Ensure you have backups if needed.")

                if st.button("Run Query"):
                    if not query.strip():
                        st.warning("⚠️ Please enter a SQL query.")
                    else:
                        try:
                            # Create in-memory SQLite database
                            conn = sqlite3.connect(":memory:")
                            # Load each DataFrame into SQLite with safe table name
                            for orig_name, df in st.session_state.tables.items():
                                safe_name = table_name_map[orig_name]
                                df.to_sql(safe_name, conn, if_exists="replace", index=False)

                            # Execute query and fetch results
                            result_df = pd.read_sql_query(query, conn)
                            conn.close()

                            st.subheader("Query Result")
                            if result_df.empty:
                                st.info("ℹ️ Query returned no rows.")
                            else:
                                st.dataframe(result_df, width='stretch')
                                # Option to download result as CSV
                                csv = result_df.to_csv(index=False)
                                st.download_button(
                                    label="Download Result as CSV",
                                    data=csv,
                                    file_name="query_result.csv",
                                    mime="text/csv"
                                )
                        except Exception as e:
                            st.error(f"❌ SQL Error: {e}")

        elif tab_name == "Power BI Report":
            with tabs[i]:
                st.subheader("📈 Embedded Power BI Report")

                # IMPORTANT NOTICE ABOUT LOCAL FILES
                st.warning("""
                **⚠️ Local .pbix files cannot be embedded directly in any web application.**
                
                To display your Power BI report, you must:
                1. **Publish** your report to the Power BI service (app.powerbi.com)
                2. Get a **public embed URL** from the published report
                3. Paste that URL below
                """)

                st.markdown("""
                ### 📋 Instructions to get your embed URL:
                1. Open your report in **Power BI Desktop**
                2. Click **File → Publish → Publish to Power BI**
                3. Sign in and select a workspace
                4. Go to [app.powerbi.com](https://app.powerbi.com) and open your published report
                5. Click **File → Embed report → Publish to web (public)**
                6. Copy the **iframe embed URL** (starts with `https://app.powerbi.com/view?r=`)
                """)

                # Power BI embed URL input with validation
                embed_url = st.text_input(
                    "Power BI Embed URL",
                    value=st.session_state.powerbi_embed_url,
                    key="pbi_url_input",
                    placeholder="https://app.powerbi.com/view?r=..."
                )

                # Validate URL format
                valid_pbi_url = False
                if embed_url:
                    # Check if it looks like a Power BI embed URL
                    if embed_url.startswith("https://") and ("powerbi.com" in embed_url or "fabric.microsoft.com" in embed_url) and "view?r=" in embed_url:
                        valid_pbi_url = True
                    else:
                        st.error("❌ The URL does not look like a valid Power BI embed link. Please make sure you copied the correct URL from 'Publish to web'.")

                # Update session state
                if embed_url != st.session_state.powerbi_embed_url:
                    st.session_state.powerbi_embed_url = embed_url
                    st.rerun()

                # Display the report if we have a valid URL
                if st.session_state.powerbi_embed_url and valid_pbi_url:
                    st.components.v1.iframe(
                        src=st.session_state.powerbi_embed_url,
                        height=600,
                        scrolling=True
                    )
                elif st.session_state.powerbi_embed_url and not valid_pbi_url:
                    st.info("👆 Please correct the URL above to see your report.")
                else:
                    st.info("👆 Enter a valid Power BI embed URL above to see your report.")

                # Fallback: open local .pbix file externally
                st.markdown("---")
                st.subheader("📂 Alternative: Open locally")
                if os.path.exists(PBIX_FILE):
                    if st.button("Open .pbix file in Power BI Desktop"):
                        try:
                            if sys.platform == "win32":
                                os.startfile(PBIX_FILE)
                            elif sys.platform == "darwin":
                                subprocess.run(["open", PBIX_FILE])
                            else:
                                subprocess.run(["xdg-open", PBIX_FILE])
                            st.success("Opening Power BI Desktop...")
                        except Exception as e:
                            st.error(f"❌ Could not open file: {e}")
                else:
                    st.warning(f"Local .pbix file not found at: {PBIX_FILE}")

        else:
            # This is a data sheet tab
            with tabs[i]:
                df_current = st.session_state.tables[tab_name]

                # Checkbox to show cleaned data
                show_cleaned = st.checkbox(f"Show cleaned version of '{tab_name}'", key=f"clean_{tab_name}")

                if show_cleaned:
                    st.subheader(f"Cleaned Data for '{tab_name}'")
                    cleaned_df = clean_data(df_current)
                    st.dataframe(cleaned_df, width='stretch')
                else:
                    st.subheader(f"Raw Data in '{tab_name}'")
                    st.dataframe(df_current, width='stretch')

                # ✅ ADD THIS BUTTON RIGHT HERE
                if st.button(f"🧹 Clean & Save '{tab_name}'"):
                    cleaned_df = clean_data(df_current)
                    st.session_state.tables[tab_name] = cleaned_df
                    save_tables(st.session_state.tables)
                    st.success(f"✅ '{tab_name}' cleaned and saved!")
                    st.rerun()

                # ----- INSERT NEW RECORD -----
                with st.expander("➕ Insert New Record", expanded=True):
                    with st.form(key=f"insert_form_{tab_name}"):
                        st.write("Fill in the values for the new row")
                        new_row = {}
                        validation_errors = []

                        # Identify all columns that are ID‑like (case‑insensitive contains "id")
                        id_columns = [col for col in df_current.columns if 'id' in col.lower()]

                        for col in df_current.columns:
                            dtype = df_current[col].dtype

                            if col in id_columns:
                                # Auto‑increment this ID column
                                next_val = get_next_id_value(df_current[col])
                                if pd.api.types.is_numeric_dtype(df_current[col]):
                                    # Numeric ID: use number_input (disabled)
                                    new_row[col] = st.number_input(
                                        f"{col} (auto‑assigned)",
                                        value=next_val,
                                        step=1,
                                        disabled=True,
                                        key=f"id_num_{tab_name}_{col}"
                                    )
                                else:
                                    # String ID: use text_input (disabled)
                                    new_row[col] = st.text_input(
                                        f"{col} (auto‑assigned)",
                                        value=str(next_val),
                                        disabled=True,
                                        key=f"id_str_{tab_name}_{col}"
                                    )
                            elif pd.api.types.is_datetime64_any_dtype(dtype):
                                new_row[col] = st.date_input(
                                    f"{col}",
                                    value=date.today(),
                                    key=f"date_{tab_name}_{col}"
                                )
                            elif pd.api.types.is_numeric_dtype(dtype):
                                # Numeric input with safe bounds and default
                                min_b, max_b, default = get_numeric_bounds_and_default(df_current[col])
                                if pd.api.types.is_integer_dtype(dtype):
                                    new_row[col] = st.number_input(
                                        f"{col}",
                                        value=int(default),
                                        step=1,
                                        min_value=int(min_b) if min_b is not None else None,
                                        max_value=int(max_b) if max_b is not None else None,
                                        key=f"num_{tab_name}_{col}"
                                    )
                                else:
                                    new_row[col] = st.number_input(
                                        f"{col}",
                                        value=default,
                                        step=0.01,
                                        format="%f",
                                        min_value=min_b,
                                        max_value=max_b,
                                        key=f"num_{tab_name}_{col}"
                                    )
                            else:
                                # Text input – STRIP and validate NOT EMPTY
                                raw_val = st.text_input(
                                    f"{col}",
                                    value="",
                                    key=f"text_{tab_name}_{col}"
                                )
                                stripped_val = raw_val.strip()
                                if stripped_val == "":
                                    validation_errors.append(f"❌ {col} cannot be empty.")
                                new_row[col] = stripped_val

                        submitted = st.form_submit_button("Add Record")
                        if submitted:
                            if validation_errors:
                                for err in validation_errors:
                                    st.error(err)
                            else:
                                # Convert date objects to Timestamp
                                for col, val in new_row.items():
                                    if isinstance(val, date) and not isinstance(val, datetime):
                                        new_row[col] = pd.Timestamp(val)
                                new_df = pd.DataFrame([new_row])
                                st.session_state.tables[tab_name] = pd.concat(
                                    [df_current, new_df], ignore_index=True
                                )
                                save_tables(st.session_state.tables)
                                st.success(f"✅ Record added to '{tab_name}'!")
                                st.rerun()

                # ----- DELETE RECORDS BY ID -----
                with st.expander("🗑️ Delete Record(s) by ID", expanded=False):
                    # Get all ID columns for this sheet
                    id_cols = [col for col in df_current.columns if 'id' in col.lower()]
                    if not id_cols:
                        st.info("No ID column found in this sheet.")
                    else:
                        selected_id_col = st.selectbox(
                            "Select ID column to use for deletion",
                            id_cols,
                            key=f"del_id_col_{tab_name}"
                        )
                        id_values_input = st.text_input(
                            f"Enter {selected_id_col} value(s) to delete (comma‑separated)",
                            key=f"del_ids_{tab_name}"
                        )
                        if st.button("Delete Selected Rows", key=f"del_btn_{tab_name}"):
                            if not id_values_input.strip():
                                st.warning("⚠️ Please enter at least one ID value.")
                            else:
                                # Split and clean
                                raw_values = [v.strip() for v in id_values_input.split(",") if v.strip()]
                                # Convert to appropriate type based on column dtype
                                col_dtype = df_current[selected_id_col].dtype
                                target_values = []
                                conversion_failed = False
                                for v in raw_values:
                                    try:
                                        if pd.api.types.is_numeric_dtype(col_dtype):
                                            if pd.api.types.is_integer_dtype(col_dtype):
                                                target_values.append(int(v))
                                            else:
                                                target_values.append(float(v))
                                        else:
                                            target_values.append(str(v))
                                    except ValueError:
                                        st.error(f"❌ Value '{v}' cannot be converted to the required type for column '{selected_id_col}'.")
                                        conversion_failed = True
                                        break
                                if not conversion_failed:
                                    mask = df_current[selected_id_col].isin(target_values)
                                    rows_to_delete = df_current[mask]
                                    if len(rows_to_delete) == 0:
                                        st.warning("⚠️ No matching records found.")
                                    else:
                                        st.warning(f"Deleting {len(rows_to_delete)} record(s):")
                                        st.dataframe(rows_to_delete, width='stretch')
                                        df_current = df_current[~mask].reset_index(drop=True)
                                        st.session_state.tables[tab_name] = df_current
                                        save_tables(st.session_state.tables)
                                        st.success(f"✅ Deleted {len(rows_to_delete)} record(s).")
                                        st.rerun()

                # ----- UPDATE RECORD BY ID -----
                with st.expander("✏️ Update Record by ID", expanded=False):
                    id_cols = [col for col in df_current.columns if 'id' in col.lower()]
                    if not id_cols:
                        st.info("No ID column found in this sheet – cannot update.")
                    else:
                        update_id_col = st.selectbox(
                            "Select ID column to identify the record",
                            id_cols,
                            key=f"update_id_col_{tab_name}"
                        )
                        update_id_value = st.text_input(
                            f"Enter {update_id_col} of the record to update",
                            key=f"update_id_val_{tab_name}"
                        )

                        # Button to fetch the record
                        if st.button("🔍 Fetch Record", key=f"fetch_btn_{tab_name}"):
                            if not update_id_value.strip():
                                st.warning("⚠️ Please enter an ID value.")
                            else:
                                # Convert to appropriate type
                                col_dtype = df_current[update_id_col].dtype
                                try:
                                    if pd.api.types.is_numeric_dtype(col_dtype):
                                        if pd.api.types.is_integer_dtype(col_dtype):
                                            target_id = int(update_id_value)
                                        else:
                                            target_id = float(update_id_value)
                                    else:
                                        target_id = str(update_id_value)
                                except ValueError:
                                    st.error(f"❌ ID value cannot be converted to the required type for column '{update_id_col}'.")
                                    target_id = None

                                if target_id is not None:
                                    # Find the record
                                    mask = df_current[update_id_col] == target_id
                                    record_df = df_current[mask]
                                    if len(record_df) == 0:
                                        st.error(f"❌ No record found with {update_id_col} = {target_id}.")
                                    else:
                                        if len(record_df) > 1:
                                            st.warning(f"⚠️ Multiple records found. Updating the first one.")
                                        # Always take the first row as a Series
                                        record = record_df.iloc[0]
                                        # Store the index and record in session state
                                        st.session_state[f"update_record_{tab_name}"] = record.to_dict()
                                        st.session_state[f"update_index_{tab_name}"] = record_df.index[0]
                                        st.rerun()

                        # If a record is fetched, show update form
                        if f"update_record_{tab_name}" in st.session_state:
                            record_data = st.session_state[f"update_record_{tab_name}"]
                            record_index = st.session_state[f"update_index_{tab_name}"]

                            with st.form(key=f"update_form_{tab_name}"):
                                st.write("Edit the values below:")
                                updated_row = {}
                                validation_errors_upd = []

                                for col in df_current.columns:
                                    dtype = df_current[col].dtype
                                    current_val = record_data.get(col, "")

                                    if col == update_id_col:
                                        # ID column – disabled (cannot change ID)
                                        if pd.api.types.is_numeric_dtype(dtype):
                                            val = float(current_val) if pd.api.types.is_float(dtype) else int(current_val)
                                            updated_row[col] = st.number_input(
                                                f"{col} (ID – cannot change)",
                                                value=val,
                                                disabled=True,
                                                key=f"upd_id_{tab_name}_{col}"
                                            )
                                        else:
                                            updated_row[col] = st.text_input(
                                                f"{col} (ID – cannot change)",
                                                value=str(current_val),
                                                disabled=True,
                                                key=f"upd_id_{tab_name}_{col}"
                                            )
                                    elif pd.api.types.is_datetime64_any_dtype(dtype):
                                        # Convert current_val to date if it's a Timestamp
                                        if isinstance(current_val, pd.Timestamp):
                                            current_date = current_val.date()
                                        elif isinstance(current_val, datetime):
                                            current_date = current_val.date()
                                        else:
                                            current_date = date.today()
                                        updated_row[col] = st.date_input(
                                            f"{col}",
                                            value=current_date,
                                            key=f"upd_date_{tab_name}_{col}"
                                        )
                                    elif pd.api.types.is_numeric_dtype(dtype):
                                        # Numeric input with safe bounds and current value as default
                                        min_b, max_b, default = get_numeric_bounds_and_default(df_current[col], current_val)
                                        if pd.api.types.is_integer_dtype(dtype):
                                            updated_row[col] = st.number_input(
                                                f"{col}",
                                                value=int(default),
                                                step=1,
                                                min_value=int(min_b) if min_b is not None else None,
                                                max_value=int(max_b) if max_b is not None else None,
                                                key=f"upd_num_{tab_name}_{col}"
                                            )
                                        else:
                                            updated_row[col] = st.number_input(
                                                f"{col}",
                                                value=default,
                                                step=0.01,
                                                format="%f",
                                                min_value=min_b,
                                                max_value=max_b,
                                                key=f"upd_num_{tab_name}_{col}"
                                            )
                                    else:
                                        # Text input – STRIP and validate NOT EMPTY
                                        raw_val = st.text_input(
                                            f"{col}",
                                            value=str(current_val) if pd.notna(current_val) else "",
                                            key=f"upd_text_{tab_name}_{col}"
                                        )
                                        stripped_val = raw_val.strip()
                                        if stripped_val == "":
                                            validation_errors_upd.append(f"❌ {col} cannot be empty.")
                                        updated_row[col] = stripped_val

                                submitted_upd = st.form_submit_button("Update Record")
                                if submitted_upd:
                                    if validation_errors_upd:
                                        for err in validation_errors_upd:
                                            st.error(err)
                                    else:
                                        try:
                                            # Convert date objects to Timestamp
                                            for col, val in updated_row.items():
                                                if isinstance(val, date) and not isinstance(val, datetime):
                                                    updated_row[col] = pd.Timestamp(val)

                                            # Update the DataFrame at the stored index
                                            for col in updated_row:
                                                st.session_state.tables[tab_name].at[record_index, col] = updated_row[col]

                                            save_tables(st.session_state.tables)
                                            st.success(f"✅ Record with {update_id_col} = {update_id_value} updated.")
                                            # Clear the fetched record from session
                                            del st.session_state[f"update_record_{tab_name}"]
                                            del st.session_state[f"update_index_{tab_name}"]
                                            st.rerun()
                                        except Exception as e:
                                            st.error(f"❌ An error occurred during update: {e}")

                            if st.button("Cancel Update", key=f"cancel_upd_{tab_name}"):
                                del st.session_state[f"update_record_{tab_name}"]
                                del st.session_state[f"update_index_{tab_name}"]
                                st.rerun()

else:
    st.error(f"❌ Could not load any sheets from '{SAVE_FILE}'. Please check the file.")

# -----------------------------
# Process current table (export cleaned version) – with validation
# -----------------------------
if process_current and st.session_state.tables:
    st.sidebar.markdown("---")
    st.sidebar.subheader("Process a specific table")
    process_table_name = st.sidebar.selectbox(
        "Choose table to process",
        list(st.session_state.tables.keys()),
        key="process_select"
    )
    if st.sidebar.button("Process This Table Now"):
        if not process_table_name:
            st.sidebar.error("❌ Please select a table to process.")
        else:
            df_original = st.session_state.tables[process_table_name]
            cleaned = clean_data(df_original)

            st.subheader(f"Processed Table: {process_table_name}")
            st.dataframe(cleaned, width='stretch')

            csv_data = cleaned.to_csv(index=False)
            st.download_button(
                label=f"Download {process_table_name} as CSV",
                data=csv_data,
                file_name=f"{process_table_name}_processed.csv",
                mime="text/csv"
            )

# -----------------------------
# Process all tables (ZIP of cleaned CSVs)
# -----------------------------
if process_all and st.session_state.tables:
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for name, df in st.session_state.tables.items():
            cleaned = clean_data(df)
            csv_data = cleaned.to_csv(index=False)
            zip_file.writestr(f"{name}_processed.csv", csv_data)
    zip_buffer.seek(0)
    st.success("✅ All tables processed and packaged.")
    st.download_button(
        label="Download All Tables as ZIP",
        data=zip_buffer,
        file_name="all_tables_processed.zip",
        mime="application/zip"
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
