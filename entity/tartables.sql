# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Okopf(Base):
    __tablename__ = 'okopf'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okopf_id_seq'::regclass)"))
    code = Column(String(32), nullable=False, unique=True)
    name = Column(String(1024), nullable=False, unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TypeTargetOrg(Base):
    __tablename__ = 'type_target_org'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_target_org_id_seq'::regclass)"))
    name = Column(String(32), nullable=False, unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TargetStudyRequestStatu(Base):
    __tablename__ = 'target_study_request_status'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".target_study_request_status_id_seq'::regclass)"))
    name = Column(String(64), unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TypeOrganizationActivity(Base):
    __tablename__ = 'type_organization_activity'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_organization_activity_id_seq'::regclass)"))
    name = Column(String(64), unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))
# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Okf(Base):
    __tablename__ = 'okfs'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okfs_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class Okopf(Base):
    __tablename__ = 'okopf'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okopf_id_seq'::regclass)"))
    code = Column(String(32), nullable=False, unique=True)
    name = Column(String(1024), nullable=False, unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))


class Okso(Base):
    __tablename__ = 'okso'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".okso_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class Region(Base):
    __tablename__ = 'region'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".region_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    code = Column(String(16), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class TargetStudyRequestStatu(Base):
    __tablename__ = 'target_study_request_status'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".target_study_request_status_id_seq'::regclass)"))
    name = Column(String(64), unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))


class TypeMrigo(Base):
    __tablename__ = 'type_mrigo'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_mrigo_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class TypeOrganizationActivity(Base):
    __tablename__ = 'type_organization_activity'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_organization_activity_id_seq'::regclass)"))
    name = Column(String(64), unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))


class TypeTargetOrg(Base):
    __tablename__ = 'type_target_org'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".type_target_org_id_seq'::regclass)"))
    name = Column(String(32), nullable=False, unique=True)
    date_added = Column(DateTime, nullable=False, server_default=text("now()"))


class City(Base):
    __tablename__ = 'city'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"data\".city_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)
    id_region = Column(ForeignKey('data.region.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))

    region = relationship('Region')


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
    name = Column(String(1024), nullable=False, unique=True)
    id_mrigo = Column(ForeignKey('data.mrigo.id'), nullable=False)
    id_okfs = Column(ForeignKey('data.okfs.id'), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    is_educ = Column(Integer, server_default=text("1"))
    is_worker = Column(Integer, server_default=text("1"))

    mrigo = relationship('Mrigo')
    okf = relationship('Okf')


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

    organization = relationship('Organization', primaryjoin='TargetStudyRequest.id_educ_organization == Organization.id')
    mrigo = relationship('Mrigo')
    okopf = relationship('Okopf', primaryjoin='TargetStudyRequest.id_okopf_customer == Okopf.id')
    okopf1 = relationship('Okopf', primaryjoin='TargetStudyRequest.id_okopf_employer == Okopf.id')
    okso = relationship('Okso')
    organization1 = relationship('Organization', primaryjoin='TargetStudyRequest.id_organization == Organization.id')
    region = relationship('Region')
    target_study_request_statu = relationship('TargetStudyRequestStatu')
    type_organization_activity = relationship('TypeOrganizationActivity', primaryjoin='TargetStudyRequest.id_type_activity_customer == TypeOrganizationActivity.id')
    type_organization_activity1 = relationship('TypeOrganizationActivity', primaryjoin='TargetStudyRequest.id_type_activity_employer == TypeOrganizationActivity.id')
    type_target_org = relationship('TypeTargetOrg')
