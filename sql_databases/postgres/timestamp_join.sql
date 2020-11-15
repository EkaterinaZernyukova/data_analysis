CREATE TABLE emails (id INT,subject character(20),"from" character(20), "to" CHARACTER (20), timestamp timestamp);
INSERT
	INTO
	emails
VALUES (2, 'Big Sur', 'sarah@g.com', 'thomas@g.com', '2018-01-02 16:30:01'),
(3, 'Yosemite', 'thomas@g.com', 'zach@g.com', '2018-01-02 16:35:04'),
(4, 'Running', ' jill@g.com', 'zach@g.com', '2018-01-03 08:12:45'),
(5, ' Yosemite', 'zach@g.com', ' thomas@g.com', '2018-01-03 14:02:01'),
(6, 'Yosemite', 'thomas@g.com', 'zach@g.com', ' 2018-01-03 15:01:05');
SELECT * FROM emails ;

SELECT * FROM EMAILS A JOIN EMAILS B ON b.subject = a.subject AND a."to" = b."from" AND a."from" = b."to" WHERE a."to" = 'zach@g.com' GROUP BY a.ID a.subject; 

SELECT"to"FROM emails;

ALTER TABLE emails ADD COLUMN dat date;
ALTER TABLE emails ADD COLUMN tim time;
ALTER TABLE emails DROP COLUMN time;

UPDATE emails SET dat=timestamp::date, tim=timestamp::time;

SELECT * FROM emails WHERE "from" = 'zach@g.com' or "to"= 'zach@g.com';

SELECT A.ID, MIN (B.TIMESTAMP - A.TIMESTAMP) AS TIME_TO_RESPOND FROM EMAILS A JOIN EMAILS B ON B.SUBJECT = A.SUBJECT AND A."to" = B."from" AND A."from" = B."to" AND A.TIMESTAMP > B.TIMESTAMP WHERE A."to" = 'zach@g.com' GROUP BY A.ID;

