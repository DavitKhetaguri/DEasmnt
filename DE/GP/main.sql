create schema deasmnt;

--- olap სისტემისთვის constraint-ებით (pk-fk დამოკიდებულება, not null) შეზღუდვა არაა კარგი პრაქტიკა. (მითუმეტეს პარალელური პროცესებისას).

create table deasmnt.customers 
 (
 cutomer_id int primary key,
 customer_name varchar(100),
 email_address varchar(100),
 country varchar(50)
 )distributed replicated
;
-- distributed by (customer_id)
 
create table deasmnt.products 
(
product_id int  primary key,
product_name varchar(50),
price decimal(10, 2),
category varchar(50)
)
distributed replicated
;

create table deasmnt.sales_transactions (
    transaction_id bigint,
    customer_id int,
    product_id int,
    purchase_date timestamp,
    quantity int,
    total_amount decimal(10, 2),
    CONSTRAINT sales_transactions_pk primary key ( transaction_id, purchase_date )
)
WITH (appendoptimized=true, orientation=column)
distributed by (transaction_id)
partition by range (purchase_date)
    
(start ('01-01-2020') end ('01-01-2030') every (interval '1 month'));


create table deasmnt.shipping_details (
    transaction_id bigint ,
    shipping_date timestamp ,
    shipping_address varchar(255),
    city varchar(100),
    country varchar(50),
     CONSTRAINT shipping_details_pk primary key ( transaction_id, shipping_date )
)
WITH (appendoptimized=true, orientation=column)
distributed by (transaction_id)
partition by range (shipping_date)
    
(start ('01-01-2020') end ('01-01-2030') every (interval '1 month'));




------------1
select sum(total_amount) as sales_amount, 
	   count(1) as num_of_transactions,
	   date_trunc('day', x.purchase_date) as month 
from deasmnt.sales_transactions x
group by date_trunc('day', x.purchase_date);
------------2

with sales as (
select sum(total_amount) as sales_amount, 
	   count(1) as num_of_transactions,
	   date_trunc('day', x.purchase_date) as month 
from deasmnt.sales_transactions x
group by date_trunc('day', x.purchase_date))
select * from sales;


