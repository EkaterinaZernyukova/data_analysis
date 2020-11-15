CREATE TABLE present (user_id int, date text);
INSERT INTO present VALUES (1, '01.07.2018'), (234, '04.10.2018'), (234, '02.07.2018'), (3, '02.07.2018'), (1, '01.07.2018');
WITH mau AS (SELECT DATE_TRUNC("month", date) month_timestamp, COUNT(DISTINCT user_id) mau FROM logins GROUP BY DATE_TRUNC("month", date))
SELECT a.month_timestamp previous_month, a.mau previous_mau, b.month_timestamp current_month, b.mau current_mau, ROUND(100.0*(b.mau - a.mau)/a.mau,2) AS percent_change FROM mau a JOIN mau b ON a.month_timestamp = b.month_timestamp - interval '1 month'

update present set user_id = 2 where "date" ='01.07.2018';
SELECT * from present;

drop table present 

CREATE TABLE present (user_id int primary KEY, date text);
insert into present values ( 1,'01.01.2020'),(2,'01/02/2020'),(3,'01.03.2020');


create table orders (id serial primary key, users integer, quantity integer, FOREIGN KEY(users) references present (user_id));

select * from ORDERS

insert into ORDERS values (1,2,6);
select * from ORDERS;
alter table ORDERS add PHONE VARCHAR(10) null;
select *from ORDERS;
alter table ORDERS add PHONES VARCHAR(10) not null default 'NOT';
select * from ORDERS

ALTER TABLE orders DROP COLUMN phone;
select* from ORDERS;

alter table ORDERS alter column quantity type varchar(20);
alter table orders alter column quantity set not null;
alter table orders alter column quantity drop not null;
alter table orders ADD check (USERS>0);
alter table orders rename column quantity to mix;
select * from orders;
INSERT INTO orders (mix) values (4) returning id;
select * from orders;


select * from orders WHERE not users*id>1 OR users IS NULL;
update orders set id=id+400;
insert into orders (users,mix) values (3,6),(2,8),(1,6)


select distinct users from orders;
select users from orders order BY users DESC;

select users from orders order BY users LIMIT 5 OFFSET 2;
SELECT AVG (id) FROM orders;
SELECT COUNT(DISTINCT users) FROM orders;

SELECT id, COUNT(*) FROM orders WHERE id >6 GROUP BY id ORDER BY id DESC;

SELECT id, COUNT(*) FROM orders GROUP BY id HAVING COUNT(*)>0;

SELECT id, COUNT(*), mix FROM orders GROUP BY GROUPING SETS(id,mix);

SELECT id, COUNT(*),SUM (users) FROM orders GROUP BY ROLLUP (id);


SELECT id, COUNT(*),SUM (users) FROM orders GROUP BY CUBE (id, users);
SELECT * from orders;
ALTER TABLE orders ADD COLUMN indexs VARCHAR (20);
ALTER TABLE orders ALTER COLUMN indexs TYPE VARCHAR (10)[];
ALTER TABLE orders DROP COLUMN indexs;
ALTER TABLE orders ADD COLUMN indexs VARCHAR (20)[];
INSERT INTO orders (indexs) VALUES ('{"sql", "postgres", "database", "plsql"}'); 
SELECT indexs [2:3] FROM orders;

CREATE TYPE request as enum ('min','max');

ALTER TABLE orders ADD COLUMN status request;
UPDATE orders set status='min' where mix='6';

UPDATE orders set status='max' where mix!='6';
UPDATE orders set status='max' where mix=NULL;

ALTER TYPE request ADD VALUE 'middle';
SELECT * from present;

SELECT date,mix FROM present JOIN orders ON user_id=users;
SELECT date,mix,status FROM present RIGHT JOIN orders ON user_id=users;

SELECT * FROM present, orders;




