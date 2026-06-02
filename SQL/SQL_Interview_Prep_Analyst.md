# SQL Interview Preparation Guide for Data Analysts

This guide covers the most critical SQL concepts and questions frequently asked during Data Analyst and Junior Data Analyst interviews.

---

## 1. Fundamentals & Theory

### What is SQL and its Primary Uses?
- **Standard Language:** Structured Query Language (SQL) is the industry-standard language for interacting with Relational Database Management Systems (RDBMS).
- **Data Retrieval:** Its most common use for analysts is querying databases to extract specific datasets for reporting and analysis.
- **Data Manipulation:** It allows users to insert, update, and delete data records to maintain accurate information.
- **Schema Management:** It provides tools to create, modify, and manage the structure of database objects like tables and indexes.

### Difference between DDL and DML
| Feature | Data Definition Language (DDL) | Data Manipulation Language (DML) |
| :--- | :--- | :--- |
| **Primary Purpose** | Defines and modifies the database structure (schema). | Manages and manipulates the actual data within tables. |
| **Core Commands** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`. | `SELECT`, `INSERT`, `UPDATE`, `DELETE`. |
| **Transaction** | Changes are usually auto-committed and permanent. | Changes can be rolled back before being committed. |
| **Scope of Impact** | Affects the entire table or database object. | Affects specific rows or records within a table. |

### DCL and TCL Sublanguages
- **Data Control Language (DCL):** Used to manage permissions and access control (e.g., `GRANT`, `REVOKE`).
- **Transaction Control Language (TCL):** Manages the changes made by DML statements (e.g., `COMMIT`, `ROLLBACK`, `SAVEPOINT`).
- **Security:** DCL ensures that only authorized users can perform specific operations on database objects.
- **Data Integrity:** TCL ensures that a series of operations are either all completed successfully or all reverted in case of failure.

### Difference between SQL and MySQL
| Feature | SQL (Structured Query Language) | MySQL |
| :--- | :--- | :--- |
| **Definition** | A standard programming language for managing relational databases. | A specific open-source Relational Database Management System (RDBMS). |
| **Functionality** | Provides the syntax and rules for querying and manipulating data. | Uses SQL to store, retrieve, and manage data in a server environment. |
| **Updates** | The standard is updated infrequently by committees (ISO/ANSI). | Updated frequently by Oracle with new features and performance fixes. |
| **Usage** | You "write" SQL to interact with any relational database. | You "install" MySQL as a platform to host your data. |

### Normalization vs. Denormalization
- **Normalization:** The process of organizing data into multiple related tables to minimize redundancy and dependency.
- **Denormalization:** The process of combining normalized tables back into a single table to improve read performance.
- **Trade-off:** Normalization favors data integrity and storage efficiency; denormalization favors query speed and simplicity.
- **Use Case:** Use normalization for transactional systems (OLTP) and denormalization for reporting/analytical systems (OLAP).

### ACID Properties of Transactions
- **Atomicity:** Ensures that all operations within a transaction are treated as a single unit; they all succeed or all fail.
- **Consistency:** Ensures that a transaction brings the database from one valid state to another, maintaining all rules and constraints.
- **Isolation:** Ensures that concurrent transactions do not interfere with each other, appearing as if they executed sequentially.
- **Durability:** Ensures that once a transaction is committed, its changes are permanent, even in the event of a system crash.

### Difference between SQL and NoSQL
| Feature | SQL (Relational) | NoSQL (Non-Relational) |
| :--- | :--- | :--- |
| **Data Model** | Structured data stored in predefined tables and rows. | Unstructured or semi-structured data (Key-Value, Document, Graph). |
| **Schema** | Rigid and predefined; requires a schema before inserting data. | Flexible and dynamic; allows for changing data structures on the fly. |
| **Scaling** | Vertically scalable (adding more power to a single server). | Horizontally scalable (adding more servers to a cluster). |
| **Ideal For** | Complex queries, multi-row transactions, and high data integrity. | Large-scale data, rapid development, and varying data types. |

### Normalization (1NF, 2NF, 3NF)
- **1st Normal Form (1NF):** Ensures that every column contains atomic (indivisible) values and each record is unique.
- **2nd Normal Form (2NF):** Meets all 1NF requirements and ensures all non-key columns are fully dependent on the primary key.
- **3rd Normal Form (3NF):** Meets all 2NF requirements and ensures no "transitive dependencies" (non-key columns depending on other non-key columns).
- **Goal:** The primary objective of normalization is to reduce data redundancy and improve data integrity across the database.

### Difference between OLTP and OLAP
| Feature | OLTP (Online Transactional Processing) | OLAP (Online Analytical Processing) |
| :--- | :--- | :--- |
| **Objective** | Optimized for fast, frequent business transactions. | Optimized for complex data analysis and reporting. |
| **Data Source** | Real-time operational data from daily activities. | Historical data consolidated from multiple OLTP sources. |
| **Query Type** | Simple, short queries affecting a few records. | Complex queries involving large volumes of data and aggregations. |
| **Design Pattern** | Highly normalized to ensure fast writes and integrity. | Often denormalized (Star/Snowflake) to speed up reads. |

---

## 2. Data Retrieval & Querying

### SQL Order of Execution
- **Step 1 (Source):** The database first identifies the source tables in the `FROM` and `JOIN` clauses.
- **Step 2 (Filter):** It then applies row-level filters using the `WHERE` clause before any grouping occurs.
- **Step 3 (Group & Aggregate):** Data is grouped via `GROUP BY`, and aggregate functions (like `SUM` or `AVG`) are calculated.
- **Step 4 (Final Filter & Sort):** The `HAVING` clause filters groups, the `SELECT` picks columns, and `ORDER BY` sorts the final output.

### Difference between WHERE and HAVING
| Feature | WHERE Clause | HAVING Clause |
| :--- | :--- | :--- |
| **Filtering Level** | Filters individual rows before they are grouped. | Filters summarized groups after the GROUP BY clause. |
| **Aggregates** | Cannot be used with aggregate functions (e.g., `WHERE SUM(val) > 10` fails). | Specifically designed to work with aggregate functions. |
| **Placement** | Comes before the `GROUP BY` clause. | Comes after the `GROUP BY` clause. |
| **Performance** | More efficient as it reduces the data size early in execution. | Less efficient as it processes data after aggregation is complete. |

### SQL JOINs Explained
- **INNER JOIN:** Returns only the records where there is a matching value in both the left and right tables.
- **LEFT JOIN:** Returns all records from the left table and the matched records from the right; unmatched right side returns NULL.
- **RIGHT JOIN:** Returns all records from the right table and the matched records from the left; unmatched left side returns NULL.
- **FULL OUTER JOIN:** Returns all records when there is a match in either the left or right table, filling with NULLs where matches are missing.

### Pattern Matching: LIKE vs. REGEXP
| Feature | LIKE Operator | REGEXP Operator |
| :--- | :--- | :--- |
| **Simplicity** | Uses simple wildcards (`%` for any characters, `_` for one). | Uses complex regular expression patterns for advanced matching. |
| **Precision** | Limited to basic prefix, suffix, and "contains" searches. | Can match specific character classes, repetitions, and groupings. |
| **Performance** | Generally faster for simple patterns due to indexing support. | Can be significantly slower as it requires more CPU processing. |
| **Syntax** | Standard across almost all SQL dialects. | Syntax varies (e.g., `REGEXP` in MySQL/BigQuery, `~` in Postgres). |

### Wildcards and OFFSET FETCH
- **% Wildcard:** Represents zero or more characters (e.g., `'A%'` matches 'Amit' and 'Abhishek').
- **_ Wildcard:** Represents exactly one character (e.g., `'L_m%'` matches 'Lamp' but not 'Lump').
- **OFFSET Clause:** Specifies the number of rows to skip before starting to return rows from the query.
- **FETCH Clause:** Specifies the exact number of rows to return after the OFFSET has been applied.

### Set Operators: INTERSECT vs. EXCEPT
| Feature | INTERSECT | EXCEPT / MINUS |
| :--- | :--- | :--- |
| **Logic** | Returns only the rows that appear in BOTH result sets. | Returns rows from the first set that do NOT appear in the second. |
| **Requirements** | Both queries must have the same number of columns and data types. | Both queries must have the same column structure and data types. |
| **Duplicates** | Removes duplicate rows from the final result by default. | Removes duplicates from the final result by default. |
| **Use Case** | Use to find common records between two tables. | Use to find records in one table that are missing from another. |

### ALL, ANY, and SOME Operators
- **ANY / SOME:** Returns TRUE if the comparison is true for *at least one* value in the subquery result.
- **ALL:** Returns TRUE if the comparison is true for *every single* value in the subquery result.
- **Context:** These are used with comparison operators (=, <, >, etc.) against a list returned by a subquery.
- **Analysts' View:** They are powerful alternatives to `IN` and `EXISTS` when comparing values across groups.

### Difference between UNION and UNION ALL
| Feature | UNION | UNION ALL |
| :--- | :--- | :--- |
| **Duplicates** | Automatically removes duplicate rows from the final result set. | Retains all rows, including duplicates, from all query parts. |
| **Performance** | Slower because it requires an internal sorting/distinct operation. | Faster as it simply appends the results together without checking. |
| **Data Volume** | Typically produces a smaller, unique result set. | Produces a larger result set containing every row found. |
| **Use Case** | Use when you need a distinct list of items from multiple sources. | Use when you need a complete record count or performance is critical. |

---

## 3. Advanced Querying

### Common Table Expressions (CTEs) vs. Subqueries
- **Readability:** CTEs use the `WITH` clause to define temporary results at the top, making complex queries much easier to read.
- **Reusability:** A single CTE can be referenced multiple times within the same query, whereas subqueries must be rewritten.
- **Recursion:** CTEs support recursive logic (self-referencing), which is impossible to achieve with standard subqueries.
- **Scope:** Both are temporary; however, CTEs are often preferred in modern SQL for their "top-down" logical flow.

### Window Functions: RANK vs. DENSE_RANK
- **RANK():** Assigns a rank to each row; if there is a tie, it skips the next rank (e.g., 1, 2, 2, 4).
- **DENSE_RANK():** Assigns a rank to each row; if there is a tie, it does NOT skip the next rank (e.g., 1, 2, 2, 3).
- **ROW_NUMBER():** Assigns a unique, sequential integer to every row regardless of ties (e.g., 1, 2, 3, 4).
- **Use Case:** These are essential for finding the "Top N" items per category or calculating running totals.

### LAG and LEAD Functions
- **LAG Function:** Allows you to access data from a previous row in the same result set without using a self-join.
- **LEAD Function:** Allows you to access data from a subsequent row in the same result set, useful for forward-looking comparisons.
- **Offset Parameter:** You can specify how many rows back or forward to look (default is 1).
- **Analysis:** Analysts use these to calculate period-over-period growth or identify trends between consecutive events.

### FIRST_VALUE and LAST_VALUE
- **Purpose:** These window functions return the first and last values in an ordered set of data.
- **Window Frame:** They require a specific window frame (e.g., `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`) to work correctly.
- **Use Case:** Finding the starting price and ending price for a stock within a month.
- **Benefit:** They provide context from the boundaries of a partition without requiring complex self-joins or aggregations.

### EXISTS vs. IN Operators
| Feature | EXISTS Operator | IN Operator |
| :--- | :--- | :--- |
| **Logic** | Checks for the existence of ANY row returned by a subquery. | Checks if a value matches ANY value in a provided list. |
| **Performance** | Faster for large subqueries as it stops as soon as a match is found. | Can be slower for large lists as it may process the entire set. |
| **NULL Handling** | Returns TRUE/FALSE regardless of NULLs in the subquery. | Can produce unexpected results (UNKNOWN) if the list contains NULLs. |
| **Use Case** | Use when you only care if a matching record exists elsewhere. | Use when you have a specific, small list of values to match against. |

### PIVOT and UNPIVOT
- **PIVOT:** Rotates a table-valued expression by turning unique values from one column into multiple columns in the output.
- **UNPIVOT:** Performs the opposite operation, rotating columns into rows to normalize the data structure.
- **Reporting:** PIVOT is extremely useful for creating cross-tab reports (e.g., Sales by Year as columns).
- **Cleanup:** UNPIVOT is often used to fix "wide" tables that were designed for manual entry but need to be normalized for analysis.

### GROUPING SETS, ROLLUP, and CUBE
- **GROUPING SETS:** Allows you to define multiple grouping criteria in a single query (e.g., group by Year, then by Region).
- **ROLLUP:** Creates hierarchical subtotals (e.g., Total by Year -> Total by Month -> Grand Total).
- **CUBE:** Generates subtotals for every possible combination of the specified columns (power set).
- **Efficiency:** These operators are much more efficient than using multiple `UNION ALL` statements for subtotal reporting.

### Recursive CTEs and Self-Joins
- **Recursive CTE:** A CTE that references itself, allowing you to traverse hierarchical data (e.g., Org Charts, Bill of Materials).
- **Self-Join:** Joining a table to itself to compare rows within the same table (e.g., finding employees who earn more than their managers).
- **Anchor Member:** Every recursive query must have an initial "anchor" query that doesn't reference the CTE.
- **Termination:** A recursive CTE continues until the recursive part returns no more rows or a limit is reached.

---

## 4. Performance & Design

### Difference between DELETE, TRUNCATE, and DROP
| Feature | DELETE | TRUNCATE | DROP |
| :--- | :--- | :--- | :--- |
| **Type** | DML (Data Manipulation) | DDL (Data Definition) | DDL (Data Definition) |
| **Action** | Removes specific rows based on a condition. | Removes all rows but keeps the table structure. | Removes the entire table and its structure. |
| **Rollback** | Can be rolled back if used within a transaction. | Generally cannot be rolled back (depends on DB engine). | Cannot be rolled back. |
| **Speed** | Slowest (logs each row deletion). | Faster than DELETE (minimal logging). | Instant (removes object from schema). |

### Star Schema vs. Snowflake Schema
- **Star Schema:** A central "Fact" table surrounded by "Dimension" tables; it is the simplest and most common data warehousing design.
- **Snowflake Schema:** An extension of the Star Schema where dimension tables are normalized into multiple related tables.
- **Read Performance:** Star schemas are generally faster for reading and querying because they require fewer joins.
- **Maintenance:** Snowflake schemas save storage space and reduce redundancy but are more complex to maintain and query.

### Primary Key vs. Unique Constraint
| Feature | Primary Key | Unique Constraint |
| :--- | :--- | :--- |
| **Null Values** | Strictly does NOT allow NULL values in the column. | Allows NULL values (usually only one, depending on the DB). |
| **Count** | Only one Primary Key is allowed per table. | Multiple Unique constraints can be defined on a single table. |
| **Clustered Index** | Automatically creates a clustered index by default. | Creates a non-clustered index by default. |
| **Purpose** | Uniquely identifies each record in the table for relationships. | Ensures data integrity by preventing duplicate values in a column. |

### Clustered vs. Non-Clustered Indexes
| Feature | Clustered Index | Non-Clustered Index |
| :--- | :--- | :--- |
| **Data Storage** | Stores the actual data rows in the leaf nodes of the index. | Stores pointers (row identifiers) to the actual data rows. |
| **Quantity** | Only one per table because data can only be sorted in one way. | Multiple per table (e.g., up to 999 in SQL Server). |
| **Structure** | The table *is* the index; the data is physically reordered. | A separate object from the table; it contains a sorted list of values. |
| **Performance** | Faster for range searches as data is physically contiguous. | Faster for specific lookups on non-key columns. |

### Execution Plans and Statistics
- **Execution Plan:** The roadmap created by the database engine showing how it will execute a query (e.g., Index Seek vs. Table Scan).
- **Statistics:** Metadata about the distribution of data in columns; the query optimizer uses this to pick the most efficient plan.
- **Optimization:** Analysts use execution plans to identify bottlenecks, such as missing indexes or expensive joins.
- **Accuracy:** Outdated statistics can lead to poor query plans; regular maintenance is required for consistent performance.

### Database Partitioning
- **Definition:** Dividing a large table or index into smaller, more manageable pieces (partitions) while appearing as one table.
- **Horizontal Partitioning:** Splitting rows across different tables (e.g., Sales 2023, Sales 2024).
- **Vertical Partitioning:** Splitting columns into different tables to reduce I/O (e.g., moving large text blobs to a separate table).
- **Benefit:** Improves performance by allowing "partition pruning," where the engine only scans relevant chunks of data.

### Star Schema vs. Snowflake Schema

### Handling NULL, Zero, and Empty Strings
- **NULL Value:** Represents a "missing" or "unknown" value; it is not equal to zero or an empty string.
- **Zero (0):** A defined numerical value; arithmetic operations with zero are valid, unlike with NULL.
- **Empty String (' '):** A string of zero length; it is a known value, whereas NULL is unknown.
- **Comparison:** In SQL, `column = NULL` is always false; you must use the `IS NULL` operator to check for it.

### Finding the Nth Highest Salary
- **Method 1 (Subquery):** Use a correlated subquery to count how many salaries are greater than the current one.
- **Method 2 (Window Function):** Use `DENSE_RANK()` in a CTE to assign ranks to salaries and then filter where rank = N.
- **Method 3 (Offset/Limit):** Use `ORDER BY Salary DESC` with `LIMIT 1 OFFSET N-1` (syntax varies by database).
- **Edge Cases:** Always use `DISTINCT` or `DENSE_RANK` to handle duplicate salary values correctly.

### Date and Time Manipulation
- **Extraction:** Functions like `EXTRACT()` or `YEAR()`, `MONTH()` are used to pull specific parts from a date.
- **Arithmetic:** `DATEADD()` or `DATEDIFF()` allow you to calculate the time elapsed between two dates.
- **Formatting:** `TO_CHAR()` or `FORMAT()` functions convert date objects into readable string formats.
- **Current Date:** Each system has a reserved keyword (e.g., `GETDATE()`, `CURRENT_DATE`, `NOW()`) to fetch the system time.

### COALESCE and CASE Statements
- **COALESCE:** Returns the first non-NULL value in a list; it is perfect for providing default values for missing data.
- **CASE Statement:** SQL's version of IF-THEN logic; it allows for conditional data transformation within a query.
- **Data Cleaning:** Analysts use COALESCE to replace NULLs with "Unknown" or 0 to avoid broken calculations.
### Categorization: CASE statements are frequently used to bucket continuous variables (e.g., "High", "Medium", "Low" based on price).

---

## 5. Practical Exercises (Top 50 Queries)

These queries are based on a standard `Worker` table. Practice these to master data retrieval and manipulation.

### Basic Retrieval & Formatting
1. **Alias Name:** `SELECT first_name AS WORKER_NAME FROM worker;`
2. **Uppercase:** `SELECT UPPER(first_name) FROM worker;`
3. **Unique Departments:** `SELECT DISTINCT department FROM worker;`
4. **First 3 Characters:** `SELECT SUBSTRING(first_name, 1, 3) FROM worker;`
5. **Position of 'b':** `SELECT INSTR(first_name, 'B') FROM worker WHERE first_name = 'Amitabh';`
6. **Remove Right Space:** `SELECT RTRIM(first_name) FROM worker;`
7. **Remove Left Space:** `SELECT LTRIM(department) FROM worker;`
8. **Length of Unique Values:** `SELECT DISTINCT department, LENGTH(department) FROM worker;`
9. **Replace Character:** `SELECT REPLACE(first_name, 'a', 'A') FROM worker;`
10. **Concatenate Names:** `SELECT CONCAT(first_name, ' ', last_name) AS COMPLETE_NAME FROM worker;`

### Sorting & Filtering
11. **Order by Name:** `SELECT * FROM worker ORDER BY first_name ASC;`
12. **Multi-Column Sort:** `SELECT * FROM worker ORDER BY first_name ASC, department DESC;`
13. **Specific Values (IN):** `SELECT * FROM worker WHERE first_name IN ('Vipul', 'Satish');`
14. **Excluding Values:** `SELECT * FROM worker WHERE first_name NOT IN ('Vipul', 'Satish');`
15. **Wildcard Match:** `SELECT * FROM worker WHERE department LIKE 'Admin%';`
16. **Contains 'a':** `SELECT * FROM worker WHERE first_name LIKE '%a%';`
17. **Ends with 'a':** `SELECT * FROM worker WHERE first_name LIKE '%a';`
18. **Length & Suffix:** `SELECT * FROM worker WHERE first_name LIKE '_____h';`
19. **Salary Range:** `SELECT * FROM worker WHERE salary BETWEEN 100000 AND 500000;`
20. **Join Date Month:** `SELECT * FROM worker WHERE YEAR(joining_date) = 2014 AND MONTH(joining_date) = 2;`

### Aggregation & Joins
21. **Count by Dept:** `SELECT COUNT(*) FROM worker WHERE department = 'Admin';`
22. **Names by Salary:** `SELECT CONCAT(first_name, ' ', last_name) FROM worker WHERE salary BETWEEN 50000 AND 100000;`
23. **Dept Count (Desc):** `SELECT department, COUNT(worker_id) AS cnt FROM worker GROUP BY department ORDER BY cnt DESC;`
24. **Workers who are Managers:** `SELECT w.* FROM worker w JOIN title t ON w.worker_id = t.worker_ref_id WHERE t.worker_title = 'Manager';`
25. **Duplicate Titles:** `SELECT worker_title, COUNT(*) FROM title GROUP BY worker_title HAVING COUNT(*) > 1;`

### Advanced Operations
26. **Odd Rows:** `SELECT * FROM worker WHERE MOD(worker_id, 2) <> 0;`
27. **Even Rows:** `SELECT * FROM worker WHERE MOD(worker_id, 2) = 0;`
28. **Clone Table:** `CREATE TABLE worker_clone LIKE worker; INSERT INTO worker_clone SELECT * FROM worker;`
29. **Intersect Records:** `SELECT * FROM worker INNER JOIN worker_clone USING(worker_id);`
30. **Minus Records:** `SELECT w.* FROM worker w LEFT JOIN worker_clone c USING(worker_id) WHERE c.worker_id IS NULL;`
31. **Current Date/Time:** `SELECT CURDATE(); SELECT NOW();`
32. **Top 5 Salaries:** `SELECT * FROM worker ORDER BY salary DESC LIMIT 5;`
33. **5th Highest Salary:** `SELECT * FROM worker ORDER BY salary DESC LIMIT 4,1;`
34. **Nth Salary (No Limit):** `SELECT salary FROM worker w1 WHERE n-1 = (SELECT COUNT(DISTINCT w2.salary) FROM worker w2 WHERE w2.salary > w1.salary);`
35. **Same Salary Workers:** `SELECT w1.* FROM worker w1, worker w2 WHERE w1.salary = w2.salary AND w1.worker_id != w2.worker_id;`

### Subqueries & Limits
36. **2nd Highest Salary:** `SELECT MAX(salary) FROM worker WHERE salary < (SELECT MAX(salary) FROM worker);`
37. **Double Row (UNION):** `SELECT * FROM worker UNION ALL SELECT * FROM worker ORDER BY worker_id;`
38. **No Bonus Workers:** `SELECT worker_id FROM worker WHERE worker_id NOT IN (SELECT worker_ref_id FROM bonus);`
39. **First 50% Records:** `SELECT * FROM worker WHERE worker_id <= (SELECT COUNT(worker_id)/2 FROM worker);`
40. **Small Depts:** `SELECT department FROM worker GROUP BY department HAVING COUNT(department) < 4;`
41. **Dept Employee Count:** `SELECT department, COUNT(department) FROM worker GROUP BY department;`
42. **Last Record:** `SELECT * FROM worker WHERE worker_id = (SELECT MAX(worker_id) FROM worker);`
43. **First Record:** `SELECT * FROM worker WHERE worker_id = (SELECT MIN(worker_id) FROM worker);`
44. **Last 5 Records:** `(SELECT * FROM worker ORDER BY worker_id DESC LIMIT 5) ORDER BY worker_id;`
45. **Max Salary per Dept:** `SELECT w.department, w.first_name, w.salary FROM worker w JOIN (SELECT department, MAX(salary) AS ms FROM worker GROUP BY department) t ON w.department = t.department AND w.salary = t.ms;`
46. **Top 3 Salaries (Corr):** `SELECT DISTINCT salary FROM worker w1 WHERE 3 >= (SELECT COUNT(DISTINCT salary) FROM worker w2 WHERE w1.salary <= w2.salary) ORDER BY salary DESC;`
47. **Bottom 3 Salaries (Corr):** `SELECT DISTINCT salary FROM worker w1 WHERE 3 >= (SELECT COUNT(DISTINCT salary) FROM worker w2 WHERE w1.salary >= w2.salary) ORDER BY salary DESC;`
48. **Nth Highest (Generic):** `SELECT DISTINCT salary FROM worker w1 WHERE n = (SELECT COUNT(DISTINCT salary) FROM worker w2 WHERE w2.salary >= w1.salary);`
49. **Dept Total Salary:** `SELECT department, SUM(salary) FROM worker GROUP BY department ORDER BY SUM(salary) DESC;`
50. **Max Salary Earners:** `SELECT first_name, salary FROM worker WHERE salary = (SELECT MAX(salary) FROM worker);`

---

## 6. Focus Areas for Data Analysts

To succeed in a Data Analyst interview, prioritize your study time in this order:

1.  **JOINS & CTEs (High Priority):** Master the logic of combining tables. You should be able to write a multi-join query using CTEs without hesitation.
2.  **Window Functions (High Priority):** Understand `RANK`, `DENSE_RANK`, and `ROW_NUMBER`. Practice using `LAG` and `LEAD` for trend analysis.
3.  **Aggregation & Filtering (High Priority):** Be very clear on `GROUP BY` vs. `WHERE` vs. `HAVING`. This is a frequent trap for beginners.
4.  **Handling NULLs (Medium Priority):** Know how `COALESCE` works and how NULLs impact counts and sums (they are usually ignored).
5.  **Performance Basics (Medium Priority):** Know what an Index does and why a full table scan is bad. You don't need to be a DBA, but you should know how to write efficient queries.
6.  **Schema Design (Low/Medium Priority):** Understand Star vs. Snowflake schemas. As an analyst, you'll be querying these structures daily.

### What's Missing? (Bonus Topics)
- **Data Quality Checks:** How would you find duplicate records or missing IDs in a large dataset?
- **Pivoting in Practice:** Many analyst tasks involve transforming data from a narrow format to a wide format for Excel/Dashboards.
- **Querying JSON:** In modern roles, knowing how to extract data from a JSON column using `JSON_EXTRACT` or similar is increasingly important.

