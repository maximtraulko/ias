#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text, Text, TIMESTAMP, Float, JSON, Date, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import logging


Base = declarative_base()
metadata = Base.metadata


class IasResumeClean(Base):
    __tablename__ = 'ias_resume_clean'
    __table_args__ = {'schema': 'vacs'}

    id = Column(Integer, primary_key=True)
    id_external = Column(Integer, nullable=False)
    title = Column(Text)
    qualities = Column(Text)
    education = Column(Text)
    skills = Column(JSON, comment='(DC2Type:json_array)')
    published_at = Column(TIMESTAMP, server_default=text("NULL::timestamp without time zone"))
    updated_at = Column(TIMESTAMP, nullable=False)
    birthday = Column(TIMESTAMP, server_default=text("NULL::timestamp without time zone"))
    fio = Column(String(255), server_default=text("NULL::character varying"))
    sex = Column(String(255), server_default=text("NULL::character varying"))
    wanted_salary = Column(String(255), server_default=text("NULL::character varying"))


class IasResumeOnePosition(Base):
    __tablename__ = 'ias_resume_one_position'
    __table_args__ = {'schema': 'vacs'}

    id = Column(Integer, primary_key=True,
                server_default=text("nextval('\"vacs\".ias_resume_one_position_id_seq'::regclass)"))
    id_ias_resume_clean = Column(ForeignKey('vacs.ias_resume_clean.id'))
    pos_name = Column(String(512), nullable=False)
    pos_coeff = Column(Float(53), nullable=False)

    ias_resume_clean = relationship('IasResumeClean')


