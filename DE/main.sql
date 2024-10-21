create schema deasmnt;


drop table deasmnt.customers;
drop table deasmnt.products;

create table deasmnt.customers 
 (
 cutomer_id int primary key,
 customer_name varchar(100),
 email_address varchar(100),
 country varchar(50)
 );
-- distributed by (customer_id)
 

create table deasmnt.products 
(
product_id int  primary key,
product_name varchar(50),
price decimal(10, 2),
category varchar(50)
);

create table deasmnt.sales_transactions (
    transaction_id bigint primary key,
    customer_id int,
    product_id int,
    purchase_date timestamp,
    quantity int,
    total_amount decimal(10, 2)
);


create table deasmnt.shipping_details (
    transaction_id bigint primary key,
    shipping_date timestamp not null,
    shipping_address varchar(255) not null,
    city varchar(100) not null,
    country varchar(50) not null  
);

-- insert into deasmnt.sales_transactions(transaction_id,
-- purchase_date,
-- total_amount)
-- values(1,'2017-03-14',10);

------------1
select sum(total_amount) as sales_amount, 
	   count(1) as num_of_transactions,
	   date_trunc('month', x.purchase_date) as month 
from deasmnt.sales_transactions x
group by date_trunc('month', x.purchase_date);


------------2
with sales as (
select sum(total_amount) as sales_amount, 
	   count(1) as num_of_transactions,
	   date_trunc('month', x.purchase_date) as month 
from deasmnt.sales_transactions x
group by date_trunc('month', x.purchase_date))
select month,
sales_amount,
avg(sales_amount) over(order by month rows between 2 preceding and current row) as moving_average
from sales;


