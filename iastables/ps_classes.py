# coding: utf-8
from typing import Type

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text, Text, TIMESTAMP, Float, JSON, Date, Numeric, Table
from sqlalchemy.orm import relationship, exc
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from iastables import db_config
import logging
import datetime
import decimal

Base = declarative_base()
metadata = Base.metadata


class ProfStandard(Base):
    __tablename__ = 'prof_standard'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_standard_id_seq'::regclass)"))
    code = Column(String(16), nullable=False, unique=True)
    name = Column(String(1024), nullable=False)
    date_accepted = Column(String(1024))
    tf_cnt = Column(Integer)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))


class ProfStandardOkso(Base):
    __tablename__ = 'prof_standard_okso'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_standard_okso_id_seq'::regclass)"))
    id_prof_standard = Column(ForeignKey('data.prof_standard.id'), nullable=False)
    code_okso = Column(String(16), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_standard = relationship('ProfStandard')


class ProfStandardOkved(Base):
    __tablename__ = 'prof_standard_okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_standard_okved_id_seq'::regclass)"))
    id_prof_standard = Column(ForeignKey('data.prof_standard.id'), nullable=False)
    code_okved = Column(String(16), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_standard = relationship('ProfStandard')


class ProfStandardOkz(Base):
    __tablename__ = 'prof_standard_okz'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_standard_okz_id_seq'::regclass)"))
    id_prof_standard = Column(ForeignKey('data.prof_standard.id'), nullable=False)
    code_okz = Column(String(16), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_standard = relationship('ProfStandard')


class ProfTf(Base):
    __tablename__ = 'prof_tf'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_tf_id_seq'::regclass)"))
    id_prof_standard = Column(ForeignKey('data.prof_standard.id'), nullable=False)
    level = Column(String(16), nullable=False)
    num = Column(Integer, nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_standard = relationship('ProfStandard')


class ProfTfAccessReq(Base):
    __tablename__ = 'prof_tf_access_reqs'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_tf_access_reqs_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    access_req = Column(String(1024), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfEducReq(Base):
    __tablename__ = 'prof_tf_educ_reqs'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_tf_educ_reqs_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    educ_req = Column(String(1024), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfOkdptr(Base):
    __tablename__ = 'prof_tf_okdptr'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_tf_okdptr_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    code_okdptr = Column(String(32), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfOkso(Base):
    __tablename__ = 'prof_tf_okso'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_tf_okso_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    code_okso = Column(String(32), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfProfession(Base):
    __tablename__ = 'prof_tf_professions'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_tf_professions_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    prof = Column(String(1024), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfStageReq(Base):
    __tablename__ = 'prof_tf_stage_reqs'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.prof_tf_stage_reqs_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    stage_req = Column(String(1024), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


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


class MenuItem(Base):
    __tablename__ = 'menu_items'
    __table_args__ = {'schema': 'app'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('app.menu_items_id_seq'::regclass)"))
    caption = Column(String(64), nullable=False, unique=True)
    descr = Column(String(512), nullable=False)
    href = Column(String(64), nullable=False)


class MenuSubitem(Base):
    __tablename__ = 'menu_subitems'
    __table_args__ = {'schema': 'app'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('app.menu_subitems_id_seq'::regclass)"))
    id_menu_items = Column(ForeignKey('app.menu_items.id'))
    caption = Column(String(64), nullable=False, unique=True)
    href = Column(String(64), nullable=False)

    menu_item = relationship('MenuItem')


class Okved(Base):
    __tablename__ = 'okved'
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


class UtlJsonDatum(Base):
    __tablename__ = 'utl$json_data'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".\"utl$json_data_id_seq\"'::regclass)"))
    entity_name = Column(String(256))
    jsdata = Column(Text)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


ENTITY_CLASSES = {'invest_proj': InvestProj}
ENTITY_LINES_CLASSES = {'invest_proj_line': VwInvestProjLines,
                        'invest_proj_line_add': VwInvestProjLinesAdd,
                        'invest_proj_years': VwInvestProjYears,
                        'invest_proj_okved': InvestProjOkved
                        }
ENTITY_LINES_ID = {'invest_proj_line': VwInvestProjLines.id_invest_proj,
                   'invest_proj_line_add': VwInvestProjLinesAdd.id_invest_proj,
                   'invest_proj_years': VwInvestProjYears.id_invest_proj,
                   'invest_proj_okved': InvestProjOkved.id_invest_proj
                   }

ENTITY_LINE_IDID = {'invest_proj_line': VwInvestProjLines.id_type,
                  'invest_proj_line_add': VwInvestProjLinesAdd.id_okpdtr,
                  'invest_proj_years': VwInvestProjYears.id_invest_proj,
                  'invest_proj_okved': InvestProjOkved.id_okved
                  }

ENTITY_LINES_SORT = {'invest_proj_line': VwInvestProjLines.id_type,
                     'invest_proj_line_add': VwInvestProjLinesAdd.id_okpdtr,
                     'invest_proj_years': VwInvestProjYears.id_invest_proj,
                     'invest_proj_okved': InvestProjOkved.id_okved
                   }
REFS_CLASSES = {'okz': Okz, 'okved': Okved, 'okso': Okso, 'okpdtr': Okpdtr, 'okf': Okf, 'organizations': Organization,
                'mrigo': Mrigo}


def get_ps_standart(sess, vcode):
    """
    возврат объекта проф. стандарта, если такого нет, то возвращается новый
    :param sess: сеанс
    :param vcode: код стандарта
    :return: объект, либо полный, либо только с code
    """
    try:
        res = sess.query(ProfStandard).filter(ProfStandard.code == vcode).one()
    except exc.NoResultFound:
        res = ProfStandard(code=vcode)
    return res


def get_ps_okz(sess, ps, vcode):
    """
    возврат ОКЗ для проф. стандарта, если такого нет, то возвращается новый
    :param sess: сеанс
    :param ps: проф. стандарт
    :param vcode: код ОКЗ
    :return: объект, либо полный, либо только с code
    """
    try:
        res = sess.query(ProfStandardOkz).filter(ProfStandardOkz.prof_standard == ps,
                                                 ProfStandardOkz.code_okz == str(vcode)).one()
    except exc.NoResultFound:
        res = ProfStandardOkz(prof_standard=ps, code_okz=str(vcode))
    return res


def get_ps_okved(sess, ps, vcode):
    """
    возврат ОКВЭД проф. стандарта, если такого нет, то возвращается новый
    :param sess: сеанс
    :param ps: проф. стандарт
    :param vcode: код ОКВЭД
    :return: объект, либо полный, либо только с code
    """
    try:
        res = sess.query(ProfStandardOkved).filter(ProfStandardOkved.prof_standard == ps,
                                                   ProfStandardOkved.code_okved == str(vcode)).one()
    except exc.NoResultFound:
        res = ProfStandardOkved(prof_standard=ps, code_okved=str(vcode))
    return res


def get_ps_okso(sess, ps, vcode):
    """
    возврат ОКСО проф. стандарта, если такого нет, то возвращается новый
    :param sess: сеанс
    :param ps: проф. стандарт
    :param vcode: код ОКСО
    :return: объект, либо полный, либо только с code
    """
    try:
        res = sess.query(ProfStandardOkso).filter(ProfStandardOkso.prof_standard == ps,
                                                  ProfStandardOkso.code_okso == str(vcode)).one()
    except exc.NoResultFound:
        res = ProfStandardOkso(prof_standard=ps, code_okso=str(vcode))
    return res


def get_ps_tf(sess, ps, vnum, lev):
    """
    возврат ОКСО проф. стандарта, если такого нет, то возвращается новый
    :param sess: сеанс
    :param ps: проф. стандарт
    :param vnum: номер
    :param lev: уровень
    :return: объект, либо полный, либо только с num
    """
    tclass = ProfTf
    try:
        res = sess.query(tclass).filter(tclass.prof_standard == ps,
                                        tclass.num == vnum).one()
    except exc.NoResultFound:
        res = tclass(prof_standard=ps, num=vnum)
    res.level = lev
    return res


def get_ps_tf_prof(sess, ps_tf, vprof):
    """

    :param sess:
    :param ps_tf:
    :param vprof:
    :return:
    """
    tclass = ProfTfProfession
    try:
        res = sess.query(tclass).filter(tclass.prof_tf == ps_tf,
                                        tclass.prof == vprof).one()
    except exc.NoResultFound:
        res = tclass(prof_tf=ps_tf, prof=vprof)
    return res


def get_ps_tf_stage(sess, ps_tf, stage):
    """

    :param sess:
    :param ps_tf:
    :param stage:
    :return:
    """
    tclass = ProfTfStageReq
    try:
        res = sess.query(tclass).filter(tclass.prof_tf == ps_tf,
                                        tclass.stage_req == stage).one()
    except exc.NoResultFound:
        res = tclass(prof_tf=ps_tf, stage_req=stage)
    return res


def get_ps_tf_okso(sess, ps_tf, okso):
    """

    :param sess:
    :param ps_tf:
    :param okso:
    :return:
    """
    tclass = ProfTfOkso
    try:
        res = sess.query(tclass).filter(tclass.prof_tf == ps_tf,
                                        tclass.code_okso == str(okso)).one()
    except exc.NoResultFound:
        res = tclass(prof_tf=ps_tf, code_okso=str(okso))
    return res


def get_ps_educ_reqs(sess, ps_tf, educ):
    """

    :param sess:
    :param ps_tf:
    :param educ:
    :return:
    """
    tclass = ProfTfEducReq
    try:
        res = sess.query(tclass).filter(tclass.prof_tf == ps_tf,
                                        tclass.educ_req == educ).one()
    except exc.NoResultFound:
        res = tclass(prof_tf=ps_tf, educ_req=educ)
    return res


def get_ps_okdptr(sess, ps_tf, okdptr):
    """

    :param sess:
    :param ps_tf:
    :param okdptr:
    :return:
    """
    tclass = ProfTfOkdptr
    try:
        res = sess.query(tclass).filter(tclass.prof_tf == ps_tf,
                                        tclass.code_okdptr == str(okdptr)).one()
    except exc.NoResultFound:
        res = tclass(prof_tf=ps_tf, code_okdptr=str(okdptr))
    return res


def get_ps_access_reqs(sess, ps_tf, access):
    """
    :param sess:
    :param ps_tf:
    :param access:
    :return:
    """
    tclass = ProfTfAccessReq
    try:
        res = sess.query(tclass).filter(tclass.prof_tf == ps_tf,
                                        tclass.access_req == str(access)).one()
    except exc.NoResultFound:
        res = tclass(prof_tf=ps_tf, access_req=str(access))
    return res


def get_refs_data(_sess, ref_name):
    """возврат данных справочников"""
    tclass = REFS_CLASSES[ref_name.lower()]
    _res = _sess.query(tclass).all()
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def get_entity_data(_sess, entity_name, entity_id):
    """возврат данных сущности"""
    tclass = ENTITY_CLASSES[entity_name.lower()]
    _res = None
    if entity_id > 0:
        _res = _sess.query(tclass).get(entity_id)
    else:
        _res = _sess.query(tclass).all()
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def get_entity_lines_data(_sess, lines_name, entity_id):
    """возврат данных сущности"""
    tclass = ENTITY_LINES_CLASSES[lines_name.lower()]
    tid = ENTITY_LINES_ID[lines_name.lower()]
    sort_col = ENTITY_LINES_SORT[lines_name.lower()]
    _res = _sess.query(tclass).\
        filter(tid == entity_id).order_by(sort_col).all()
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def get_organization_poll(_sess, year_for, id_mrigo):
    _res = _sess.query(VWOrganizationPollForm).\
        filter(VWOrganizationPollForm.year_for == year_for and VWOrganizationPollForm.id_mrigo == id_mrigo).all()
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def json2attrs(_tclass, _data):
    """преобразуем json в словарь и убираем лишнее"""
    r = json.loads(_data)
    logging.debug(type(r))
    _res = []
    if type(r) == list:
        for item in r:
            tr = {i: item[i] for i in item if i in _tclass.__dict__}
            _res.append(tr)
    if type(r) == dict:
        tr = {i: r[i] for i in r if i in _tclass.__dict__}
        _res.append(tr)
    return _res


def set_entity_data(_sess, _entity_name, _entity_id, _data):
    """редактирование данных сущности"""
    tclass = ENTITY_CLASSES[_entity_name.lower()]
    tr = json2attrs(tclass, _data)
    _sess.query(tclass).filter(tclass.id == _entity_id).update(tr[0])
    _sess.commit()
    return "{'result':'ok'}"


def set_entity_lines_data(_sess, _lines_name, _entity_id, _data):
    """редактирование данных строк сущности"""
    tclass = ENTITY_LINES_CLASSES[_lines_name.lower()]
    _tid = ENTITY_LINE_IDID[_lines_name.lower()]
    trls = json2attrs(tclass, _data)
    _tid_name = str(_tid).split('.')[1]
    for tr in trls:
        _id = tr[_tid_name]
        cnt = _sess.query(tclass).filter(_tid == _id).count()
        # если есть такая строка
        has_string = cnt > 0
        _res = None
        if has_string:
            _sess.query(tclass).filter(_tid == _id).update(tr)
            _res = 'updated'
        else:
            obj = tclass(**tr)
            _sess.add(obj)
            _res = 'inserted'
        _sess.commit()
    return _res


def get_session():
    """
    Возврат сессии
    """
    _sess = sessionmaker(bind=create_engine('postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        db_config.USER, db_config.PASSWORD, db_config.HOST, db_config.PORT, db_config.DB)))()
    return _sess


def new_alchemy_encoder(revisit_self=False, fields_to_expand=[]):
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if revisit_self:
                    if obj in _visited_objs:
                        return None
                    _visited_objs.append(obj)

                # go through each field in this SQLalchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and x != 'dateadd']:
                    val = obj.__getattribute__(field)
                    if type(val) == datetime.date:
                        val = str(val)
                    if type(val) == decimal.Decimal:
                        val = int(val)
                    # is this field another SQLalchemy object, or a list of SQLalchemy objects?
                    if isinstance(val.__class__, DeclarativeMeta) or (isinstance(val, list) and len(val) > 0 and isinstance(val[0].__class__, DeclarativeMeta)):
                        # unless we're expanding this field, stop here
                        if field not in fields_to_expand:
                            # not expanding this field: set it to None and continue
                            fields[field] = None
                            continue

                    fields[field] = val
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    sess = get_session()
    #res = set_entity_lines_data(sess, 'invest_proj_line', 1, '[{"id_type":1, "y_0":100}, {"id_type":2, "y_0":200}]')
    res = set_entity_data(sess, 'invest_proj', 1, '{"name":"Тестовый проект","id_organization":1,"invest_sum":"400001","date_start":"2019-11-01","date_finish":"2024-12-31"}')
    logging.debug(res)





