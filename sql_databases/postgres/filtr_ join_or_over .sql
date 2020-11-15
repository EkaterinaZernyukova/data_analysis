CREATE TABLE salaries (depname character(20), empno INT, salary INT);
INSERT INTO salaries VALUES ('develop', 11, 5200), ('develop', 7, 4200), ('develop', 9, 4500), ('develop', 8,6000), ('develop', 10, 5200), ('personnel', 5, 3500);
INSERT INTO salaries VALUES ('personnel',2 , 3900), ('sales', 3, 4800), ('sales', 1, 5000), ('sales', 4, 4800);

UPDATE salaries SET salary = 6000 where empno=7;

SELECT * FROM salaries;

SELECT depname, max(salary)as maxim FROM salaries GROUP BY 1;

--фильтр через JOIN
SELECT * FROM salaries JOIN (SELECT depname, max(salary) as maxim FROM salaries GROUP BY 1) Z USING(depname) where maxim =salary;

--фильтр через оконную функцию
SELECT * FROM (SELECT *, max(salary) OVER (PARTITION BY depname) as maxim FROM salaries) Z where maxim =salary; 

