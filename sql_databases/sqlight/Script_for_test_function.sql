CREATE TABLE universal (_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, url TEXT, theme INTEGER, num INTEGER);
PRAGMA TABLE_INFO(universal);
INSERT INTO universal (title,url) VALUES ('python',352);
PRAGMA foreign_keys=ON;
PRAGMA TABLE_INFO(universal);
INSERT INTO universal VALUES (5,"pandas",123,32,34);
INSERT INTO universal VALUES (2,'mpl','text',33,37);
SELECT * FROM universal WHERE num LIKE "%4%";
SELECT * FROM universal;
SELECT title,url FROM universal;
SELECT theme,url FROM universal ORDER BY theme ASC;
SELECT theme,url FROM universal ORDER BY theme DESC;

INSERT INTO universal (theme,num,url) VALUES (1,1,100),(2,2,200),(92,3,300),(9,7,700),(9,29,900);
SELECT * FROM universal;
SELECT _id,url,theme,SUM(theme) OVER() AS SUM FROM universal;
SELECT _id,url,theme,num , SUM(num) OVER(PARTITION BY theme) AS SUM FROM universal;

INSERT INTO universal (theme,num,url) VALUES (1,3,400),(2,3,500),(1,4,600),(2,8,900);
SELECT *FROM universal;
SELECT url,theme,num, SUM(num) OVER (PARTITION BY theme) AS SUM FROM universal;
--нарастающий итог:
SELECT *,SUM(num) OVER (PARTITION BY theme ORDER BY url) AS SUM FROM universal;
SELECT _url,theme , num ,SUM(num) OVER (PARTITION BY theme ORDER BY url) AS SUM FROM universal;
SELECT *,SUM(num) OVER (PARTITION BY theme ORDER BY url,num) AS SUM FROM universal;
PRAGMA foreign_keys=ON;
SELECT _id,url,theme,num, SUM(num) OVER (PARTITION BY theme ORDER BY url,num ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS SUM FROM universal;

UPDATE universal SET theme = 1 WHERE "_id" < 5;
SELECT COUNT(DISTINCT theme) FROM universal;
SELECT COUNT () FROM universal;
SELECT DISTINCT theme FROM universal ORDER BY theme ASC;
SELECT COUNT() FROM universal WHERE theme =2;
SELECT theme FROM universal GROUP BY theme;

SELECT theme, max(num) FROM universal GROUP BY theme;
SELECT universal.title, for_example.url AS theme
FROM universal JOIN for_example
ON universal.theme == for_example._id;

INSERT INTO for_example (theme) VALUES (1),(2),(3),(4),(1),(2),(3),(4),(1),(2),(3),(5);

SELECT universal.title, for_example.num AS theme
FROM universal JOIN for_example
ON universal.theme == for_example._id;

SELECT universal."_id", for_example.theme AS example
FROM universal JOIN for_example
WHERE universal.num == for_example._id;

CREATE TABLE dates(_id INTEGER PRIMARY KEY AUTOINCREMENT, page_id INTEGER NOT NULL, date TEXT, FOREIGN KEY (page_id) REFERENCES universal(_id));

SELECT dates.date, universal.title FROM dates, universal ON dates.page_id == universal._id ORDER BY date(dates.date) DESC;
SELECT date FROM dates WHERE page_id == 8 ORDER BY date DESC;

INSERT INTO universal (theme,num,url) VALUES (1,3,400),(2,3,500),(1,4,600),(2,8,900);

CREATE VIEW temporary_ AS SELECT title, url FROM universal;
SELECT * FROM temporary_;


ALTER TABLE universal RENAME TO portions;
ALTER TABLE portions ADD age INT;
ALTER TABLE portions ADD date TEXT;

ALTER TABLE portions DELETE COLUMN age;
INSERT INTO portions (_id) VALUES (100),(200);

ALTER TABLE portions RENAME COLUMN age to for_del;

TRUNCATE TABLE for_example;
ALTER TABLE portions RENAME TO universal;
PRAGMA foreign_keys=ON;
CREATE TABLE dates(_id INTEGER PRIMARY KEY AUTOINCREMENT, page_id INTEGER NOT NULL, date TEXT, FOREIGN KEY (page_id) REFERENCES universal(_id));

ALTER TABLE dates ADD CHECK (date>5);


--CREATE COLUMN 
--WHERE FOREIGN KEY (theme) REFERENCES for_example(_id);

--PRAGMA TABLE_INFO(for_example);

--DROP TABLE universal;



