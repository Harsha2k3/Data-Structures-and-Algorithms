select patient_id , patient_name , conditions
from Patients
where conditions like "% DIAB1%" or conditions like "DIAB1%";