-- If there is date 2019-08-16 present then the price on that date would be returned ,if the date is not present then there would be 2 cases:-
-- 1. change date is before 2019-8-16 then the the price which is on any date before this date is selected
-- 2. change date is after 2019-08-16 then we need to assume the price of all products before any change is 10.

select distinct product_id , 10 as price
from Products
group by product_id
having (min(change_date) > "2019-08-16")

union

select p2.product_id , new_price
from Products p2
where (p2.product_id , p2.change_date) in

(
select product_id , max(change_date)
from Products
where change_date <= "2019-08-16"
group by product_id
)