# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class EducProgramType(Base):
    __tablename__ = 'educ_program_type'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".educ_program_type_id_seq'::regclass)"))
    name = Column(String(32), nullable=False, unique=True)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    not_ws = Column(Integer, nullable=False, server_default=text("0"))


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
    code_okz = Column(String(16))


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
    cnt_groups = Column(Integer, server_default=text("0"))


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
    name = Column(String(512), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    ord_num = Column(Integer, nullable=False)


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


class TypeEducForm(Base):
    __tablename__ = 'type_educ_form'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_educ_form_id_seq'::regclass)"))
    name = Column(String(128), nullable=False, unique=True)
    short_name = Column(String(5), nullable=False, unique=True)
    datedadd = Column(DateTime, nullable=False, server_default=text("now()"))


class TypeMrigo(Base):
    __tablename__ = 'type_mrigo'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_mrigo_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class UtlJsonDatum(Base):
    __tablename__ = 'utl$json_data'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".\"utl$json_data_id_seq\"'::regclass)"))
    entity_name = Column(String(256))
    jsdata = Column(Text)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


t_vw_educ_program_type = Table(
    'vw_educ_program_type', metadata,
    Column('id', Integer),
    Column('name', String(32)),
    schema='data'
)


t_vw_educ_program_type_ws = Table(
    'vw_educ_program_type_ws', metadata,
    Column('id', Integer),
    Column('name', String(32)),
    schema='data'
)


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
    Column('type_name', String(64)),
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
    Column('okz_code', String(16)),
    Column('okz_name', String(1024)),
    Column('okved_code', String(16)),
    Column('okved_name', String(1024)),
    Column('okpdtr_code', String(16)),
    Column('okpdtr_name', String(1024)),
    schema='data'
)


t_vw_invest_proj_years = Table(
    'vw_invest_proj_years', metadata,
    Column('id_invest_proj', Integer),
    Column('y_0', Float(53)),
    Column('y_1', Float(53)),
    Column('y_2', Float(53)),
    Column('y_3', Float(53)),
    Column('y_4', Float(53)),
    Column('y_5', Float(53)),
    Column('y_6', Float(53)),
    Column('y_7', Float(53)),
    Column('y_8', Float(53)),
    schema='data'
)


t_vw_okso_work = Table(
    'vw_okso_work', metadata,
    Column('id', Integer),
    Column('code', Text),
    Column('name', String(1024)),
    schema='data'
)


t_vw_okved = Table(
    'vw_okved', metadata,
    Column('id', Integer),
    Column('code', String(16)),
    Column('name', String(1024)),
    Column('dateadd', DateTime),
    schema='data'
)


t_vw_organization_form_age_lines = Table(
    'vw_organization_form_age_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_workers_age_type', Integer),
    Column('age', String(64)),
    Column('value', Integer),
    schema='data'
)


t_vw_organization_form_base_lines = Table(
    'vw_organization_form_base_lines', metadata,
    Column('id_type', Integer),
    Column('name', String(512)),
    Column('value', Integer),
    Column('id_form', Integer),
    schema='data'
)


t_vw_organization_form_educ_lines = Table(
    'vw_organization_form_educ_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okved', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okso', Integer),
    Column('id_educ_program_type', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('okved_code', String(16)),
    Column('okved_name', String(1024)),
    Column('okso_code', Text),
    Column('okso_name', String(1024)),
    Column('educ_program', String(32)),
    schema='data'
)


t_vw_organization_form_invest_req_lines = Table(
    'vw_organization_form_invest_req_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okz', Integer),
    Column('id_okved', Integer),
    Column('id_invest_proj', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('y_3', Integer),
    Column('y_4', Integer),
    Column('y_5', Integer),
    Column('okpdtr_code', String(16)),
    Column('okpdtr_name', String(1024)),
    Column('okz_code', String(16)),
    Column('okz_name', String(1024)),
    Column('okved_code', String(16)),
    Column('okved_name', String(1024)),
    schema='data'
)


t_vw_organization_form_pks_lines = Table(
    'vw_organization_form_pks_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okz', Integer),
    Column('value', Integer),
    Column('value2', Numeric(10, 2)),
    Column('okpdtr_code', String(16)),
    Column('okpdtr_name', String(1024)),
    Column('okz_code', String(16)),
    Column('okz_name', String(1024)),
    schema='data'
)


