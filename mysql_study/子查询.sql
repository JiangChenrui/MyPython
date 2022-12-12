SELECT e2.last_name, e2.salary
FROM employees e1, employees e2
WHERE e1.last_name = 'Abel'
AND e1.salary < e2.salary;

SELECT last_name
FROM employees
WHERE salary > (
		SELECT salary
        FROM employees
        WHERE last_name = 'Abel'
	);
    
SELECT last_name
FROM employees
WHERE salary > (
	SELECT salary
    FROM employees
    WHERE employee_id = 149);

SELECT last_name, job_id, salary
FROM employees
WHERE job_id = (
	SELECT job_id
    FROM employees
    WHERE employee_id = 141
)
AND salary > (
	SELECT salary
    FROM employees
    WHERE employee_id = 143
);

SELECT last_name, job_id, salary
FROM employees
WHERE salary = (
	SELECT MIN(salary)
    FROM employees);

SELECT manager_id, department_id, employee_id
FROM employees
WHERE manager_id IN (
	SELECT manager_id
    FROM employees
    WHERE employee_id IN (141, 174)
)
AND department_id IN (
	SELECT department_id
    FROM employees
    WHERE employee_id IN (141, 174)
)
AND employee_id NOT IN (141, 174);

SELECT manager_id, department_id, employee_id
FROM employees
WHERE (manager_id, department_id) in (
	SELECT manager_id, department_id
	FROM employees
	WHERE employee_id IN (141, 174))
AND employee_id NOT IN (141, 174);

SELECT employee_id, last_name,
	(CASE department_id
	 WHEN
		(SELECT department_id FROM departments WHERE location_id = 1800)
	 THEN 'Canada' ELSE 'USA' END) loaction
FROM employees;

SELECT employee_id, last_name, job_id, salary
FROM employees
WHERE salary < ANY (
	SELECT salary
    FROM employees
    WHERE job_id = 'IT_PROG')
AND job_id <> 'IT_PROG';

SELECT department_id
FROM employees
GROUP BY department_id
HAVING AVG(salary) = (
	SELECT MIN(avg_sal)
    FROM (
		SELECT AVG(salary) avg_sal
        FROM employees
        GROUP BY department_id
    ) dept_avg_sal
);

SELECT department_id
FROM employees
GROUP BY department_id
HAVING AVG(salary) <= ALL(
	SELECT AVG(salary)
    FROM employees
    GROUP BY department_id
);

SELECT last_name, salary, e1.department_id
FROM employees e1, (SELECT department_id, AVG(salary) avg_sal FROM employees GROUP BY department_id) e2
WHERE e1.department_id = e2.department_id
AND e1.salary > e2.avg_sal;

SELECT employee_id, salary, d.department_name
FROM employees e, departments d
ORDER BY (
	SELECT department_name
    FROM departments d
    WHERE e.department_id = d.department_id
);

SELECT employee_id, last_name, job_id, department_id
FROM employees e1
WHERE EXISTS ( 
	SELECT employee_id, last_name, job_id, department_id
    FROM employees e2
    WHERE e2.manager_id = e1.employee_id);

SELECT DISTINCT e1.employee_id, e1.last_name, e1.job_id, e1.department_id
FROM employees e1, employees e2
WHERE e1.employee_id = e2.manager_id;

SELECT employee_id, last_name, job_id, department_id
FROM employees
WHERE employee_id IN (
	SELECT distinct manager_id
    FROM employees);
    
SELECT department_id, department_name
FROM departments d
WHERE NOT EXISTS (
	SELECT 'X'
    FROM employees
    WHERE department_id = d.department_id);

ALTER TABLE employees
ADD(department_name varchar(14));
SET SQL_SAFE_UPDATES = 0;
UPDATE employees e
SET department_name = (
	SELECT department_name
    FROM departments d
    WHERE e.department_id = d.department_id); 
    
