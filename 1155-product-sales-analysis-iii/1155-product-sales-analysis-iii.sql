# Store first_year

with nt as
(select product_id , min(year) as first_year
from Sales
group by product_id)

select s.product_id , n.first_year , s.quantity , s.price
from nt as n
join Sales as s on s.product_id = n.product_id and n.first_year = s.year
order by s.product_id;