t_vw_organization_form_req_lines = Table(
    'vw_organization_form_req_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okz', Integer),
    Column('id_okved', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('y_3', Integer),
    Column('y_4', Integer),
    Column('y_5', Integer),
    schema='data'
)


t_vw_organization_form_ws_lines = Table(
    'vw_organization_form_ws_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okved', Integer),
    Column('id_okpdtr', Integer),
    Column('id_world_skills', Integer),
    Column('id_educ_program_type', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('okved_code', String(16)),
    Column('okved_name', String(1024)),
    Column('ws_code', String(16)),
    Column('ws_name', String(1024)),
    Column('educ_program', String(32)),
    schema='data'
)


t_vw_organization_form_years = Table(
    'vw_organization_form_years', metadata,
    Column('id_organization_poll_form', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('y_3', Integer),
    Column('y_4', Integer),
    Column('y_5', Integer),
    schema='data'
)


t_vw_organization_poll_form = Table(
    'vw_organization_poll_form', metadata,
    Column('id_organization_poll', Integer),
    Column('id_organization', Integer),
    Column('dateadd', DateTime),
    Column('organization_name', String(1024)),
    Column('year_for', Integer),
    Column('id_mrigo', Integer),
    Column('mrigo_name', String(1024)),
    schema='data'
)


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


class Organization(Base):
    __tablename__ = 'organization'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_id_seq'::regclass)"))
    inn = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False, unique=True)
    id_mrigo = Column(ForeignKey('data.mrigo.id'), nullable=False)
    id_okfs = Column(ForeignKey('data.okfs.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    is_educ = Column(Integer, server_default=text("1"))
    is_worker = Column(Integer, server_default=text("1"))

    mrigo = relationship('Mrigo')
    okf = relationship('Okf')


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


class InvestProjOkved(Base):
    __tablename__ = 'invest_proj_okved'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".invest_proj_okved_id_seq'::regclass)"))
    id_invest_proj = Column(ForeignKey('data.invest_proj.id', ondelete='CASCADE'), nullable=False)
    id_okved = Column(ForeignKey('data.okved.id', ondelete='CASCADE'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    invest_proj = relationship('InvestProj')
    okved = relationship('Okved')


class OrganizationEnrolFormLine(Base):
    __tablename__ = 'organization_enrol_form_line'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".organization_enrol_form_line_id_seq'::regclass)"))
    id_organization = Column(ForeignKey('data.organization.id'), nullable=False)
    id_organization_poll_form = Column(ForeignKey('data.organization_poll_form.id'), nullable=False)
    id_type_educ_form = Column(ForeignKey('data.type_educ_form.id'), nullable=False)
    id_okso = Column(ForeignKey('data.okso.id'))
    p1 = Column(Integer, server_default=text("0"))
    p2 = Column(Integer, server_default=text("0"))
    p3 = Column(Integer, server_default=text("0"))
    p4 = Column(Integer, server_default=text("0"))
    p5 = Column(Integer, server_default=text("0"))
    p6 = Column(Integer, server_default=text("0"))
    p7 = Column(Integer, server_default=text("0"))
    p8 = Column(Integer, server_default=text("0"))
    p9 = Column(Integer, server_default=text("0"))
    p10 = Column(Integer, server_default=text("0"))
    p11 = Column(Integer, server_default=text("0"))
    p12 = Column(Integer, server_default=text("0"))
    p13 = Column(Integer, server_default=text("0"))
    p14 = Column(Integer, server_default=text("0"))
    p15 = Column(Integer, server_default=text("0"))
    p16 = Column(Integer, server_default=text("0"))
    ege_b = Column(Numeric(8, 3))
    ege_k = Column(Numeric(8, 3))
    ege_common = Column(Numeric(8, 3))
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    okso = relationship('Okso')
    organization = relationship('Organization')
    organization_poll_form = relationship('OrganizationPollForm')
    type_educ_form = relationship('TypeEducForm')


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
    value = Column(Integer)
    year_for = Column(Integer)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    value2 = Column(Numeric(10, 2))
    id_educ_program_type = Column(ForeignKey('data.educ_program_type.id'))

    educ_program_type = relationship('EducProgramType')
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
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table, Text

