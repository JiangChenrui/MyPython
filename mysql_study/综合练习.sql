CREATE DATABASE IF NOT EXISTS test01_library CHARACTER SET 'utf8';
USE `test01_library`;

CREATE TABLE books(
    id INT,
    name VARCHAR(50),
    `authors` VARCHAR(100) ,
    price FLOAT,
    pubdate YEAR ,
    note VARCHAR(100),
    num INT
);

INSERT INTO books
VALUES(1, 'Tal of AAA', 'Dickes', 23, 1995, 'novel', 11);

INSERT INTO books (id, NAME, `authors`, price, pubdate, note, num)
VALUES(2, 'EmmaT', 'Jane lura', 35, 1993, 'Joke', 22);

INSERT INTO books (id, NAME, `authors`, price, pubdate, note, num) VALUES
(3,'Story of Jane','Jane Tim',40,2001,'novel',0),
(4,'Lovey Day','George Byron',20,2005,'novel',30),
(5,'Old land','Honore Blade',30,2010,'Law',0),
(6,'The Battle','Upton Sara',30,1999,'medicine',40),
(7,'Rose Hood','Richard haggard',28,2008,'cartoon',28);

UPDATE books SET price=price+5 WHERE note = 'novel';

UPDATE books SET price=40, note = 'drama' WHERE NAME = 'EmmaT';

DELETE FROM books WHERE num=0;

SELECT * FROM books WHERE NAME LIKE '%a%';

SELECT count(*), sum(num) FROM books WHERE NAME LIKE '%a%';

DELETE FROM books WHERE num = 0;

SELECT * FROM books WHERE note = 'novel' ORDER BY price DESC;

SELECT * FROM books ORDER BY num DESC, note ASC;

SELECT note, count(*) FROM books GROUP BY note;

SELECT note, sum(num) FROM books GROUP BY note HAVING sum(num)>30;

SELECT * FROM books LIMIT 5, 5;

SELECT note, sum(num) sum_num FROM books GROUP BY note ORDER BY sum_num DESC LIMIT 0, 1;

SELECT * FROM books WHERE CHAR_LENGTH(REPLACE(NAME, ' ', '')) >= 9;

SELECT NAME AS "书名", note, CASE note
    WHEN 'nove' THEN '小说'
    WHEN 'law' THEN '法律'
    WHEN 'medicine' THEN '医药'
    WHEN 'cartoon' THEN '卡通'
    WHEN 'joke' THEN '笑话'
    END AS '类型'
FROM books;

SELECT NAME, num, CASE
    WHEN num > 30 THEN '滞销'
    WHEN num > 0 AND num < 10 THEN '畅销'
    WHEN num = 0 THEN '无货'
    ELSE '正常'
    END AS '库存状态'
FROM books;

SELECT ifnull(note, '合计库存总量') AS note, sum(num) FROM books GROUP BY note WITH ROLLUP;

SELECT * FROM books ORDER BY num DESC LIMIT 0, 3;

SELECT * FROM books ORDER BY pubdate ASC LIMIT 0, 1;

SELECT * FROM books WHERE note = 'novel' ORDER BY price DESC LIMIT 0, 1;

SELECT * FROM books ORDER BY CHAR_LENGTH(REPLACE(NAME, ' ', '')) DESC LIMIT 0, 1;


