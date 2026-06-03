# SQL Database Schema and Practice Questions

This document contains the database schema, sample data, and practice questions for SQL learning.

---

## 1. Database Schema

### Departments Table
```sql
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO Departments VALUES
(1,'IT'),
(2,'HR'),
(3,'Finance'),
(4,'Marketing'),
(5,'Sales');
```

### Employees Table
```sql
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    gender VARCHAR(10),
    dept_id INT,
    salary INT,
    city VARCHAR(50),
    hire_date DATE,
    FOREIGN KEY(dept_id) REFERENCES Departments(dept_id)
);

INSERT INTO Employees VALUES
(101,'John Smith','Male',1,60000,'New York','2021-01-15'),
(102,'Sarah Lee','Female',2,75000,'Chicago','2020-05-10'),
(103,'Mike Brown','Male',1,55000,'Boston','2022-02-12'),
(104,'Emma Davis','Female',3,85000,'Seattle','2019-11-25'),
(105,'Chris Wilson','Male',2,70000,'Chicago','2021-09-15'),
(106,'Olivia Taylor','Female',4,95000,'San Francisco','2018-03-30'),
(107,'David Miller','Male',3,80000,'Seattle','2020-12-10'),
(108,'Sophia Clark','Female',5,65000,'Boston','2022-08-01'),
(109,'James Anderson','Male',5,72000,'New York','2021-06-14'),
(110,'Isabella White','Female',4,90000,'Chicago','2019-04-05');
```

### Projects Table
```sql
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    budget INT,
    dept_id INT
);

INSERT INTO Projects VALUES
(201,'Cloud Migration',80000,1),
(202,'Hiring Campaign',30000,2),
(203,'Audit System',50000,3),
(204,'Digital Marketing',60000,4),
(205,'Sales Booster',70000,5);
```

### Employee_Project Table
```sql
CREATE TABLE Employee_Project (
    emp_id INT,
    project_id INT,
    hours_worked INT
);

INSERT INTO Employee_Project VALUES
(101,201,120),
(103,201,150),
(102,202,90),
(105,202,100),
(104,203,80),
(107,203,95),
(106,204,130),
(110,204,140),
(108,205,110),
(109,205,125);
```

---

## 2. SQL Practice Questions

### SELECT
1. **Display all employee details.**

```sql
SELECT * FROM Employees;
```

2. **Display only employee name.**

```sql
SELECT emp_name FROM Employees;
```

3. **Display only employee name and salary.**

```sql
SELECT emp_name, salary FROM Employees;
```

4. **Display all project names.**

```sql
SELECT project_name FROM Projects;
```

5. **Display employee IDs and cities.**

```sql
SELECT emp_id, city FROM Employees;
```

6. **Display project budgets.**

```sql
SELECT budget FROM Projects;
```

7. **Display hire dates of all employees.**

```sql
SELECT emp_name, hire_date 
FROM Employees;
```

8. **Display employee names and department IDs.**

```sql
SELECT emp_name, dept_id 
FROM Employees;
```

9. **Display all columns from Departments table.**

```sql
SELECT * FROM Departments;
```

### WHERE
1. **Find employees earning more than 70000.**

```sql
SELECT emp_id, salary 
FROM Employees
WHERE salary > 70000;
```

2. **Find employees earning less than 60000.**

```sql
SELECT emp_id, salary
FROM Employees
WHERE salary < 60000;
```

3. **Find employees from Chicago.**

```sql
SELECT emp_name, city
FROM Employees
WHERE city = 'Chicago';
```

4. **Find employees from Boston.**

```sql
SELECT emp_name, city
FROM Employees
WHERE city = 'Boston';
```

5. **Find employees hired after 2021-01-01.**

```sql
SELECT emp_name, hire_date
FROM Employees 
WHERE hire_date > '2021-01-01';
```

6. **Find employees hired before 2020-01-01.**

```sql
SELECT emp_name, hire_date
FROM Employees
WHERE hire_date < '2020-01-01';
```

7. **Find employees in department 1.**

```sql
SELECT emp_name, dept_id 
FROM Employees 
WHERE dept_id = 1;
```

8. **Find female employees.**

```sql
SELECT emp_name, gender
FROM Employees
WHERE gender = 'Female';
```

9. **Find employees earning exactly 75000.**

```sql
SELECT emp_id, emp_name, salary
FROM Employees
WHERE salary = 75000;
```

10. **Find employees from Seattle.**

```sql
SELECT emp_name, city
FROM Employees
WHERE city = 'Seattle';
```

### ORDER BY

