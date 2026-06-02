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
1. Display all employee details.
SELECT * FROM Employees;

2. Display only employee name.
SELECT emp_name FROM Employees;

3. Display only employee name and salary.
SELECT emp_name, salary FROM Employees;

4. Display all project names.
SELECT project_name FROM Projects;

5. Display employee IDs and cities.
SELECT emp_id, city FROM Employees;

6. Display project budgets.
SELECT budget FROM Projects;

7. Display hire dates of all employees.
SELECT emp_name, hire_date 
FROM Employees;

8. Display employee names and department IDs.
SELECT emp_name, dept_id 
FROM Employees;

9. Display all columns from Departments table.
SELECT * FROM Departments;

### WHERE
1. Find employees earning more than 70000.
SELECT emp_id, salary 
FROM Employees
WHERE salary > 70000;

2. Find employees earning less than 60000.
SELECT emp_id, salary
FROM Employees
WHERE salary < 60000;

3. Find employees from Chicago.
SELECT emp_name, city
FROM Employees
WHERE city = 'Chicago';

4. Find employees from Boston.
SELECT emp_name, city
FROM Employees
WHERE city = 'Boston';

5. Find employees hired after 2021-01-01.
SELECT emp_name, hire_date
FROM Employees 
WHERE hire_date > '2021-01-01';

6. Find employees hired before 2020-01-01.
SELECT emp_name, hire_date
FROM Employees
WHERE hire_date < '2020-01-01';

7. Find employees in department 1.
SELECT emp_name, dept_id 
FROM Employees 
WHERE dept_id = 1;

8. Find female employees.
SELECT emp_name, gender
FROM Employees
WHERE gender = 'Female';

9. Find employees earning exactly 75000.
SELECT emp_id, emp_name, salary
FROM Employees
WHERE salary = 75000;

10. Find employees from Seattle.
SELECT emp_name, city
FROM Employees
WHERE city = 'Seattle';

### ORDER BY
1. Display employees sorted by salary ascending.
2. Display employees sorted by salary descending.
3. Display employees sorted by hire date.

### LIMIT
1. Show the top 3 highest-paid employees.
2. Show the first 5 employees.

### Comparison Operators
1. Find employees with salary >= 80000.
2. Find employees with salary <= 65000.
3. Find employees whose salary is between 60000 and 80000.

### Logical Operators
1. Find employees from Chicago AND earning above 70000.
2. Find employees from Chicago OR Boston.
3. Find employees NOT working in Seattle.

### Aggregate Functions
1. Count total employees.
2. Find total salary paid by company.
3. Find average salary.
4. Find highest salary.
5. Find lowest salary.

### GROUP BY
1. Count employees in each department.
2. Find average salary by department.
3. Find total salary by department.

### HAVING
1. Show departments having more than 1 employee.
2. Show departments whose average salary exceeds 75000.

### DISTINCT
1. List all unique cities.
2. List all unique department IDs from employees.

### CASE WHEN
1. Categorize salaries:
   - High → >= 85000
   - Medium → 65000 to 84999
   - Low → < 65000
2. Categorize employees as:
   - Senior → Salary > 80000
   - Junior → Otherwise

### JOINS
1. Show employee names with department names.
2. Show project names with department names.
3. Show employee names and project names they work on.
4. Show all employees even if they don't have projects (LEFT JOIN).
5. Show all projects even if no employee is assigned.

### UNION
1. Display all cities and department names in one column.
2. Combine employee IDs and project IDs into a single result.

### String Functions
1. Convert employee names to uppercase.
2. Convert employee names to lowercase.
3. Display first 3 characters of employee names.
4. Display last 4 characters of employee names.
5. Extract surname from employee names.
6. Concatenate employee name and city.
7. Find position of letter 'a' in employee names.
8. Remove leading/trailing spaces from a string.

### Window Functions

#### ROW_NUMBER()
1. Assign row numbers based on salary descending.

#### RANK()
1. Rank employees based on salary.

#### DENSE_RANK()
1. Give dense ranking based on salary.

#### PARTITION BY
1. Rank employees within each department.

#### LAG()
1. Show previous employee salary when ordered by salary.

#### LEAD()
1. Show next employee salary when ordered by salary.

#### Running Total
1. Calculate cumulative salary total.

#### Window COUNT()
1. Count employees in each department using window functions.

#### Window AVG()
1. Show department average salary beside every employee.
