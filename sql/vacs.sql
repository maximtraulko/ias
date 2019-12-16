select * from vacs.ias_resume_clean

select * from vacs.ias_vacancy_clean

select c.title,
       c.working_time,
       c.education,
       c.payment_type,
       case when c.payment_type like 'payment_weight_fixed%' then NULLIF(c.salary_from, '')::int
            when c.payment_type = 'payment_weight_range' and c.salary_to is null then 1.15*NULLIF(c.salary_from, '')::int
            when c.payment_type = 'payment_weight_range' and c.salary_from is null then  0.8*NULLIF(c.salary_to, '')::int
            when c.payment_type = 'payment_weight_range' and c.salary_from is not null
                                and c.salary_to is not null then  (NULLIF(c.salary_to, '')::int+NULLIF(c.salary_from, '')::int)/2
       end salary,
       c.salary_from,
       c.salary_to
from vacs.ias_vacancy_clean c;


select distinct c.payment_type from vacs.ias_vacancy_clean c;

select *
from vacs.ias_resume_clean

drop table vacs.ias_resume_one_position;

create table vacs.ias_resume_one_position(
  id serial primary key,
  id_ias_resume_clean int references ias_resume_clean(id),
  pos_name  varchar(512) not null,
  pos_coeff float  not null
);


select t.*,
       1. / coalesce(nullif(count(t.okved_code) over (partition by title),0),1) coefft
from (
       select t.*,
              row_number() over (partition by title order by okved_code) rn
       from (
              select distinct c.title,
                              ov.code okved_code,
                              c.working_time,
                              c.education,
                              c.payment_type,
                              case
                                when c.payment_type like 'payment_weight_fixed%' then NULLIF(c.salary_from, '')::int
                                when c.payment_type = 'payment_weight_range' and c.salary_to is null
                                  then 1.15 * NULLIF(c.salary_from, '')::int
                                when c.payment_type = 'payment_weight_range' and c.salary_from is null
                                  then 0.8 * NULLIF(c.salary_to, '')::int
                                when c.payment_type = 'payment_weight_range' and c.salary_from is not null
                                  and c.salary_to is not null then
                                    (NULLIF(c.salary_to, '')::int + NULLIF(c.salary_from, '')::int) / 2
                                end   salary,
                              c.salary_from,
                              c.salary_to
              from vacs.ias_vacancy_clean c
                     join ld_vacs_okz lvo on lvo.vac_name = c.title
                     join okz okz on okz.id = lvo.id_okz
                     join adapter_class_o aooo on aooo.id_okz = lvo.id_okz
                     join okved ov on ov.id = aooo.id_okved
            ) t
     ) t where t.rn < 10;


select t.*,
       1. / coalesce(nullif(count(t.okso_code) over (partition by vac_name),0),1) coefft
from (select t.*,
             row_number() over (partition by title order by okso_code) rn
      from(
        select distinct c.title, lvo.vac_name,
                                 ov.code okso_code,
                                 c.working_time,
                                 c.education,
                                 c.payment_type,
                                 case
                                   when c.payment_type like 'payment_weight_fixed%' then NULLIF(c.salary_from, '')::int
                                   when c.payment_type = 'payment_weight_range' and c.salary_to is null
                                     then 1.15 * NULLIF(c.salary_from, '')::int
                                   when c.payment_type = 'payment_weight_range' and c.salary_from is null
                                     then 0.8 * NULLIF(c.salary_to, '')::int
                                   when c.payment_type = 'payment_weight_range' and c.salary_from is not null
                                     and c.salary_to is not null then
                                       (NULLIF(c.salary_to, '')::int + NULLIF(c.salary_from, '')::int) / 2
                                   end salary,
                                 c.salary_from,
                                 c.salary_to from vacs.ias_vacancy_clean c
              join ld_vacs_okz lvo on lvo.vac_name = c.title
              join okz okz on okz.id = lvo.id_okz
              join adapter_class_o aooo on aooo.id_okz = lvo.id_okz
              join okso ov on ov.id = aooo.id_okso and ( (substr(ov.code,6,2) in ('05','04','03') and c.education like '%высшее%')
                                                     or (substr(ov.code,6,2) in ('01','02') and not c.education like '%высшее%')
                                                      )
        ) t
       ) t  where t.rn < 10;

select distinct
       lvo.id_okz,
       okz.code,
       okz.name
from vacs.ias_vacancy_clean c
join ld_vacs_okz lvo on lvo.vac_name = c.title
join okz okz on okz.id = lvo.id_okz
left join adapt_okso_okz_okved aooo on aooo.id_okz = lvo.id_okz
left join okved ov on ov.id = aooo.id_okved;


select *
from adapt_okso_okz_okved aooo

select t.title, okved_code, education, sex, wanted_salary,
       coeff/count(okved_code) over (partition by title) coeff
from (
       select t.*,row_number() over (partition by title order by okved_code) rn
       from (
              select distinct coalesce(p.pos_name, r.title) title,
                              ov.code                       okved_code,
                              coalesce(p.pos_coeff, 1)      coeff,
                              r.education,
                              r.sex,
                              r.wanted_salary
              from vacs.ias_resume_clean r
                     left join vacs.ias_resume_one_position p on p.id_ias_resume_clean = r.id
                     join ld_vacs_okz lvo on lvo.vac_name = coalesce(p.pos_name, r.title)
                     join okz okz on okz.id = lvo.id_okz
                     join adapter_class_o aooo on aooo.id_okz = lvo.id_okz
                     join okved ov on ov.id = aooo.id_okved
            ) t
     ) t
where t.rn < 10
order by 1,2;


select t.title, okso_code, education, sex, wanted_salary,
       coeff/count(okso_code) over (partition by title) coeff
from (
       select t.*,row_number() over (partition by title order by okso_code) rn
       from (
              select distinct coalesce(p.pos_name, r.title) title,
                              ov.code                       okso_code,
                              coalesce(p.pos_coeff, 1)      coeff,
                              r.education,
                              r.sex,
                              r.wanted_salary
              from vacs.ias_resume_clean r
                     left join vacs.ias_resume_one_position p on p.id_ias_resume_clean = r.id
                     join ld_vacs_okz lvo on lvo.vac_name = coalesce(p.pos_name, r.title)
                     join okz okz on okz.id = lvo.id_okz
                     join adapter_class_o aooo on aooo.id_okz = lvo.id_okz
                     join okso ov on ov.id = aooo.id_okso
         and ( (substr(ov.code,6,2) in ('05','04','03') and r.education like '%высш%')
                                                     or (substr(ov.code,6,2) in ('01','02') and not r.education like '%высш%')
                                                      )
            ) t
     ) t
where t.rn < 10
order by 1,2;