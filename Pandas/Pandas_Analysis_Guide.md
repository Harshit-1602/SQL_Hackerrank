# Pandas Essential Functions for Data Analysts

This guide covers the core Pandas functions required for Data Analyst and Junior Data Analyst roles, focusing on data cleaning, transformation, and analysis.

## 1. Data Loading
- `pd.read_csv()`: Load data from a CSV file.
- `pd.read_excel()`: Load data from an Excel file.
- `pd.read_sql()`: Load data from a SQL database.
- `pd.read_json()`: Load data from a JSON file.

## 2. Data Inspection
- `df.head(n)`: View the first $n$ rows.
- `df.tail(n)`: View the last $n$ rows.
- `df.info()`: Summary of the DataFrame (dtypes, non-null counts, memory usage).
- `df.describe()`: Summary statistics for numerical columns.
- `df.shape`: Get the number of rows and columns.
- `df.columns`: Get the column names.
- `df.dtypes`: Get the data types of each column.
- `df.unique()` / `df.nunique()`: Get unique values or count of unique values.
- `df.value_counts()`: Count occurrences of unique values in a column.

## 3. Data Selection & Filtering
- `df['column_name']`: Select a single column.
- `df[['col1', 'col2']]`: Select multiple columns.
- `df.iloc[]`: Select rows and columns by integer-based index.
- `df.loc[]`: Select rows and columns by labels/boolean mask.
- `df[df['col'] > value]`: Filter rows based on a condition.
- `df.query()`: Filter data using a query string.

## 4. Data Cleaning
- `df.isnull()` / `df.isna()`: Check for missing values.
- `df.dropna()`: Remove rows or columns with missing values.
- `df.fillna(value)`: Fill missing values with a specific value or method (mean, median, etc.).
- `df.drop_duplicates()`: Remove duplicate rows.
- `df.rename(columns={'old': 'new'})`: Rename columns.
- `df.drop(columns=['col1', 'col2'])`: Drop specific columns.
- `df.astype()`: Convert data types (e.g., string to datetime).
- `df['col'].str.strip()` / `lower()` / `replace()`: String manipulation.

## 5. Data Transformation
- `df.apply(func)`: Apply a function along an axis of the DataFrame.
- `df.map()`: Map values of Series according to input correspondence.
- `df.applymap()`: Apply a function to a Dataframe elementwise.
- `df.sort_values(by='col', ascending=True)`: Sort data.
- `df.reset_index()`: Reset the index of the DataFrame.
- `pd.to_datetime()`: Convert a column to datetime objects.

## 6. Data Aggregation & Grouping
- `df.groupby('col').mean()`: Group data and calculate mean (or other stats like `sum`, `count`, `max`, `min`).
- `df.pivot_table()`: Create a spreadsheet-style pivot table.
- `df.groupby('col').agg({'col2': 'sum', 'col3': 'mean'})`: Multiple aggregations.
- `df.crosstab()`: Compute a simple cross-tabulation of two (or more) factors.

## 7. Joining & Merging
- `pd.merge(df1, df2, on='key')`: Database-style join.
- `df1.join(df2)`: Join DataFrames on index.
- `pd.concat([df1, df2])`: Concatenate DataFrames along a particular axis.

## 8. Exporting Data
- `df.to_csv('filename.csv', index=False)`: Save to CSV.
- `df.to_excel('filename.xlsx', index=False)`: Save to Excel.
- `df.to_sql()`: Write records stored in a DataFrame to a SQL database.
