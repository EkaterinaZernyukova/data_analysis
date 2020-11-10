UPDATE dates SET date = "31.01.1987"

UPDATE dates SET date = "29.01.1987" where date=0

INSERT INTO dates (date, page_id) VALUES ("01.01.2020",1),("01.12.2023",2),(0,5)

UPDATE dates SET date = "29.01.1987" where date=0

UPDATE dates SET date = "31.01.1987"

DELETE FROM dates where page_id =5

SELECT AVG(theme) FROM universal

SELECT AVG(num) FROM universal

SELECT COUNT(theme) FROM universal

SELECT SUM(theme) FROM universal

SELECT universal.title, dates.date as today FROM universal JOIN dates ON universal._id=dates.page_id;
--LEFT - включить пустые поля
SELECT universal.title, dates.date as today FROM universal LEFT JOIN dates ON universal._id=dates.page_id;

SELECT * FROM universal CROSS JOIN dates;

SELECT theme from universal INTERSECT select theme from for_example;
SELECT theme from universal MINUS select theme from for_example;

CREATE VIEW predict(_id,date) AS SELECT _id,date FROM dates;

CREATE INDEX ALLE ON universal (theme);