1. **Sort employees by salary ascending.**
```sql
SELECT emp_name, salary 
FROM Employees 
ORDER BY salary ASC;
```

2. **Sort employees by salary descending.**
```sql
SELECT emp_name, salary 
FROM Employees 
ORDER BY salary DESC;
```

3. **Sort employees by name alphabetically.**
```sql
SELECT emp_id, emp_name 
FROM Employees 
ORDER BY emp_name ASC;
```

4. **Sort employees by city.**
```sql
SELECT emp_name, city 
FROM Employees 
ORDER BY city;
```

5. **Sort employees by hire date.**
```sql
SELECT emp_name, hire_date 
FROM Employees 
ORDER BY hire_date;
```

6. **Sort projects by budget descending.**
```sql
SELECT project_id, budget 
FROM Projects 
ORDER BY budget DESC;
```

7. **Sort projects by budget ascending.**
```sql
SELECT project_id, budget 
FROM Projects 
ORDER BY budget ASC;
```

8. **Sort employees by department and salary.**
```sql
SELECT * FROM Employees 
ORDER BY dept_id, salary;
```

9. **Sort employees by city descending.**
```sql
SELECT * FROM Employees 
ORDER BY city DESC;
```

10. **Sort departments alphabetically.**
```sql
SELECT * FROM Departments 
ORDER BY dept_name ASC;
```

### LIMIT
1. **Show the top 3 highest-paid employees.**

```sql
SELECT * FROM Employees 
ORDER BY salary DESC 
LIMIT 3;
```

2. **Show the first 5 employees.**

```sql
SELECT * FROM Employees 
LIMIT 5;
```

### Comparison Operators
1. **Find employees with salary >= 80000.**

```sql
SELECT * FROM Employees 
WHERE salary >= 80000;
```

2. **Find employees with salary <= 65000.**

```sql
SELECT * FROM Employees 
WHERE salary <= 65000;
```

3. **Find employees whose salary is between 60000 and 80000.**

```sql
SELECT * FROM Employees 
WHERE salary BETWEEN 60000 AND 80000;
```

### Logical Operators
1. **Find employees from Chicago AND earning above 70000.**

```sql
SELECT * FROM Employees 
WHERE city = 'Chicago' AND salary > 70000;
```

2. **Find employees from Chicago OR Boston.**

```sql
SELECT * FROM Employees 
WHERE city = 'Chicago' OR city = 'Boston';
```

3. **Find employees NOT working in Seattle.**

```sql
SELECT * FROM Employees 
WHERE city != 'Seattle';
```

### Aggregate Functions
1. **Count total employees.**

```sql
SELECT COUNT(*) FROM Employees;
```

2. **Find total salary paid by company.**

```sql
SELECT SUM(salary) FROM Employees;
```

3. **Find average salary.**

```sql
SELECT AVG(salary) FROM Employees;
```

4. **Find highest salary.**

```sql
SELECT MAX(salary) FROM Employees;
```

5. **Find lowest salary.**

```sql
SELECT MIN(salary) FROM Employees;
```

### GROUP BY
1. **Count employees in each department.**

```sql
SELECT dept_id, COUNT(*) 
FROM Employees 
GROUP BY dept_id;
```

2. **Find average salary by department.**

```sql
SELECT dept_id, AVG(salary) 
FROM Employees 
GROUP BY dept_id;
```

3. **Find total salary by department.**

```sql
SELECT dept_id, SUM(salary) 
FROM Employees 
GROUP BY dept_id;
```

### HAVING
1. **Show departments having more than 1 employee.**

```sql
SELECT dept_id, COUNT(*) 
FROM Employees 
GROUP BY dept_id 
HAVING COUNT(*) > 1;
```

2. **Show departments whose average salary exceeds 75000.**

```sql
SELECT dept_id, AVG(salary) 
FROM Employees 
GROUP BY dept_id 
HAVING AVG(salary) > 75000;
```

### DISTINCT
1. **List all unique cities.**

```sql
SELECT DISTINCT city FROM Employees;
```

2. **List all unique department IDs from employees.**

```sql
SELECT DISTINCT dept_id FROM Employees;
```

### CASE WHEN
1. **Categorize salaries.**

```sql
SELECT emp_name, salary,
CASE 
    WHEN salary >= 85000 THEN 'High'
    WHEN salary >= 65000 THEN 'Medium'
    ELSE 'Low'
END AS salary_category
FROM Employees;
```

2. **Categorize employees as Senior/Junior.**

