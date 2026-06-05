# Power BI Mastery Roadmap

To become proficient in Power BI, you need to master the "Internal Three": **Power Query**, **DAX (Data Modeling)**, and **Visualization**.

## 1. Data Transformation (Power Query)
*Goal: Move from messy raw data to clean, structured tables.*
- **Key Concepts:**
    - Connecting to data sources (Excel, CSV, SQL).
    - Basic transformations: Filtering, renaming, changing data types.
    - Advanced transformations: Merging vs. Appending, Pivoting/Unpivoting.
    - The "M" Language (the code behind the UI).
- **Practice Task:** Clean the `Inventory_Analytics_Data_Custom.xlsx` file. Fix any inconsistencies in product names or dates.

## 2. Data Modeling & DAX
*Goal: Create relationships and calculate complex metrics.*
- **Key Concepts:**
    - **Star Schema:** Understanding Fact tables vs. Dimension tables.
    - **Relationships:** One-to-many, Directional filtering.
    - **DAX Basics:** Calculated Columns vs. Measures.
    - **Time Intelligence:** Total-to-date, Year-over-Year (YoY) growth.
- **Practice Task:** Create a measure for "Total Stock Value" and "Monthly Inventory Turnover".

## 3. Data Visualization
*Goal: Tell a story that drives decisions.*
- **Key Concepts:**
    - Choosing the right chart (Bar vs. Line vs. Scatter).
    - Using Slicers and Filters for interactivity.
    - Tooltips and Drill-throughs.
    - Dashboard Layout & Design Principles (CRAP: Contrast, Repetition, Alignment, Proximity).
- **Practice Task:** Build an Inventory Dashboard that highlights "Out of Stock" risks and "Top Performing Categories".

---

## Suggested First Steps
1. **Explore Existing Data:** I see you have `processed_inventory_data.csv`. We can use this as our primary source.
2. **Installation:** Ensure you have **Power BI Desktop** installed (Free from Microsoft Store).
3. **First Import:** Open Power BI, click "Get Data", and select your inventory CSV.
