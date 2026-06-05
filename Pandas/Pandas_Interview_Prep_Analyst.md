# Pandas Interview Preparation Guide for Data Analysts

This guide covers the most critical Pandas concepts and questions frequently asked during Data Analyst and Junior Data Analyst interviews.

---

## 1. Fundamentals & Core Objects

### What is Pandas and its Primary Uses?
- **Data Manipulation:** An open-source Python library providing high-performance data structures and data analysis tools.
- **Handling Tabular Data:** It is designed to work with "relational" or "labeled" data, similar to SQL tables or Excel spreadsheets.
- **Integration:** Seamlessly integrates with other libraries like NumPy (for math), Matplotlib (for plotting), and Scikit-learn (for ML).
- **Automation:** Replaces manual Excel tasks with reproducible scripts, handling millions of rows much faster than spreadsheets.

### Series vs. DataFrame
| Feature | Series | DataFrame |
| :--- | :--- | :--- |
| **Dimensionality** | 1-Dimensional (single column). | 2-Dimensional (tabular structure). |
| **Components** | Data + Index. | Data + Index + Columns. |
| **Data Types** | Every element must be of the same data type. | Different columns can have different data types (heterogeneous). |
| **Concept** | Like a single column in an Excel sheet. | Like the entire Excel spreadsheet or SQL table. |

### Indexing: loc vs. iloc
| Feature | loc | iloc |
| :--- | :--- | :--- |
| **Selection Type** | Label-based indexing. | Integer-position based indexing. |
| **Input** | Uses names of rows and columns (strings or labels). | Uses numerical indices (0, 1, 2...). |
| **Slicing** | Includes the stop index (e.g., `'a':'c'` includes 'c'). | Excludes the stop index (e.g., `0:3` includes 0, 1, 2). |
| **Use Case** | Best for selecting by specific names/labels. | Best for selecting by row/column position. |

---

## 2. Data Cleaning & Preparation

### Handling Missing Data (NaN)
- **Identification:** Use `isnull()` or `isna()` to find missing values across the entire DataFrame or specific columns.
- **Removal:** Use `dropna()` to delete rows or columns containing missing values (be careful of data loss).
- **Imputation:** Use `fillna()` to replace missing values with a specific value, mean, median, or the previous/next value.
- **Significance:** Missing data can lead to incorrect calculations (e.g., sums or averages) if not handled before analysis.

### Dealing with Duplicates
- **Detection:** Use `duplicated()` to identify rows that are identical to previous rows.
- **Removal:** Use `drop_duplicates()` to keep only the first (or last) occurrence of a repeated record.
- **Subsets:** You can check for duplicates based on a specific subset of columns rather than the entire row.
- **Integrity:** Removing duplicates is a vital step in data cleaning to ensure accuracy in counts and aggregations.

### Data Type Conversion
- **astype():** The primary method to convert a column from one type to another (e.g., string to float).
- **to_numeric():** A safer way to convert strings to numbers, providing error handling for non-numeric characters.
- **to_datetime():** Essential for converting string dates into proper datetime objects for time-series analysis.
- **Category Type:** Converting repetitive strings to the `category` type can significantly reduce memory usage.

---

## 3. Data Manipulation & Transformation

### GroupBy: Split-Apply-Combine
- **Split:** Data is broken into groups based on some criteria (e.g., grouping by 'Region').
- **Apply:** A function (like sum, mean, or count) is applied to each group independently.
- **Combine:** The results are gathered back into a new data structure.
- **Analogy:** This is the exact equivalent of the `GROUP BY` clause in SQL.

### Merge vs. Join vs. Concatenate
| Operation | Key Characteristic | SQL Equivalent |
| :--- | :--- | :--- |
| **Merge** | Combines DataFrames based on common columns (keys). | `JOIN` |
| **Join** | Combines DataFrames based on their indices (row names). | `JOIN` (on index) |
| **Concat** | Stacks DataFrames on top of each other or side-by-side. | `UNION ALL` |
| **Pivot** | Reshapes data from "long" to "wide" format. | `PIVOT` |

### Apply, Map, and Applymap
- **map():** Used to substitute each value in a **Series** with another value (often using a dictionary).
- **apply():** Used to apply a function along an axis of a **DataFrame** (rows or columns) or on a **Series**.
- **applymap():** Used to apply a function to every single **element** of a DataFrame individually.
- **Performance:** For large datasets, vectorized operations are usually faster than using these functions.

---

## 4. Analytical Operations

### Reshaping Data: Pivot Table and Melt
- **pivot_table():** Creates a spreadsheet-style summary table, allowing for multi-index grouping and aggregation.
- **melt():** Unpivots a DataFrame from "wide" to "long" format, making it easier to analyze in certain tools.
- **Crosstab:** A specialized version of pivot table specifically for frequency counts (contingency tables).
- **Purpose:** These tools are vital for preparing data for visualization and final reporting.

### Window Functions in Pandas
- **rolling():** Calculates statistics for a moving window of rows (e.g., 7-day moving average).
- **expanding():** Calculates statistics for a window that grows from the start of the data.
- **shift():** Moves data up or down by a specific number of periods (similar to `LAG` and `LEAD` in SQL).
- **Use Case:** Crucial for time-series analysis, calculating growth rates, and smoothing out noise in data.

---

