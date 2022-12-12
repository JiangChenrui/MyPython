SHOW DATABASES;
SELECT DATABASE();
SHOW TABLES FROM atguigudb;
SHOW CREATE DATABASE atguigudb;
-- 创建表
CREATE TABLE emp (
-- int类型
emp_id INT,
-- 最多保存20个中英文字符 emp_name VARCHAR(20), -- 总位数不超过15位 salary DOUBLE,
-- 日期类型
birthday DATE
);
DESC emp;
CREATE TABLE dept(
    -- int
    deptno INT(2) AUTO_INCREMENT,
    dname VARCHAR(14),
    loc VARCHAR(13),
    PRIMARY KEY (deptno)    
);
DESCRIBE dept;

CREATE TABLE dept80
AS
SELECT employee_id, last_name, salary * 12 ANNSAL, hire_date
FROM employees
WHERE department_id = 80;

DESCRIBE dept80;

SHOW CREATE TABLE dept80;

ALTER TABLE dept80
ADD job_id VARBINARY(15);

ALTER TABLE dept80
ADD department_name VARBINARY(15);

ALTER TABLE dept80
MODIFY last_name VARBINARY(30);

ALTER TABLE dept80
CHANGE department_name dept_name VARCHAR(15);

ALTER TABLE  dept80
DROP COLUMN job_id;

RENAME TABLE emp
TO myemp;

ALTER TABLE dept
RENAME detail_dept;

DROP TABLE dept80;
TRUNCATE TABLE detail_dept;


