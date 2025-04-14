select e.name, b.bonus
from Employee as e
left join Bonus as b on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null;


-- select e.name, b.bonus
-- from Employee as e
-- left join Bonus as b on e.empId = b.empId
-- where b.bonus < 1000

-- Output,

-- | name | bonus |
-- | ---- | ----- |
-- | Dan  | 500   |

-- But we might think that,
-- Because when I do left join it gives all the records from the 
-- left table and matched ones from right table and it'll be Null 
-- if it's not on right table right? Then why result is like that?
-- where b.bonus < 1000, This filters out all rows where b.bonus 
-- is NULL — which defeats the purpose of the left join.


-- If we remove where condition

-- select e.name, b.bonus
-- from Employee as e
-- left join Bonus as b on e.empId = b.empId
-- Output,
-- | name   | bonus |
-- | ------ | ----- |
-- | Brad   | null  |
-- | John   | null  |
-- | Dan    | 500   |
-- | Thomas | 2000  |

-- So where b.bonus < 1000, This filters out all rows where b.bonus 
-- is NULL — which defeats the purpose of the left join.