## 5. Focus Areas for Data Analysts

To succeed in a Pandas interview, prioritize these skills:

1.  **Data Cleaning (Highest Priority):** You must know how to handle missing values, duplicates, and incorrect data types. This is 70% of an analyst's work.
2.  **GroupBy & Pivot (High Priority):** Be able to summarize data across different categories and dimensions.
3.  **Merging/Joining (High Priority):** Master how to combine datasets from different sources using `pd.merge()`.
4.  **Indexing & Slicing (Medium Priority):** Understand `loc` and `iloc` to extract specific subsets of data quickly.
5.  **Vectorization (Medium Priority):** Understand that using built-in Pandas functions is faster than writing `for` loops.
6.  **Time Series (Low/Medium Priority):** Know basic date conversion and how to calculate a simple moving average.

### What is often missed?
- **Memory Optimization:** Knowing how to use `chunksize` for large files or converting objects to `category` types.
- **Method Chaining:** Writing clean, readable code by stringing multiple operations together (e.g., `df.dropna().groupby().sum()`).
- **Exploratory Data Analysis (EDA):** Using `df.describe()`, `df.info()`, and `df.head()` to understand a new dataset instantly.

---

## 6. Practical Exercises (Top 50 Operations)

Mastering these code snippets will cover 90% of your daily Pandas tasks as a Data Analyst.

### Basic Exploration
1. **Read CSV:** `df = pd.read_csv('worker.csv')`
2. **First 5 Rows:** `df.head()`
3. **Column Names:** `df.columns`
4. **Statistical Summary:** `df.describe()`
5. **Value Counts:** `df['department'].value_counts()`

### Selection & Filtering
6. **Selection by Position (iloc):** `df.iloc[0:10, 0:3]`
7. **Selection by Name (loc):** `df.loc[0:10, ['first_name', 'salary']]`
8. **Filter by Condition:** `df[df['salary'] > 100000]`
9. **Filter (IN):** `df[df['first_name'].isin(['Vipul', 'Satish'])]`
10. **Multiple Conditions:** `df[(df['salary'] > 50000) & (df['department'] == 'Admin')]`

### String & Date Manipulation
11. **Uppercase Name:** `df['first_name'].str.upper()`
12. **Starts With:** `df[df['first_name'].str.startswith('A')]`
13. **Trim Spaces:** `df['first_name'].str.strip()`
14. **To Datetime:** `df['joining_date'] = pd.to_datetime(df['joining_date'])`
15. **Filter by Year:** `df[df['joining_date'].dt.year == 2014]`

### Data Cleaning
16. **Rename Column:** `df.rename(columns={'old':'new'}, inplace=True)`
17. **Drop Nulls:** `df.dropna()`
18. **Fill Nulls:** `df.fillna(0)`
19. **Drop Duplicates:** `df.drop_duplicates()`
20. **Convert Type:** `df['salary'] = df['salary'].astype(float)`

### Grouping & Aggregating
21. **Group Count:** `df.groupby('department').size()`
22. **Group Aggregation:** `df.groupby('department')['salary'].agg(['sum', 'mean'])`
23. **Pivot Table:** `df.pivot_table(index='department', values='salary', aggfunc='mean')`
24. **Multi-Index Group:** `df.groupby(['department', 'gender']).size()`
25. **Apply Lambda:** `df['salary'].apply(lambda x: x * 1.1)`

### Advanced Manipulation
26. **Merge (Inner):** `pd.merge(df1, df2, on='id', how='inner')`
27. **Concat (Union):** `pd.concat([df1, df2])`
28. **Ranking:** `df['rank'] = df['salary'].rank(method='dense', ascending=False)`
29. **Shift (Lag):** `df['prev_month'] = df['sales'].shift(1)`
30. **Rolling Avg:** `df['7day_avg'] = df['sales'].rolling(7).mean()`
31. **Melt (Wide to Long):** `pd.melt(df, id_vars=['id'], value_vars=['A', 'B'])`
32. **Reset Index:** `df.reset_index(drop=True)`
33. **Sampling:** `df.sample(n=100)`
34. **Find Duplicates:** `df[df.duplicated()]`
35. **Cross Tab:** `pd.crosstab(df['dept'], df['gender'])`
36. **Between:** `df[df['salary'].between(50000, 100000)]`
37. **Replace Values:** `df['status'].replace({'A': 'Active', 'I': 'Inactive'})`
38. **Drop Columns:** `df.drop(columns=['unwanted_col'])`
39. **Sort Values:** `df.sort_values(by='salary', ascending=False)`
40. **Correlation:** `df.corr()`

### Advanced Filtering & Analysis
41. **Query Method:** `df.query('salary > 50000 and department == "Admin"')`
42. **Select Numerics:** `df.select_dtypes(include=['number'])`
43. **Unique Count:** `df['department'].nunique()`
44. **Cumulative Sum:** `df['salary'].cumsum()`
45. **Quantiles:** `df['salary'].quantile([0.25, 0.5, 0.75])`
46. **Memory Usage:** `df.memory_usage(deep=True)`
47. **Explode (List to Rows):** `df.explode('hobbies_list')`
48. **Get Dummies:** `pd.get_dummies(df['department'])`
49. **Interpolate:** `df.interpolate()`
50. **Export to CSV:** `df.to_csv('output.csv', index=False)`
