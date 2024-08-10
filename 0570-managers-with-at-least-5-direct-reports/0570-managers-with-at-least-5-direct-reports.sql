select e.name
from Employee as e
join employee as m on e.id = m.managerId
group by m.managerId
having count(m.managerId) >= 5;