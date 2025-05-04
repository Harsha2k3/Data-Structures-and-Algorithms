select s.user_id , round(sum(case when c.action = "confirmed" then 1 else 0 end) / count(*), 2) as confirmation_rate 
from Signups s
left join Confirmations c on s.user_id = c.user_id
group by s.user_id;


# Why it is not c.user_id?

# We want every user from the Signups table in the result — even 
# if they never made a confirmation request.
# if we used GROUP BY c.user_id, users with no confirmations 
# (like user 6) would be excluded.

#  Run this and see for clarity
-- select *
-- from Signups s
-- left join Confirmations c on s.user_id = c.user_id;