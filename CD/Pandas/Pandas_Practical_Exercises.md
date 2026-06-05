# Pandas Practical Exercises (Top 50 Operations)

This document contains 50 essential Pandas operations that every Data Analyst should master. They are categorized to mirror common SQL workflows.

### 1. Basic Data Exploration
1. **Read CSV:** `df = pd.read_csv('worker.csv')`
2. **First 5 Rows:** `df.head()`
3. **Last 5 Rows:** `df.tail()`
4. **Data Info:** `df.info()`
5. **Statistical Summary:** `df.describe()`
6. **Column Names:** `df.columns`
7. **Shape of Data:** `df.shape`
8. **Check for Nulls:** `df.isnull().sum()`
9. **Unique Values:** `df['department'].unique()`
10. **Value Counts:** `df['department'].value_counts()`

### 2. Selection & Filtering
11. **Select Column:** `df['first_name']`
12. **Select Multiple:** `df[['first_name', 'last_name']]`
13. **Selection by Label (loc):** `df.loc[0:10, 'salary']`
14. **Selection by Position (iloc):** `df.iloc[0:10, 0:3]`
15. **Filter by Condition:** `df[df['salary'] > 100000]`
16. **Filter (IN):** `df[df['first_name'].isin(['Vipul', 'Satish'])]`
17. **Filter (NOT IN):** `df[~df['first_name'].isin(['Vipul', 'Satish'])]`
18. **Between Range:** `df[df['salary'].between(100000, 500000)]`
19. **Multiple Conditions:** `df[(df['salary'] > 50000) & (df['department'] == 'Admin')]`
20. **Filter by Month/Year:** `df[(df['joining_date'].dt.year == 2014) & (df['joining_date'].dt.month == 2)]`

### 3. String Manipulation
21. **Uppercase:** `df['first_name'].str.upper()`
22. **Lowercase:** `df['first_name'].str.lower()`
23. **Contains String:** `df[df['department'].str.contains('Admin')]`
24. **Starts With:** `df[df['first_name'].str.startswith('A')]`
25. **String Slicing:** `df['first_name'].str[:3]`
26. **Replace String:** `df['first_name'].str.replace('a', 'A')`
27. **Trim Whitespace:** `df['first_name'].str.strip()`
28. **Concatenate Strings:** `df['first_name'] + ' ' + df['last_name']`
29. **String Length:** `df['department'].str.len()`
30. **Find Position:** `df['first_name'].str.find('B')`

### 4. Data Cleaning & Transformation
31. **Drop Columns:** `df.drop(columns=['column_name'])`
32. **Rename Columns:** `df.rename(columns={'old_name': 'new_name'})`
33. **Change Data Type:** `df['salary'] = df['salary'].astype(float)`
34. **To Datetime:** `df['joining_date'] = pd.to_datetime(df['joining_date'])`
35. **Drop Duplicates:** `df.drop_duplicates()`
36. **Fill Nulls:** `df.fillna(0)`
37. **Drop Nulls:** `df.dropna()`
38. **Reset Index:** `df.reset_index(drop=True)`
39. **Sort Values:** `df.sort_values(by=['salary', 'first_name'], ascending=[False, True])`
40. **Map Values:** `df['gender'].map({'M': 1, 'F': 0})`

### 5. Aggregation & Grouping
41. **Group By Count:** `df.groupby('department').size()`
42. **Group By Aggregation:** `df.groupby('department')['salary'].agg(['sum', 'mean', 'count'])`
43. **Pivot Table:** `df.pivot_table(index='department', values='salary', aggfunc='mean')`
44. **Cross Tabulation:** `pd.crosstab(df['department'], df['salary_bracket'])`
45. **Apply Function:** `df['salary'].apply(lambda x: x * 1.1)  # 10% raise`

### 6. Merging & Advanced
46. **Merge (Join):** `pd.merge(df1, df2, on='worker_id', how='inner')`
47. **Concatenate (Union):** `pd.concat([df1, df2], axis=0)`
48. **Ranking:** `df['rank'] = df['salary'].rank(method='dense', ascending=False)`
49. **Shift (Lag):** `df['prev_salary'] = df['salary'].shift(1)`
50. **Rolling Mean:** `df['rolling_avg'] = df['salary'].rolling(window=7).mean()`
