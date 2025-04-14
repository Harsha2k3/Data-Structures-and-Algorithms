# Store the first login date of each player
with temp as
(select player_id , min(event_date) as first_login_date
from Activity 
group by player_id)

# Calculate the fraction
select round(sum(datediff(a.event_date , t.first_login_date) = 1) / count(distinct a.player_id) , 2) as fraction
from Activity as a
join temp as t on a.player_id = t.player_id;