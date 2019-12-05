# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class InvestProjLineType(Base):
    __tablename__ = 'invest_proj_line_type'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".invest_proj_line_type_id_seq'::regclass)"))
    name = Column(String(64), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    is_add = Column(Integer, nullable=False, server_default=text("0"))


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


class Okved(Base):
    __tablename__ = 'okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okved_id_seq'::regclass)"))
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

REFS_CLASSES = {'okz': Okz, 'okved': Okved, 'okso': Okso, 'okpdtr': Okpdtr, 'okf': Okf}

class OrganizationPoll(Base):
    __tablename__ = 'organization_poll'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_poll_id_seq'::regclass)"))
    year_for = Column(Integer, nullable=False)
    date_start = Column(Date)
    date_finish = Column(Date)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class OrganizationPollFormLineType(Base):
    __tablename__ = 'organization_poll_form_line_type'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_poll_form_line_type_id_seq'::regclass)"))
    name = Column(String(64), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class OrganizationPollFormStatu(Base):
    __tablename__ = 'organization_poll_form_status'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_poll_form_status_id_seq'::regclass)"))
    name = Column(String(64), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class ProfStandard(Base):
    __tablename__ = 'prof_standard'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_standard_id_seq'::regclass)"))
    code = Column(String(16), nullable=False, unique=True)
    name = Column(String(1024), nullable=False)
    date_accepted = Column(String(1024))
    tf_cnt = Column(Integer)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))


class Region(Base):
    __tablename__ = 'region'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".region_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    code = Column(String(16), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class TypeMrigo(Base):
    __tablename__ = 'type_mrigo'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_mrigo_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


t_vw_invest_proj_lines = Table(
    'vw_invest_proj_lines', metadata,
    Column('id_type', Integer),
    Column('id_invest_proj', Integer),
    Column('y_0', Numeric),
    Column('y_1', Numeric),
    Column('y_2', Numeric),
    Column('y_3', Numeric),
    Column('y_4', Numeric),
    Column('y_5', Numeric),
    Column('y_6', Numeric),
    Column('y_7', Numeric),
    Column('y_8', Numeric),
    Column('year_start', Float(53)),
    schema='data'
)