class Okved(Base):
    __tablename__ = 'okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okved_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class VwOkved(Base):
    __tablename__ = 'vw_okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okved_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class Okf(Base):
    __tablename__ = 'okfs'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okfs_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class Okpdtr(Base):
    __tablename__ = 'okpdtr'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okpdtr_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class Okso(Base):
    __tablename__ = 'okso'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okso_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class Okz(Base):
    __tablename__ = 'okz'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okz_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class Organization(Base):
    __tablename__ = 'organization'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_id_seq'::regclass)"))
    inn = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    id_mrigo = Column(ForeignKey('data.mrigo.id'), nullable=False)
    id_okfs = Column(ForeignKey('data.okfs.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    is_educ = Column(Integer)
    is_worker = Column(Integer)


class TypeMrigo(Base):
    __tablename__ = 'type_mrigo'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_mrigo_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class Mrigo(Base):
    __tablename__ = 'mrigo'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".mrigo_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    id_region = Column(ForeignKey('data.region.id'), nullable=False)
    id_city = Column(ForeignKey('data.city.id'))
    id_type_mrigo = Column(ForeignKey('data.type_mrigo.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    city = relationship('City')
    region = relationship('Region')
    type_mrigo = relationship('TypeMrigo')


class City(Base):
    __tablename__ = 'city'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".city_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    id_region = Column(ForeignKey('data.region.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    region = relationship('Region')


class Region(Base):
    __tablename__ = 'region'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".region_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    code = Column(String(16), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class InvestProj(Base):
    __tablename__ = 'invest_proj'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".invest_proj_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    id_organization = Column(ForeignKey('data.organization.id'), nullable=False)
    date_start = Column(Date)
    date_finish = Column(Date)
    invest_sum = Column(Numeric(12, 2))
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class InvestProjOkved(Base):
    __tablename__ = 'invest_proj_okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True,
                server_default=text("nextval('\"data\".invest_proj_okved_id_seq'::regclass)"))
    id_invest_proj = Column(ForeignKey('data.invest_proj.id', ondelete='CASCADE'), nullable=False)
    id_okved = Column(ForeignKey('data.okved.id', ondelete='CASCADE'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    invest_proj = relationship('InvestProj')
    okved = relationship('Okved')


class OrganizationPollForm(Base):
    __tablename__ = 'organization_poll_form'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True,
                server_default=text("nextval('\"data\".organization_poll_form_id_seq'::regclass)"))
    id_organization = Column(ForeignKey('data.organization.id', ondelete='CASCADE'), nullable=False)
    id_poll = Column(ForeignKey('data.organization_poll.id'), nullable=False)
    id_status = Column(ForeignKey('data.organization_poll_form_status.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    organization = relationship('Organization')
    organization_poll = relationship('OrganizationPoll')
    organization_poll_form_statu = relationship('OrganizationPollFormStatu')


class OrganizationPoll(Base):
    __tablename__ = 'organization_poll'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True,
                server_default=text("nextval('\"data\".organization_poll_id_seq'::regclass)"))
    year_for = Column(Integer, nullable=False)
    date_start = Column(Date)
    date_finish = Column(Date)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class OrganizationPollFormStatu(Base):
    __tablename__ = 'organization_poll_form_status'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True,
                server_default=text("nextval('\"data\".organization_poll_form_status_id_seq'::regclass)"))
    name = Column(String(64), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class VwInvestProjLines(Base):
    __tablename__ = 'vw_invest_proj_lines'
    __table_args__ = {'schema': 'data'}
    id_type = Column(Integer,  primary_key=True)
    id_invest_proj = Column(Integer)
    y_0 = Column(Numeric)
    y_1 = Column(Numeric)
    y_2 = Column(Numeric)
    y_3 = Column(Numeric)
    y_4 = Column(Numeric)
    y_5 = Column(Numeric)
    y_6 = Column(Numeric)
    y_7 = Column(Numeric)
    y_8 = Column(Numeric)
    year_start = Column(Integer)
    type_name = Column(String(1024))


class VwInvestProjLinesAdd(Base):
    __tablename__ = 'vw_invest_proj_lines_add'
    __table_args__ = {'schema': 'data'}
    id_type = Column(Integer)
    id_invest_proj = Column(Integer)
    id_okpdtr = Column(Integer,  primary_key=True)
    id_okz = Column(Integer)
    id_okved = Column(Integer)
    y_0 = Column(Numeric)
    y_1 = Column(Numeric)
    y_2 = Column(Numeric)
    y_3 = Column(Numeric)
    y_4 = Column(Numeric)
    y_5 = Column(Numeric)
    y_6 = Column(Numeric)
    y_7 = Column(Numeric)
    y_8 = Column(Numeric)
    year_start = Column(Integer)
    okz_code = Column(String(512))
    okz_name = Column(String(512))
    okved_code = Column(String(512))
    okved_name = Column(String(512))
    okpdtr_code = Column(String(512))
    okpdtr_name = Column(String(512))


class VwInvestProjYears(Base):
    __tablename__ = 'vw_invest_proj_years'
    __table_args__ = {'schema': 'data'}
    id_invest_proj = Column(Integer,  primary_key=True)
    y_0 = Column(Integer)
    y_1 = Column(Integer)
    y_2 = Column(Integer)
    y_3 = Column(Integer)
    y_4 = Column(Integer)
    y_5 = Column(Integer)
    y_6 = Column(Integer)
    y_7 = Column(Integer)
    y_8 = Column(Integer)


class VWOrganizationPollForm(Base):
    __tablename__ = 'vw_organization_poll_form'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer, primary_key=True)
    id_organization = Column(Integer)
    dateadd = Column(DateTime)
    organization_name = Column(String(1024))
    year_for = Column(Integer)
    id_mrigo = Column(Integer)
    mrigo_name = Column(String(1024))
    id_okfs = Column(Integer)
    okfs_name = Column(String(1024))
    cnt = Column(Integer)
    salary = Column(Numeric)


class WorkersAgeType(Base):
    __tablename__ = 'workers_age_type'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".workers_age_type_id_seq'::regclass)"))
    name = Column(String(64), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    ord_num = Column(Integer, nullable=False)


class WorkersSexType(Base):
    __tablename__ = 'workers_sex_type'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".workers_sex_type_id_seq'::regclass)"))
    name = Column(String(64), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    ord_num = Column(Integer, nullable=False)


class WorldSkill(Base):
    __tablename__ = 'world_skills'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".world_skills_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class VwOksoWork(Base):
    __tablename__ = 'vw_okso_work'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True)
    code = Column(Text)
    name = Column(String(1024))


class VwOrganizationFormAgeLines(Base):
    __tablename__ = 'vw_organization_form_age_lines'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer)
    id_type = Column(Integer)
    id_workers_age_type = Column(Integer, primary_key=True)
    age = Column(String(64))
    value = Column(Integer)


