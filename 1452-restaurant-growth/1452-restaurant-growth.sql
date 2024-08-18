with dates as (
  select distinct visited_on
  from customer
)

select c1.visited_on , sum(c2.amount) as amount , round(sum(c2.amount) / 7 , 2) as average_amount
from dates c1
join customer c2 on datediff(c1.visited_on , c2.visited_on) between 0 and 6
where datediff(c1.visited_on , (select min(visited_on) from customer)) >= 6
group by c1.visited_on
order by c1.visited_on;