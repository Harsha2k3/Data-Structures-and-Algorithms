select * from 
(
select s1.id as id , s2.student from Seat s1 , Seat s2 where s1.id % 2 = 1 and s1.id + 1 = s2.id
union 
select s1.id as id , s2.student from Seat s1 , Seat s2 where s1.id % 2 = 0 and s1.id - 1 = s2.id
union
select s.id as id , s.student as student from Seat s where s.id % 2 = 1 and s.id = (select count(*) from Seat)
) 
as Result
order by id;