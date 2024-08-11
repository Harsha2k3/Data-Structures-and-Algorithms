select sig.user_id , round(sum(case when action = "confirmed" then 1 else 0 end) / count(*) , 2) as confirmation_rate
from Signups as sig
left join Confirmations as con on sig.user_id = con.user_id
group by sig.user_id