class VwOrganizationFormEducLines(Base):
    __tablename__ = 'vw_organization_form_educ_lines'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer)
    id_type = Column(Integer)
    id_okved = Column(Integer)
    id_okpdtr = Column(Integer, primary_key=True)
    id_okso = Column(Integer)
    id_educ_program_type = Column(Integer)
    y_0 = Column(Integer)
    y_1 = Column(Integer)
    y_2 = Column(Integer)
    okved_code = Column(String(16))
    okved_name = Column(String(1024))
    okso_code = Column(Text)
    okso_name = Column(String(1024))
    educ_program = Column(String(32))


class VwOrganizationFormInvestReqLines(Base):
    __tablename__ = 'vw_organization_form_invest_req_lines'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer)
    id_type = Column(Integer)
    id_okpdtr = Column(Integer, primary_key=True)
    id_okz = Column(Integer)
    id_okved = Column(Integer)
    id_invest_proj = Column(Integer)
    y_0 = Column(Integer)
    y_1 = Column(Integer)
    y_2 = Column(Integer)
    y_3 = Column(Integer)
    y_4 = Column(Integer)
    y_5 = Column(Integer)
    okpdtr_code = Column(String(16))
    okpdtr_name = Column(String(1024))
    okz_code = Column(String(16))
    okz_name = Column(String(1024))
    okved_code = Column(String(16))
    okved_name = Column(String(1024))


class VwOrganizationFormPksLines(Base):
    __tablename__ = 'vw_organization_form_pks_lines'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer)
    id_type = Column(Integer)
    id_okpdtr = Column(Integer, primary_key=True)
    id_okz = Column(Integer)
    value = Column(Integer)
    value2 = Column(Numeric(10))
    okpdtr_code = Column(String(16))
    okpdtr_name = Column(String(1024))
    okz_code = Column(String(16))
    okz_name = Column(String(1024))


class VwOrganizationFormReqLines(Base):
    __tablename__ = 'vw_organization_form_req_lines'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer)
    id_type = Column(Integer)
    id_okpdtr = Column(Integer, primary_key=True)
    id_okz = Column(Integer)
    id_okved = Column(Integer)
    y_0 = Column(Integer)
    y_1 = Column(Integer)
    y_2 = Column(Integer)
    y_3 = Column(Integer)
    y_4 = Column(Integer)
    y_5 = Column(Integer)


class VwOrganizationFormWSLines(Base):
    __tablename__ = 'vw_organization_form_ws_lines'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer)
    id_type = Column(Integer)
    id_okved = Column(Integer)
    id_okpdtr = Column(Integer, primary_key=True)
    id_world_skills = Column(Integer)
    id_educ_program_type = Column(Integer)
    y_0 = Column(Integer)
    y_1 = Column(Integer)
    y_2 = Column(Integer)
    okved_code = Column(String(16))
    okved_name = Column(String(1024))
    ws_code = Column(String(16))
    ws_name = Column(String(1024))
    educ_program = Column(String(32))


class VwOrganizationFormYears(Base):
    __tablename__ = 'vw_organization_form_years'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer, primary_key=True)
    y_0 = Column(Integer)
    y_1 = Column(Integer)
    y_2 = Column(Integer)
    y_3 = Column(Integer)
    y_4 = Column(Integer)
    y_5 = Column(Integer)


class OrganizationOkved(Base):
    __tablename__ = 'organization_okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_okved_id_seq'::regclass)"))
    id_organization = Column(ForeignKey('data.organization.id', ondelete='CASCADE'), nullable=False)
    id_okved = Column(ForeignKey('data.okved.id', ondelete='CASCADE'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    okved = relationship('Okved')
    organization = relationship('Organization')


class VwOrganizationFormSexLines(Base):
    __tablename__ = 'vw_organization_form_sex_lines'
    __table_args__ = {'schema': 'data'}
    id_form = Column(Integer)
    id_type = Column(Integer)
    id_workers_sex_type = Column(Integer, primary_key=True)
    sex_type = Column(String(64))
    value = Column(Integer)


class VwEducProgramType(Base):
    __tablename__ = 'vw_educ_program_type'
    __table_args__ = {'schema': 'data'}
    id = Column(Integer, primary_key=True)
    name = Column(String(32))


class VwEducProgramTypeWS(Base):
    __tablename__ = 'vw_educ_program_type_ws'
    __table_args__ = {'schema': 'data'}
    id = Column(Integer, primary_key=True)
    name = Column(String(32))


class Okopf(Base):
    __tablename__ = 'okopf'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okopf_id_seq'::regclass)"))
    code = Column(String(32), nullable=False, unique=True)
    name = Column(String(1024), nullable=False, unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))


class TypeTargetOrg(Base):
    __tablename__ = 'type_target_org'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_target_org_id_seq'::regclass)"))
    name = Column(String(32), nullable=False, unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))


