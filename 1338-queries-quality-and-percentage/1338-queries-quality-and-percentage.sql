select query_name , round(avg(rating / position) , 2) as quality , round(avg(rating < 3) * 100 , 2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name