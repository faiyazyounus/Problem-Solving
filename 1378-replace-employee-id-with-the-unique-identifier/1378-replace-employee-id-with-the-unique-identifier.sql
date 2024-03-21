# Write your MySQL query statement below
select EU.unique_id, E.name
From Employees E
Left Join EmployeeUNI EU
On E.id = EU.id; 