metadata = MetaData()


t_vw_okso_work = Table(
    'vw_okso_work', metadata,
    Column('id', Integer),
    Column('code', Text),
    Column('name', String(1024)),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


t_vw_organization_form_age_lines = Table(
    'vw_organization_form_age_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_workers_age_type', Integer),
    Column('age', String(64)),
    Column('value', Integer),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


t_vw_organization_form_base_lines = Table(
    'vw_organization_form_base_lines', metadata,
    Column('id_type', Integer),
    Column('name', String(512)),
    Column('value', Integer),
    Column('id_form', Integer),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table, Text

metadata = MetaData()


t_vw_organization_form_educ_lines = Table(
    'vw_organization_form_educ_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okved', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okso', Integer),
    Column('id_educ_program_type', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('okved_code', String(16)),
    Column('okved_name', String(1024)),
    Column('okso_code', Text),
    Column('okso_name', String(1024)),
    Column('educ_program', String(32)),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


t_vw_organization_form_invest_req_lines = Table(
    'vw_organization_form_invest_req_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okz', Integer),
    Column('id_okved', Integer),
    Column('id_invest_proj', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('y_3', Integer),
    Column('y_4', Integer),
    Column('y_5', Integer),
    Column('okpdtr_code', String(16)),
    Column('okpdtr_name', String(1024)),
    Column('okz_code', String(16)),
    Column('okz_name', String(1024)),
    Column('okved_code', String(16)),
    Column('okved_name', String(1024)),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, Numeric, String, Table

metadata = MetaData()


t_vw_organization_form_pks_lines = Table(
    'vw_organization_form_pks_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okz', Integer),
    Column('value', Integer),
    Column('value2', Numeric(10, 2)),
    Column('okpdtr_code', String(16)),
    Column('okpdtr_name', String(1024)),
    Column('okz_code', String(16)),
    Column('okz_name', String(1024)),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, Table

metadata = MetaData()


t_vw_organization_form_req_lines = Table(
    'vw_organization_form_req_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okpdtr', Integer),
    Column('id_okz', Integer),
    Column('id_okved', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('y_3', Integer),
    Column('y_4', Integer),
    Column('y_5', Integer),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


t_vw_organization_form_ws_lines = Table(
    'vw_organization_form_ws_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_okved', Integer),
    Column('id_okpdtr', Integer),
    Column('id_world_skills', Integer),
    Column('id_educ_program_type', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('okved_code', String(16)),
    Column('okved_name', String(1024)),
    Column('ws_code', String(16)),
    Column('ws_name', String(1024)),
    Column('educ_program', String(32)),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, Table

metadata = MetaData()


t_vw_organization_form_years = Table(
    'vw_organization_form_years', metadata,
    Column('id_organization_poll_form', Integer),
    Column('y_0', Integer),
    Column('y_1', Integer),
    Column('y_2', Integer),
    Column('y_3', Integer),
    Column('y_4', Integer),
    Column('y_5', Integer),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table

metadata = MetaData()


t_vw_organization_poll_form = Table(
    'vw_organization_poll_form', metadata,
    Column('id_organization_poll', Integer),
    Column('id_organization', Integer),
    Column('dateadd', DateTime),
    Column('organization_name', String(1024)),
    Column('year_for', Integer),
    Column('id_mrigo', Integer),
    Column('mrigo_name', String(1024)),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table, Text

metadata = MetaData()


t_vw_okso_work = Table(
    'vw_okso_work', metadata,
    Column('id', Integer),
    Column('code', Text),
    Column('name', String(1024)),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


t_vw_organization_form_sex_lines = Table(
    'vw_organization_form_sex_lines', metadata,
    Column('id_form', Integer),
    Column('id_type', Integer),
    Column('id_workers_sex_type', Integer),
    Column('sex_type', String(64)),
    Column('value', Integer),
    schema='data'
)
# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


t_vw_educ_program_type = Table(
    'vw_educ_program_type', metadata,
    Column('id', Integer),
    Column('name', String(32)),
    schema='data'
)


t_vw_educ_program_type_ws = Table(
    'vw_educ_program_type_ws', metadata,
    Column('id', Integer),
    Column('name', String(32)),
    schema='data'
)