```sql
SELECT emp_name, salary,
CASE 
    WHEN salary > 80000 THEN 'Senior'
    ELSE 'Junior'
END AS status
FROM Employees;
```

### JOINS
1. **Show employee names with department names.**

```sql
SELECT e.emp_name, d.dept_name 
FROM Employees e 
JOIN Departments d ON e.dept_id = d.dept_id;
```

2. **Show project names with department names.**

```sql
SELECT p.project_name, d.dept_name 
FROM Projects p 
JOIN Departments d ON p.dept_id = d.dept_id;
```

3. **Show employee names and project names they work on.**

```sql
SELECT e.emp_name, p.project_name 
FROM Employees e 
JOIN Employee_Project ep ON e.emp_id = ep.emp_id 
JOIN Projects p ON ep.project_id = p.project_id;
```

4. **Show all employees even if they don't have projects (LEFT JOIN).**

```sql
SELECT e.emp_name, ep.project_id 
FROM Employees e 
LEFT JOIN Employee_Project ep ON e.emp_id = ep.emp_id;
```

5. **Show all projects even if no employee is assigned.**

```sql
SELECT p.project_name, ep.emp_id 
FROM Projects p 
LEFT JOIN Employee_Project ep ON p.project_id = ep.project_id;
```

### UNION
1. **Display all cities and department names in one column.**

```sql
SELECT city FROM Employees 
UNION 
SELECT dept_name FROM Departments;
```

2. **Combine employee IDs and project IDs into a single result.**

```sql
SELECT emp_id FROM Employees 
UNION 
SELECT project_id FROM Projects;
```

### String Functions
1. **Convert employee names to uppercase.**

```sql
SELECT UPPER(emp_name) FROM Employees;
```

2. **Convert employee names to lowercase.**

```sql
SELECT LOWER(emp_name) FROM Employees;
```

3. **Display first 3 characters of employee names.**

```sql
SELECT SUBSTRING(emp_name, 1, 3) FROM Employees;
```

4. **Display last 4 characters of employee names.**

```sql
SELECT RIGHT(emp_name, 4) FROM Employees;
```

5. **Extract surname from employee names.**

```sql
SELECT SUBSTRING_INDEX(emp_name, ' ', -1) FROM Employees;
```

6. **Concatenate employee name and city.**

```sql
SELECT CONCAT(emp_name, ' - ', city) FROM Employees;
```

7. **Find position of letter 'a' in employee names.**

```sql
SELECT INSTR(emp_name, 'a') FROM Employees;
```

8. **Remove leading/trailing spaces from a string.**

```sql
SELECT TRIM('  example  ');
```

### Window Functions

#### ROW_NUMBER()
1. **Assign row numbers based on salary descending.**

```sql
SELECT emp_name, salary, 
ROW_NUMBER() OVER(ORDER BY salary DESC) as row_num 
FROM Employees;
```

#### RANK()
1. **Rank employees based on salary.**

```sql
SELECT emp_name, salary, 
RANK() OVER(ORDER BY salary DESC) as rnk 
FROM Employees;
```

#### DENSE_RANK()
1. **Give dense ranking based on salary.**

```sql
SELECT emp_name, salary, 
DENSE_RANK() OVER(ORDER BY salary DESC) as dense_rnk 
FROM Employees;
```

#### PARTITION BY
1. **Rank employees within each department.**

```sql
SELECT emp_name, dept_id, salary, 
RANK() OVER(PARTITION BY dept_id ORDER BY salary DESC) as dept_rank 
FROM Employees;
```

#### LAG()
1. **Show previous employee salary when ordered by salary.**

```sql
SELECT emp_name, salary, 
LAG(salary) OVER(ORDER BY salary) as prev_salary 
FROM Employees;
```

#### LEAD()
1. **Show next employee salary when ordered by salary.**

```sql
SELECT emp_name, salary, 
LEAD(salary) OVER(ORDER BY salary) as next_salary 
FROM Employees;
```

#### Running Total
1. **Calculate cumulative salary total.**

```sql
SELECT emp_name, salary, 
SUM(salary) OVER(ORDER BY emp_id) as running_total 
FROM Employees;
```

#### Window COUNT()
1. **Count employees in each department using window functions.**

```sql
SELECT emp_name, dept_id, 
COUNT(*) OVER(PARTITION BY dept_id) as dept_count 
FROM Employees;
```

#### Window AVG()
1. **Show department average salary beside every employee.**

```sql
SELECT emp_name, dept_id, salary, 
AVG(salary) OVER(PARTITION BY dept_id) as dept_avg_salary 
FROM Employees;
```
