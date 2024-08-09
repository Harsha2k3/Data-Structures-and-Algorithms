select p.project_id , round(avg(e.experience_years) , 2) as average_years
from Project as p
left join Employee as e on p.employee_id = e.employee_id
group by p.project_id

-- (Or)

-- select Project.project_id , round(avg(Employee.experience_years) , 2) as average_years
-- from Project
-- left join Employee on Project.employee_id = Employee.employee_id
-- group by Project.project_id