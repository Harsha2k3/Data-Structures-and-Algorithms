select stu.student_id , stu.student_name , sub.subject_name , COUNT(exam.subject_name) as attended_exams
from Students as stu
cross join Subjects as sub
left join Examinations as exam
on stu.student_id = exam.student_id and sub.subject_name = exam.subject_name
group by stu.student_id , sub.subject_name
order by student_id , subject_name;