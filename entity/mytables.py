#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text, Text, TIMESTAMP, Float, JSON, Date, Numeric, Table
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

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"vacs\".ias_resume_one_position_id_seq'::regclass)"))
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

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".invest_proj_okved_id_seq'::regclass)"))
    id_invest_proj = Column(ForeignKey('data.invest_proj.id', ondelete='CASCADE'), nullable=False)
    id_okved = Column(ForeignKey('data.okved.id', ondelete='CASCADE'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    invest_proj = relationship('InvestProj')
    okved = relationship('Okved')


class OrganizationPollForm(Base):
    __tablename__ = 'organization_poll_form'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_poll_form_id_seq'::regclass)"))
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

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_poll_id_seq'::regclass)"))
    year_for = Column(Integer, nullable=False)
    date_start = Column(Date)
    date_finish = Column(Date)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class OrganizationPollFormStatu(Base):
    __tablename__ = 'organization_poll_form_status'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_poll_form_status_id_seq'::regclass)"))
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
    id_organization_poll = Column(Integer,primary_key=True)
    id_organization = Column(Integer)
    dateadd = Column(DateTime)
    organization_name = Column(String(1024))
    year_for = Column(Integer)
    id_mrigo = Column(Integer)
    mrigo_name = Column(String(1024))


ENTITY = {'invest_proj': InvestProj}
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
                                      'sort': InvestProjOkved.id_okved}
                }


REFS_CLASSES = {'okz': Okz, 'okved': VwOkved, 'okso': Okso, 'okpdtr': Okpdtr, 'okf': Okf, 'organizations': Organization,
                'mrigo': Mrigo}


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')






