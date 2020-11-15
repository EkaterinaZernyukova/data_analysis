CREATE TABLE transactions (date date, cash_flow int);
INSERT into transactions values('2018-01-01',-1000),('2018-01-02',-100),('2018-01-03',50);
select * FROM transactions

SELECT *, sum (cash_flow) OVER(ORDER BY cash_flow) AS cumulative_cf from transactions;
