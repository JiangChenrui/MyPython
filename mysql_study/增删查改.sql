-- 创建表
CREATE TABLE emp (
-- int类型
emp_id INT,
-- 最多保存20个中英文字符 emp_name VARCHAR(20), -- 总位数不超过15位 salary DOUBLE,
-- 日期类型
birthday DATE
);

CREATE TABLE emp1 AS SELECT * FROM employees;
CREATE TABLE emp2 AS SELECT * FROM employees WHERE 1=2; -- 创建的emp2是空表

ALTER TABLE `emp`ADD emp_name VARCHAR(30);

INSERT INTO departments
VALUES (70, 'Pub', 100, 1700);

INSERT INTO departments
VALUES (100, 'finance', NULL, NULL);

INSERT INTO departments(`department_id`, `department_name`)
VALUES (80, 'IT');

INSERT INTO emp(emp_id, emp_name)
VALUES (1001, 'shkstart'), (1002, 'atguigu'), (1003, 'Tom');

INSERT INTO emp2
SELECT *
FROM employees
WHERE department_id = 90;

INSERT INTO sales_reps(id, NAME, salary, commission_pct)
SELECT employee_id, last_name, salary, commission_pct
FROM   employees
WHERE  job_id LIKE '%REP%';

UPDATE employees
SET department_id = 70
WHERE employee_id = 113;

UPDATE employees
SET department_id = 55
WHERE `department_id` = 110;

SET FOREIGN_KEY_CHECKS=0;
DELETE FROM departments
WHERE department_name = 'Finance';
DELETE FROM departments
WHERE department_id = 60;


CREATE TABLE tb1(
    id INT,
    a INT,
    b INT,
    c INT generated always AS (a + b) virtual
);


INSERT INTO tb1(a, b) VALUES(100, 200);
UPDATE tb1 SET a = 500;
SELECT * FROM tb1;
