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


select coalesce(p.pos_name,r.title) title,
       coalesce(p.pos_coeff,1) coeff,
       r.education,
       r.sex,
       r.wanted_salary
from        vacs.ias_resume_clean r
left join   vacs.ias_resume_one_position p on p.id_ias_resume_clean = r.id