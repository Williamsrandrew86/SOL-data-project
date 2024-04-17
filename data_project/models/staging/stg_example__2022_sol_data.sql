with 

source as (

    select * from {{ source('example', '2022_sol_data') }}

),

renamed as (

    select
        level,
        div_num,
        div_name,
        sch_num,
        sch_name,
        sch_type,
        low_grade,
        high_grade,
        subject,
        grade,
        test,
        2021_2022_pass_rate,
        2021_2022_adv_pass_rate

    from source

)

select * from renamed