class TargetStudyRequestStatu(Base):
    __tablename__ = 'target_study_request_status'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".target_study_request_status_id_seq'::regclass)"))
    name = Column(String(64), unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))


class TypeOrganizationActivity(Base):
    __tablename__ = 'type_organization_activity'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_organization_activity_id_seq'::regclass)"))
    name = Column(String(64), unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))


class TargetStudyRequest(Base):
    __tablename__ = 'target_study_request'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".target_study_request_id_seq'::regclass)"))
    id_organization = Column(ForeignKey('data.organization.id'), nullable=False)
    id_type_target_org = Column(ForeignKey('data.type_target_org.id'), nullable=False)
    id_okopf_customer = Column(ForeignKey('data.okopf.id'))
    id_type_activity_customer = Column(ForeignKey('data.type_organization_activity.id'))
    id_okopf_employer = Column(ForeignKey('data.okopf.id'))
    id_type_activity_employer = Column(ForeignKey('data.type_organization_activity.id'))
    id_region = Column(ForeignKey('data.region.id'))
    id_mrigo = Column(ForeignKey('data.mrigo.id'))
    id_educ_organization = Column(ForeignKey('data.organization.id'))
    id_okso = Column(ForeignKey('data.okso.id'))
    work_duration = Column(String(128))
    job_name = Column(String(512))
    job_descr = Column(String(512))
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    salary_comment = Column(String(512))
    additional_info = Column(String(4000))
    support_info = Column(String(4000))
    practice_info = Column(String(4000))
    job_garanty = Column(String(4000))
    email = Column(String(32))
    phone = Column(String(32))
    id_target_study_request_status = Column(ForeignKey('data.target_study_request_status.id'), server_default=text("1"))
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))

    organization_educ = relationship('Organization', primaryjoin='TargetStudyRequest.id_educ_organization == Organization.id')
    mrigo = relationship('Mrigo')
    okopf = relationship('Okopf', primaryjoin='TargetStudyRequest.id_okopf_customer == Okopf.id')
    okopf1 = relationship('Okopf', primaryjoin='TargetStudyRequest.id_okopf_employer == Okopf.id')
    okso = relationship('Okso')
    organization = relationship('Organization', primaryjoin='TargetStudyRequest.id_organization == Organization.id')
    region = relationship('Region')
    target_study_request_statu = relationship('TargetStudyRequestStatu')
    type_organization_activity = relationship('TypeOrganizationActivity', primaryjoin='TargetStudyRequest.id_type_activity_customer == TypeOrganizationActivity.id')
    type_organization_activity1 = relationship('TypeOrganizationActivity', primaryjoin='TargetStudyRequest.id_type_activity_employer == TypeOrganizationActivity.id')
    type_target_org = relationship('TypeTargetOrg')


class VwOksoVO(Base):
    __tablename__ = 'vw_okso_vo'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True)
    code = Column(Text)
    name = Column(String(1024))


class VwOrganizationVO(Base):
    __tablename__ = 'vw_organization_vo'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True)
    name = Column(String(1024))


ENTITY = {'invest_proj': InvestProj, 'organization_form': VWOrganizationPollForm,
          'target_study_request': TargetStudyRequest}
