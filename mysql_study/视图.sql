# 视图
CREATE VIEW empvu80
AS
SELECT employee_id, last_name, salary
FROM employees
WHERE department_id = 80;

SELECT * FROM empvu80;

CREATE VIEW salvu50
AS
SELECT employee_id ID_NUMBER, last_name NAME, salary * 12 ANN_SALARY
FROM employees
WHERE department_id = 50;

# 多表联合视图
CREATE VIEW empview
AS
SELECT employee_id emp_id,last_name NAME, e.department_name
FROM employees e,departments d
WHERE e.department_id = d.department_id;

CREATE VIEW dept_sum_vu (NAME, minsal, maxsal, avgsal)
AS
SELECT d.department_name, MIN(e.salary), max(e.salary), AVG(e.salary)
FROM employees e, departments d
WHERE e.department_id = d.department_id
GROUP BY d.department_name;

CREATE VIEW emp_depart
AS
SELECT concat(last_name, '(', e.department_name, ')') AS emp_dept
FROM employees e JOIN departments d
WHERE e.department_id = d.department_id;

CREATE VIEW emp_dept_ysalary
AS
SELECT emp_dept.ename, dname, year_salary
FROM emp_dept INNER JOIN emp_year_salary
ON emp_dept.ename = emp_year_salary.name;

SHOW TABLES;

SHOW CREATE VIEW empview;