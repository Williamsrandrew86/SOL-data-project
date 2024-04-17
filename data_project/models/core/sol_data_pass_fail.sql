
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}



select s23.div_name, s23.sch_name, s23.sch_type, s23.subject, s23.grade, s23.test, s23.2022_2023_pass_rate, s23.2022_2023_adv_pass_rate, s22.2021_2022_pass_rate, s22.2021_2022_adv_pass_rate
, case when s22.2021_2022_pass_rate = -9999 then 'Null'
when s22.2021_2022_pass_rate < 70 then 'Fail'
else 'Pass'
end as Pass_Fail_23
, case when s23.2022_2023_pass_rate = -9999 then 'Null'
when s23.2022_2023_pass_rate < 70 then 'Fail'
else 'Pass'
end as Pass_Fails_22
from valiant-surfer-411804.sol_data.2023_sol_data s23
inner join valiant-surfer-411804.sol_data.2022_sol_data s22 on s23.sch_num = s22.sch_num and s23.subject = s22.subject and s23.grade = s22.grade and s23.test=s22.test and s23.div_num = s22.div_num
where s23.subject not like '%Remote%'

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
