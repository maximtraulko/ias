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
