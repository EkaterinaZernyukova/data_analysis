--найти ежемесячное процентное изменение месячной аудитории активных пользователей (MAU).

CREATE TABLE logins (user_id int, date date);
INSERT INTO logins VALUES (1,'2018-07-01'),(234,'2018-07-02'),(3,'2018-07-02'),(1,'2018-07-02'),(234,'2018-10-04');
SELECT *FROM logins ORDER BY date;
SELECT to_char(date,'Mon')FROM logins;
SELECT * FROM logins GROUP BY date WHERE to_char(date,'Mon'); 
SELECT COUNT(DISTINCT user_id) FROM logins;

SELECT date_trunc('month',date) month_timestamp, COUNT (DISTINCT user_id) mau FROM logins GROUP BY date_trunc('month',date);
SELECT to_char(date,'Mon') MONTH_,COUNT (DISTINCT user_id) mau FROM logins GROUP BY to_char(date,'Mon');


WITH mau AS (
SELECT
	date_trunc('month', date) month_timestamp,
	COUNT (DISTINCT user_id) mau
FROM
	logins
GROUP BY
	date_trunc('month', date))
SELECT
	a.month_timestamp previous_month,
	a.mau previous_mau,
	b.month_timestamp current_month,
	b.mau current_mau,
	round(100.0 *(b.mau-a.mau)/ a.mau, 2) AS persent_change
FROM
	mau a
JOIN mau b ON
	b.month_timestamp = a.month_timestamp + interval '1 month'; 



	