ENTITY_ID = {'invest_proj': InvestProj.id, 'organization_form': VWOrganizationPollForm.id_form}
ENTITY_LINES = {'invest_proj_line': {'class': VwInvestProjLines,
                                     'parent_id': VwInvestProjLines.id_invest_proj,
                                     'id': VwInvestProjLines.id_type,
                                     'sort': VwInvestProjLines.id_type},
                'invest_proj_line_add': {'class': VwInvestProjLinesAdd,
                                         'parent_id': VwInvestProjLinesAdd.id_invest_proj,
                                         'id': VwInvestProjLinesAdd.id_okpdtr,
                                         'sort': VwInvestProjLinesAdd.id_okpdtr},
                'invest_proj_years': {'class': VwInvestProjYears,
                                      'parent_id': VwInvestProjYears.id_invest_proj,
                                      'id': VwInvestProjYears.id_invest_proj,
                                      'sort': VwInvestProjYears.id_invest_proj},
                'invest_proj_okved': {'class': InvestProjOkved,
                                      'parent_id': InvestProjOkved.id_invest_proj,
                                      'id': InvestProjOkved.id_okved,
                                      'sort': InvestProjOkved.id_okved},
                'organization_okved': {'class': OrganizationOkved,
                                       'parent_id': OrganizationOkved.id_organization,
                                       'id': OrganizationOkved.id_okved,
                                       'sort': OrganizationOkved.id_okved
                                       },
                'organization_form_req_lines': {'class': VwOrganizationFormReqLines,
                                                'parent_id': VwOrganizationFormReqLines.id_form,
                                                'id': VwOrganizationFormReqLines.id_okpdtr,
                                                'sort': VwOrganizationFormReqLines.id_okpdtr},
                'organization_form_years': {'class': VwOrganizationFormYears,
                                            'parent_id': VwOrganizationFormYears.id_form,
                                            'id': VwOrganizationFormYears.id_form,
                                            'sort': VwOrganizationFormYears.id_form},
                'organization_form_invest_req_lines': {'class': VwOrganizationFormInvestReqLines,
                                                       'parent_id': VwOrganizationFormInvestReqLines.id_form,
                                                       'id': VwOrganizationFormInvestReqLines.id_okpdtr,
                                                       'sort': VwOrganizationFormInvestReqLines.id_okpdtr
                                                       },
                'organization_form_pks_lines': {'class': VwOrganizationFormPksLines,
                                                'parent_id': VwOrganizationFormPksLines.id_form,
                                                'id': VwOrganizationFormPksLines.id_okpdtr,
                                                'sort': VwOrganizationFormPksLines.id_okpdtr},
                'organization_form_age_lines': {'class': VwOrganizationFormAgeLines,
                                                'parent_id': VwOrganizationFormAgeLines.id_form,
                                                'id': VwOrganizationFormAgeLines.id_workers_age_type,
                                                'sort': VwOrganizationFormAgeLines.id_workers_age_type},
                'organization_form_sex_lines': {'class': VwOrganizationFormSexLines,
                                                'parent_id': VwOrganizationFormSexLines.id_form,
                                                'id': VwOrganizationFormSexLines.id_workers_sex_type,
                                                'sort': VwOrganizationFormSexLines.id_workers_sex_type},
                'organization_form_educ_lines': {'class': VwOrganizationFormEducLines,
                                                 'parent_id': VwOrganizationFormEducLines.id_form,
                                                 'id': VwOrganizationFormEducLines.id_okved,
                                                 'sort': VwOrganizationFormEducLines.id_okved},
                'organization_form_ws_lines': {'class': VwOrganizationFormWSLines,
                                               'parent_id': VwOrganizationFormWSLines.id_form,
                                               'id': VwOrganizationFormWSLines.id_okved,
                                               'sort': VwOrganizationFormWSLines.id_okved}
                }


REFS_CLASSES = {'okz': Okz, 'okved': VwOkved, 'okso': Okso, 'okpdtr': Okpdtr, 'okf': Okf, 'organizations': Organization,
                'mrigo': Mrigo, 'invest_proj': InvestProj, 'world_skills': WorldSkill, 'okso_work': VwOksoWork,
                'worker_age_type': WorkersAgeType, 'worker_sex_type': WorkersSexType,
                'educ_program_type': VwEducProgramType, 'educ_program_type_ws': VwEducProgramTypeWS, 'okopf': Okopf,
                'type_target_org': TypeTargetOrg, 'type_study_request_status': TargetStudyRequestStatu,
                'type_org_activity': TypeOrganizationActivity, 'vw_okso_vo': VwOksoVO,
                'vw_organization_vo': VwOrganizationVO}


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
