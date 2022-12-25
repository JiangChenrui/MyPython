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

#1. 使用表employees创建视图employee_vu，其中包括姓名(LAST_NAME)，员工号(EMPLOYEE_ID)，部门 号(DEPARTMENT_ID)
CREATE DATABASE dbtest14;
USE dbtest14;
CREATE OR REPLACE VIEW employee_vu
AS
SELECT last_name, employee_id, department_id
FROM atguigudb.employees;
#2. 显示视图的结构
DESC employee_vu;
#3. 查询视图中的全部内容
SELECT * FROM employee_vu;
#4. 将视图中的数据限定在部门号是80的范围内
CREATE OR REPLACE VIEW employee_vu
AS
SELECT last_name, employee_id, department_id
FROM atguigudb.employees
WHERE department_id=80;
# 练习2
CREATE TABLE emps
AS
SELECT * FROM atguigudb.employees;
#1. 创建视图emp_v1,要求查询电话号码以‘011’开头的员工姓名和工资、邮箱
CREATE OR REPLACE VIEW emp_v1
AS
SELECT last_name, salary, email
FROM emps
WHERE phone_number LIKE '011%';
#2. 要求将视图 emp_v1 修改为查询电话号码以‘011’开头的并且邮箱中包含 e 字符的员工姓名和邮箱、电话号码 
CREATE OR REPLACE VIEW emp_v1
AS
SELECT last_name, salary, email
FROM emps
WHERE phone_number LIKE '011%' AND email LIKE '%e%e';
#3. 向 emp_v1 插入一条记录，是否可以?
DESC emps;
DESC emp_v1;
INSERT INTO emp_v1(last_name,salary,email,phone_number)
VALUES('Tom',2300,'tom@126.com','1322321312');
SELECT * FROM emp_v1;
#4. 修改emp_v1中员工的工资，每人涨薪1000
UPDATE emp_v1
SET salary = salary + 1000;
#5. 删除emp_v1中姓名为Olsen的员工
DELETE FROM emp_v1 WHERE last_name='Olsen';
#6. 创建视图emp_v2，要求查询部门的最高工资高于 12000 的部门id和其最高工资 
CREATE OR REPLACE VIEW emp_v2
AS
SELECT department_id, MAX(salary) max_sal
FROM emps
GROUP BY department_id
HAVING MAX(salary) > 12000;
SELECT * FROM emp_v2;
#7. 向 emp_v2 中插入一条记录，是否可以?
INSERT INTO emp_v2
VALUES(400, 18000);
#8. 删除刚才的emp_v2 和 emp_v1
DROP VIEW if EXISTS emp_v1, emp_v2;