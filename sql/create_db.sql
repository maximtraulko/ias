create database  ias;

create schema auth;

create schema polls;

create schema vacs;

create schema modeling;

create table auth.users(
  id  serial primary key,
  login varchar(64)
);


create table auth.roles(
  id serial primary key,
  name varchar(64),
  descr varchar(1024)
);

create schema data;

create table data.prof_standard(
  id serial primary key,
  code varchar(16) not null,
  name varchar(1024) not null,
  date_accepted date not null,
  tf_cnt int,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);


create table data.prof_standard_okz(
  id serial primary key,
  id_prof_standard int references data.prof_standard(id) not null,
  code_okz varchar(16) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);


create table data.prof_standard_okso(
  id serial primary key,
  id_prof_standard int references data.prof_standard(id) not null,
  code_okso varchar(16) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);

create table data.prof_standard_okved(
  id serial primary key,
  id_prof_standard int references data.prof_standard(id) not null,
  code_okved varchar(16) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);


create table data.prof_tf(
  id serial primary key,
  id_prof_standard int references data.prof_standard(id) not null,
  level varchar(16) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);


create table data.prof_tf_professions(
  id serial primary key,
  id_prof_tf int references data.prof_tf(id) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);


create table data.prof_tf_educ_reqs(
  id serial primary key,
  id_prof_tf int references data.prof_tf(id) not null,
  educ_req varchar(1024) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);

create table data.prof_tf_stage_reqs(
  id serial primary key,
  id_prof_tf int references data.prof_tf(id) not null,
  stage_req varchar(1024) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);

create table data.prof_tf_access_reqs(
  id serial primary key,
  id_prof_tf int references data.prof_tf(id) not null,
  access_req varchar(1024) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);



create table data.prof_tf_okz(
  id serial primary key,
  id_prof_tf int references data.prof_tf(id) not null,
  code_okz varchar(32) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);

create table data.prof_tf_okdptr(
  id serial primary key,
  id_prof_tf int references data.prof_tf(id) not null,
  code_okdptr varchar(32) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);


create table data.prof_tf_okso(
  id serial primary key,
  id_prof_tf int references data.prof_tf(id) not null,
  code_okso varchar(32) not null,
  remark varchar(1024),
  load_date timestamp default now() --!разобраться с текущей временной зоной
);


--#!поставить комментарии comment on

alter table data.prof_standard alter column date_accepted type varchar(1024);

alter table data.prof_standard alter column date_accepted DROP NOT NULL;

select * from data.prof_standard;

select substr(code,1,2) t,count(*) from data.prof_standard group by rollup(substr(code,1,2)) order by t;

alter table data.prof_standard add constraint prof_standard$code unique (code);

update data.prof_standard set code = rtrim(ltrim(code)) where 1 = 1;

select * from data.prof_standard_okz order by id_prof_standard;

select count(*) from data.prof_standard_okz order by id_prof_standard;

alter table data.prof_tf add num int not null;

alter table data.prof_tf_professions add prof varchar(1024) not null;

create schema app;

create table app.menu_items(
  id serial primary key,
  caption varchar(64) unique not null,
  descr varchar(512) not null,
  href varchar(64) not null
);

create table app.menu_subitems(
  id serial primary key,
  id_menu_items int references app.menu_items(id),
  caption varchar(64) unique not null,
  href varchar(64) not null
);

insert into app.menu_items(caption, descr, href) values ('Справочники', 'Редактирование и просмотр справочников', '/refs');
insert into app.menu_items(caption, descr, href) values ('Личные кабинеты', 'Личные кабинеты образовательных организаций и работодателей', '/lks');
insert into app.menu_items(caption, descr, href) values ('Моделирование', 'Ввод статистических данных и запуск моделирования', '/models');
insert into app.menu_items(caption, descr, href) values ('Распределение КЦП', 'Процедура распределения КЦП', '/cnes');
insert into app.menu_items(caption, descr, href) values ('Целевое обучение', 'Ввод и просмотр заявок на целевое обучение', '/studys');

insert into app.menu_subitems(id_menu_items, caption, href) values (1, 'ОКСО', '/refs/okso');
insert into app.menu_subitems(id_menu_items, caption, href) values (1, 'ОКВЭД', '/refs/okved');
insert into app.menu_subitems(id_menu_items, caption, href) values (1, 'ОКЗ', '/refs/okz');
insert into app.menu_subitems(id_menu_items, caption, href) values (1, 'ОКПТР', '/refs/okptr');

insert into app.menu_subitems(id_menu_items, caption, href) values (2, 'Работодатель', '/lks/work');
insert into app.menu_subitems(id_menu_items, caption, href) values (2, 'Образовательная организация', '/lks/study_org');

insert into app.menu_subitems(id_menu_items, caption, href) values (3, 'Стат. данные', '/models/stats');
insert into app.menu_subitems(id_menu_items, caption, href) values (3, 'Сценарий', '/models/scenario');

select * from organization_enrol_form_line