#1.查询和Zlotkey相同部门的员工姓名和工资
SELECT last_name, salary
FROM employees
where department_id = (
	SELECT department_id
    FROM employees
    WHERE last_name = 'Zlotkey'
);
#2.查询工资比公司平均工资高的员工的员工号，姓名和工资。
SELECT department_id, last_name, salary
FROM employees
WHERE salary > (
	SELECT AVG(salary)
    FROM employees
);
#3.选择工资大于所有JOB_ID = 'SA_MAN'的员工的工资的员工的last_name, job_id, salary 
SELECT last_name, job_id, salary
FROM employees
WHERE salary > (
	SELECT MAX(salary)
    FROM employees
    WHERE JOB_ID = 'SA_MAN'
);
#4.查询和姓名中包含字母u的员工在相同部门的员工的员工号和姓名 
SELECT employee_id, last_name, department_id
FROM employees
WHERE department_id = ANY (
	SELECT department_id
    FROM employees
    WHERE last_name LIKE '%u%'
);
#5.查询在部门的location_id为1700的部门工作的员工的员工号
SELECT employee_id
FROM employees
WHERE department_id IN (
	SELECT department_id
    FROM departments
    WHERE location_id = 1700
);
#6.查询管理者是King的员工姓名和工资
SELECT last_name, salary
FROM employees
WHERE manager_id in (
	SELECT employee_id
    FROM employees
    WHERE last_name = 'King'
);
#7.查询工资最低的员工信息: last_name, salary
SELECT last_name, salary
FROM employees
WHERE salary = (
	SELECT MIN(salary)
    FROM employees
);
#8.查询平均工资最低的部门信息
SELECT *
FROM departments
WHERE department_id = (
	SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING AVG(salary) = (
		SELECT AVG(salary) as avg_sal
        FROM employees
        GROUP BY department_id
        ORDER BY avg_sal
        LIMIT 0, 1
    )
);

SELECT *
FROM departments
WHERE department_id = (
	SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING AVG(salary) <= ALL(
		SELECT AVG(salary)
        FROM employees
        GROUP BY department_id
    )
);

SELECT *
FROM departments
WHERE department_id = (
	SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING AVG(salary) = (
		SELECT MIN(dept_avgsal)
        FROM (
			SELECT AVG(salary) dept_avgsal
            FROM employees
            GROUP BY department_id
        ) avg_sal
    )
);
#9.查询平均工资最低的部门信息和该部门的平均工资(相关子查询)
SELECT d.*, (SELECT AVG(salary) FROM employees WHERE department_id=d.department_id) avg_sal
FROM departments d
WHERE department_id = (
	SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING AVG(salary) <= ALL (
		SELECT AVG(salary)
        FROM employees
        GROUP BY department_id
    )
);
#10.查询平均工资最高的 job 信息
SELECT *
FROM jobs
WHERE job_id = (
	SELECT job_id
	FROM employees
	GROUP BY job_id
	HAVING AVG(salary) >= ALL(
		SELECT AVG(salary)
		FROM employees
		GROUP BY job_id
	)
);

SELECT *
FROM jobs
WHERE job_id = (
	SELECT job_id
    FROM employees
    GROUP BY job_id
    HAVING AVG(salary) = (
		SELECT MAX(avg_sal)
        FROM (
			SELECT AVG(salary) avg_sal
            FROM employees
            GROUP BY job_id
        ) job_avgsal
    )
);
#11.查询平均工资高于公司平均工资的部门有哪些?
SELECT department_id
FROM employees
WHERE department_id IS NOT NULL
GROUP BY department_id
HAVING AVG(salary) > (
	SELECT AVG(salary)
	FROM employees
);
#12.查询出公司中所有 manager 的详细信息
SELECT *
FROM employees
WHERE employee_id IN (
	 SELECT DISTINCT manager_id
     FROM employees
);
#13.各个部门中 最高工资中最低的那个部门的 最低工资是多少?
SELECT MIN(salary)
FROM employees
WHERE department_id = (
	SELECT department_id
	FROM employees
	GROUP BY department_id
	HAVING MAX(salary) <= ALL(
		SELECT MAX(salary) max_sal
			FROM employees
			GROUP BY department_id
	)
);
#14.查询平均工资最高的部门的 manager 的详细信息: last_name, department_id, email, salary 
#15.查询部门的部门号，其中不包括job_id是"ST_CLERK"的部门号
#16.选择所有没有管理者的员工的last_name 
#17.查询员工号、姓名、雇用时间、工资，其中员工的管理者为 'De Haan' 
#18.查询各部门中工资比本部门平均工资高的员工的员工号, 姓名和工资(相关子查询) 
#19.查询每个部门下的部门人数大于 5 的部门名称(相关子查询)
#20.查询每个国家下的部门个数大于 2 的国家编号(相关子查询)