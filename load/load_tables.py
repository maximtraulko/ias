# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Okz(Base):
    __tablename__ = 'okz'

    id = Column(Integer, primary_key=True, server_default=text("nextval('okz_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))
    cnt_groups = Column(Integer, server_default=text("0"))


class LdVacsOkz(Base):
    __tablename__ = 'ld_vacs_okz'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ld_vacs_okz_id_seq'::regclass)"))
    vac_name = Column(String(4000))
    okz = Column(String(4000))
    date_add = Column(DateTime, nullable=False, server_default=text("now()"))
    id_okz = Column(ForeignKey('okz.id'))

    okz1 = relationship('Okz')


class UtlVoGosFgos(Base):
    __tablename__ = 'utl_vo_gos_fgos'

    id = Column(Integer, primary_key=True, server_default=text("nextval('utl_vo_gos_fgos'::regclass)"))
    code_gos = Column(String(32))
    code_fgos = Column(String(32))


class Okved(Base):
    __tablename__ = 'okved'

    id = Column(Integer, primary_key=True, server_default=text("nextval('okved_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class LdOkzOkved(Base):
    __tablename__ = 'ld_okz_okved'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ld_okz_okved_id_seq'::regclass)"))
    okz = Column(String(4000))
    okved1 = Column(String(4000))
    okved2 = Column(String(4000))
    okved3 = Column(String(4000))
    date_add = Column(DateTime, nullable=False, server_default=text("now()"))
    id_okz = Column(ForeignKey('okz.id'))
    id_okved1 = Column(ForeignKey('okved.id'))
    id_okved2 = Column(ForeignKey('okved.id'))
    id_okved3 = Column(ForeignKey('okved.id'))

    okved = relationship('Okved', primaryjoin='LdOkzOkved.id_okved1 == Okved.id')
    okved4 = relationship('Okved', primaryjoin='LdOkzOkved.id_okved2 == Okved.id')
    okved5 = relationship('Okved', primaryjoin='LdOkzOkved.id_okved3 == Okved.id')
    okz1 = relationship('Okz')


class WorldSkill(Base):
    __tablename__ = 'world_skills'

    id = Column(Integer, primary_key=True, server_default=text("nextval('world_skills_id_seq'::regclass)"))
    code = Column(String(16), nullable=False)
    name = Column(String(1024), nullable=False)
    dateadd = Column(DateTime, nullable=False, server_default=text("now()"))


class LdOkzW(Base):
    __tablename__ = 'ld_okz_ws'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ld_okz_ws_id_seq'::regclass)"))
    okz = Column(String(4000))
    ws1 = Column(String(4000))
    ws2 = Column(String(4000))
    ws3 = Column(String(4000))
    date_add = Column(DateTime, nullable=False, server_default=text("now()"))
    id_okz = Column(ForeignKey('okz.id'))
    id_ws1 = Column(ForeignKey('world_skills.id'))
    id_ws2 = Column(ForeignKey('world_skills.id'))
    id_ws3 = Column(ForeignKey('world_skills.id'))

    okz1 = relationship('Okz')
    world_skill = relationship('WorldSkill', primaryjoin='LdOkzW.id_ws1 == WorldSkill.id')
    world_skill1 = relationship('WorldSkill', primaryjoin='LdOkzW.id_ws2 == WorldSkill.id')
    world_skill2 = relationship('WorldSkill', primaryjoin='LdOkzW.id_ws3 == WorldSkill.id')
