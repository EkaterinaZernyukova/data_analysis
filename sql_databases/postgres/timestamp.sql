CREATE TABLE emails (id INT,subject character(20),"from" character(20), "to" CHARACTER (20), timestamp timestamp);
INSERT
	INTO
	emails
VALUES 
(1, 'Yosemite', 'zach@g.com', 'thomas@g.com', '2018-01-02 12:45:03'),
(2, 'Big Sur', 'sarah@g.com', 'thomas@g.com', '2018-01-02 16:30:01'),
(3, 'Yosemite', 'thomas@g.com', 'zach@g.com', '2018-01-02 16:35:04'),
(4, 'Running', ' jill@g.com', 'zach@g.com', '2018-01-03 08:12:45'),
(5, 'Yosemite', 'zach@g.com', 'thomas@g.com', '2018-01-03 14:02:01'),
(6, 'Yosemite', 'thomas@g.com', 'zach@g.com', ' 2018-01-03 15:01:05');
SELECT * FROM emails;

SELECT max(timestamp)-min(timestamp) FROM emails;

--разделение timestamp на столбцы времени и даты:
ALTER TABLE emails ADD COLUMN dat date;
ALTER TABLE emails ADD COLUMN tim time;
ALTER TABLE emails DROP COLUMN time;

UPDATE emails SET dat=timestamp::date, tim=timestamp::time;

--фильтр по переписке с zach@g.com:
SELECT * FROM emails WHERE "from" = 'zach@g.com' or "to"= 'zach@g.com' ORDER by (subject);


--время отклика на каждое письмо (id), отправленное на zach@g.com:
SELECT
	A.id, A.subject,
	min(B.timestamp-A.timestamp) AS TIME_TO_RESPOND
FROM
	EMAILS A
JOIN EMAILS B ON
	B.subject = A.subject
	AND A."to" = B."from"
	AND A."from" = B."to"
GROUP BY
	A.id, A.subject;


--Время отклика на 'zach@g.com'

SELECT 
    a.id, 
    MIN(b.timestamp - a.timestamp) as time_to_respond 
FROM 
    emails a 
JOIN
    emails b 
        ON 
            b.subject = a.subject 
        AND 
            a.to = b.from
        AND 
            a.from = b.to 
        AND 
            a.timestamp < b.timestamp 
 WHERE 
    a.to = 'zach@g.com' 
 GROUP BY 
    a.id; 