t_vw_invest_proj_lines_add = Table(
    'vw_invest_proj_lines_add', metadata,
    Column('id_type', Integer),
    Column('id_invest_proj', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okz', Integer),
    Column('id_okved', Integer),
    Column('y_0', Numeric),
    Column('y_1', Numeric),
    Column('y_2', Numeric),
    Column('y_3', Numeric),
    Column('y_4', Numeric),
    Column('y_5', Numeric),
    Column('y_6', Numeric),
    Column('y_7', Numeric),
    Column('y_8', Numeric),
    Column('year_start', Float(53)),
    schema='data'
)


class WorkersAgeType(Base):
    __tablename__ = 'workers_age_type'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".workers_age_type_id_seq'::regclass)"))
    name = Column(String(64), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class WorkersSexType(Base):
    __tablename__ = 'workers_sex_type'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".workers_sex_type_id_seq'::regclass)"))
    name = Column(String(64), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class WorldSkill(Base):
    __tablename__ = 'world_skills'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".world_skills_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class City(Base):
    __tablename__ = 'city'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".city_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    id_region = Column(ForeignKey('data.region.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    region = relationship('Region')


class ProfStandardOkso(Base):
    __tablename__ = 'prof_standard_okso'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_standard_okso_id_seq'::regclass)"))
    id_prof_standard = Column(ForeignKey('data.prof_standard.id'), nullable=False)
    code_okso = Column(String(16), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_standard = relationship('ProfStandard')


class ProfStandardOkved(Base):
    __tablename__ = 'prof_standard_okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_standard_okved_id_seq'::regclass)"))
    id_prof_standard = Column(ForeignKey('data.prof_standard.id'), nullable=False)
    code_okved = Column(String(16), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_standard = relationship('ProfStandard')


class ProfStandardOkz(Base):
    __tablename__ = 'prof_standard_okz'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_standard_okz_id_seq'::regclass)"))
    id_prof_standard = Column(ForeignKey('data.prof_standard.id'), nullable=False)
    code_okz = Column(String(16), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_standard = relationship('ProfStandard')


class ProfTf(Base):
    __tablename__ = 'prof_tf'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_tf_id_seq'::regclass)"))
    id_prof_standard = Column(ForeignKey('data.prof_standard.id'), nullable=False)
    level = Column(String(16), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))
    num = Column(Integer, nullable=False)

    prof_standard = relationship('ProfStandard')


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


class Organization(Base):
    __tablename__ = 'organization'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_id_seq'::regclass)"))
    inn = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    id_mrigo = Column(ForeignKey('data.city.id'), nullable=False)
    id_okfs = Column(ForeignKey('data.okfs.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    city = relationship('City')
    okf = relationship('Okf')


class ProfTfAccessReq(Base):
    __tablename__ = 'prof_tf_access_reqs'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_tf_access_reqs_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    access_req = Column(String(1024), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfEducReq(Base):
    __tablename__ = 'prof_tf_educ_reqs'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_tf_educ_reqs_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    educ_req = Column(String(1024), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfOkdptr(Base):
    __tablename__ = 'prof_tf_okdptr'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_tf_okdptr_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    code_okdptr = Column(String(32), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfOkso(Base):
    __tablename__ = 'prof_tf_okso'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_tf_okso_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    code_okso = Column(String(32), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


class ProfTfProfession(Base):
    __tablename__ = 'prof_tf_professions'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_tf_professions_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))
    prof = Column(String(1024), nullable=False)

    prof_tf = relationship('ProfTf')


class ProfTfStageReq(Base):
    __tablename__ = 'prof_tf_stage_reqs'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".prof_tf_stage_reqs_id_seq'::regclass)"))
    id_prof_tf = Column(ForeignKey('data.prof_tf.id'), nullable=False)
    stage_req = Column(String(1024), nullable=False)
    remark = Column(String(1024))
    load_date = Column(DateTime, server_default=text("now()"))

    prof_tf = relationship('ProfTf')


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

    organization = relationship('Organization')


class OrganizationOkved(Base):
    __tablename__ = 'organization_okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_okved_id_seq'::regclass)"))
    id_organization = Column(ForeignKey('data.organization.id', ondelete='CASCADE'), nullable=False)
    id_okved = Column(ForeignKey('data.okved.id', ondelete='CASCADE'), nullable=False)
    year_for = Column(Integer, nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    okved = relationship('Okved')
    organization = relationship('Organization')


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


class InvestProjLine(Base):
    __tablename__ = 'invest_proj_line'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".invest_proj_line_id_seq'::regclass)"))
    id_invest_proj = Column(ForeignKey('data.invest_proj.id', ondelete='CASCADE'), nullable=False)
    id_type = Column(ForeignKey('data.invest_proj_line_type.id'), nullable=False)
    id_okpdtr = Column(ForeignKey('data.okpdtr.id'))
    id_okz = Column(ForeignKey('data.okz.id'))
    id_okved = Column(ForeignKey('data.okved.id'))
    value = Column(Numeric(8, 2))
    year_for = Column(Integer)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    invest_proj = relationship('InvestProj')
    okpdtr = relationship('Okpdtr')
    okved = relationship('Okved')
    okz = relationship('Okz')
    invest_proj_line_type = relationship('InvestProjLineType')


class OrganizationPollFormLine(Base):
    __tablename__ = 'organization_poll_form_line'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_poll_form_line_id_seq'::regclass)"))
    id_form = Column(ForeignKey('data.organization_poll_form.id', ondelete='CASCADE'), nullable=False)
    id_type = Column(ForeignKey('data.organization_poll_form_line_type.id'), nullable=False)
    id_okpdtr = Column(ForeignKey('data.okpdtr.id'))
    id_okz = Column(ForeignKey('data.okz.id'))
    id_okved = Column(ForeignKey('data.okved.id'))
    id_okso = Column(ForeignKey('data.okso.id'))
    id_invest_proj = Column(ForeignKey('data.invest_proj.id'))
    id_workers_age_type = Column(ForeignKey('data.workers_age_type.id'))
    id_workers_sex_type = Column(ForeignKey('data.workers_age_type.id'))
    id_world_skills = Column(ForeignKey('data.world_skills.id'))
    value = Column(Numeric(8, 2))
    year_for = Column(Integer)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    organization_poll_form = relationship('OrganizationPollForm')
    invest_proj = relationship('InvestProj')
    okpdtr = relationship('Okpdtr')
    okso = relationship('Okso')
    okved = relationship('Okved')
    okz = relationship('Okz')
    organization_poll_form_line_type = relationship('OrganizationPollFormLineType')
    workers_age_type = relationship('WorkersAgeType', primaryjoin='OrganizationPollFormLine.id_workers_age_type == WorkersAgeType.id')
    workers_age_type1 = relationship('WorkersAgeType', primaryjoin='OrganizationPollFormLine.id_workers_sex_type == WorkersAgeType.id')
    world_skill = relationship('WorldSkill')
