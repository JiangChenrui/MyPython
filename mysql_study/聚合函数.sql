-- Active: 1670377058911@@127.0.0.1@3306@atguigudb
USE atguigudb;

SELECT AVG(salary), MAX(salary), MIN(salary), SUM(salary)
FROM employees
WHERE job_id LIKE '%REP%';

SELECT MIN(hire_date), MAX(hire_date)
FROM employees;

SELECT COUNT(*) AS 'count'
FROM employees
WHERE department_id=50;

SELECT COUNT(commission_pct)
FROM employees
WHERE department_id = 80;

SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id;

SELECT department_id dept_id, job_id, SUM(salary)
FROM employees
GROUP BY department_id, job_id
ORDER BY SUM(salary);

SELECT department_id, AVG(salary)
FROM employees
WHERE department_id > 80
GROUP BY department_id WITH ROLLUP;

/*
过滤分组:HAVING子句
1. 行已经被分组。
2. 使用了聚合函数。
3. 满足HAVING 子句中条件的分组将被显示。
4. HAVING 不能单独使用，必须要跟 GROUP BY 一起使用。
*/
SELECT department_id, MAX(salary)
FROM employees
GROUP BY department_id
HAVING MAX(salary) > 10000;

