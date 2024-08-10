select
    s.machine_id, 
    round(avg(e.timestamp - s.timestamp) , 3) as processing_time 
from Activity s
join Activity e on e.machine_id=s.machine_id
where s.activity_type='start' and e.activity_type='end'
group by s.machine_id;