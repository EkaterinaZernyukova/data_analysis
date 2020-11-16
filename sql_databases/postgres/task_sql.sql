CREATE TABLE salaries (depname character(20), empno INT, salary INT);
INSERT INTO salaries VALUES ('develop', 11, 5200), ('develop', 7, 4200), ('develop', 9, 4500), ('develop', 8,6000), ('develop', 10, 5200), ('personnel', 5, 3500);
INSERT INTO salaries VALUES ('personnel',2 , 3900), ('sales', 3, 4800), ('sales', 1, 5000), ('sales', 4, 4800);

UPDATE salaries SET salary = 6000 where empno =7;
UPDATE salaries SET salary= CASE WHEN salary!=5000 THEN 10000 END;

SELECT *, RANK () over (PARTITION by depname order by salary) FROM salaries;
SELECT * from salaries

SELECT concat(depname, salary) as test from salaries 

ALTER TABLE sol RENAME to salaries;

SELECT * FROM salaries;

--id with max salary:
SELECT depname, max(salary)as maxim FROM salaries GROUP BY 1;

--фильтр через JOIN
SELECT * FROM salaries JOIN (SELECT depname, max(salary) as maxim FROM salaries GROUP BY 1) Z USING(depname) where maxim =salary;

--фильтр через оконную функцию
SELECT * FROM (SELECT *, max(salary) OVER (PARTITION BY depname) as maxim FROM salaries) Z where maxim =salary; 

--написать запрос, который возвращает ту же таблицу, но с новым столбцом, в котором указана средняя зарплата по департаменту. 
SELECT *, AVG(salary) OVER (PARTITION BY depname) as avg_selary FROM salaries ;

-- округление через временную таблицу 
CREATE TEMP TABLE for_round 
as SELECT *, AVG(salary) OVER (PARTITION BY depname) as avg_selary FROM salaries;

UPDATE for_round SET avg_selary = round(avg_selary,0);
SELECT * FROM for_round

--столбец с позицией каждого сотрудника на основе его зарплаты в своём отделе, 
--где сотрудник с самой высокой зарплатой получает позицию 1.

SELECT *, RANK() OVER (PARTITION BY depname ORDER BY SALARY DESC) as plase FROM salaries;

--выбора записей с нечётными id
--Если остаток от деления id на 2 равен нулю, перед нами чётное значение, и наоборот.

SELECT* FROM salaries where empno %2 !=0

--Как найти дубли в поле 

SELECT depname, COUNT (depname) FROM salaries GROUP BY depname HAVING COUNT (depname)>1;

--список сотрудников с зарплатой выше средней

SELECT depname, round(avg(salary),0) FROM salaries group by depname;
select salary, empno from salaries where salary>(select round(avg(salary),0) FROM salaries)

--Найдите все департаменты без единого сотрудника

CREATE TABLE departments (depname character(20), id INT, name character(20));
INSERT INTO departments VALUES ('develop', 11, 'name'), ('sales', 7, 'name'), ('develop', 9, 'name'), ('develop', 8, 'name'), ('develop', 10, 'name')

INSERT INTO departments (depname,id) VALUES ('sales', 12)

CREATE TABLE CALLS (depname character(20), id_ int);
INSERT into CALLS VALUES ('develop',1),('sales',2),('marketing',3)

select * from departments

SELECT depname FROM CALLS GROUP BY depname EXCEPT SELECT depname from departments GROUP BY depname;


