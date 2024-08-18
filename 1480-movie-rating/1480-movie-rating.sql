(select u.name as results
from Users u
left join MovieRating mr on u.user_id = mr.user_id
group by mr.user_id
order by count(*) desc , u.name
limit 1)

union all

(select m.title as results
from Movies m
left join MovieRating mr on m.movie_id = mr.movie_id
where year(mr.created_at) = 2020 and month(mr.created_at) = 2
group by mr.movie_id
order by avg(mr.rating) desc , m.title
limit 1);

# Only those records which has year(mr.created_at) = 2020 and month(mr.created_at) = 2
# groups together