select p.project_id, round(avg(e.experience_years), 2) as average_years
from Employee as e
left join Project as p
on p.employee_id = e.employee_id
where p.employee_id is not Null
group by p.project_id;



-- Execute this and see for clarity
-- select *
-- from Employee as e
-- left join Project as p
-- on p.employee_id = e.employee_id;