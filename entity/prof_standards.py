#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Работа с проф. стандартами
"""
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text, Text, TIMESTAMP, Float, JSON, Date, Numeric, Table
from sqlalchemy.orm import relationship, exc
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
import logging

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
    educ_req = Column(String(4000), nullable=False)
    remark = Column(String(4000))
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


class UtlSPOGosFgos(Base):
    __tablename__ = 'utl_spo_gos_fgos'
    __table_args__ = {'schema': 'data'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('data.utl_spo_gos_fgos_id_seq'::regclass)"))
    code_fgos = Column(String(32), nullable=False)
    name_fgos = Column(String(1024), nullable=False)
    code_gos = Column(String(32), nullable=False)
    name_gos = Column(String(1024), nullable=False)



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


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
