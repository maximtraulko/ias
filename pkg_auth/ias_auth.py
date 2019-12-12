#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import logging
import json
import hashlib
import uuid
from sqlalchemy import Column, DateTime, Integer, String, text, or_, and_
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm.exc
from entity import get_session
import random
import string

Base = declarative_base()
metadata = Base.metadata


class Role(Base):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'auth'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth.roles_id_seq'::regclass)"))
    name = Column(String(64))
    descr = Column(String(1024))


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'auth'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth.users_id_seq'::regclass)"))
    login = Column(String(64))
    user_role = Column(String(32))
    salt = Column(String(32))
    passw = Column(String(32))


class Token(Base):
    __tablename__ = 'tokens'
    __table_args__ = {'schema': 'auth'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth.tokens_id_seq'::regclass)"))
    token = Column(String(32))
    created = Column(DateTime, nullable=False, server_default=text("now()"))
    till = Column(DateTime)
    login = Column(String(64))


def add_user(sess, v_login, v_pass, v_role):
    salt = uuid.uuid4().hex
    #hashed_password = hashlib.sha512(v_pass.encode() + salt).hexdigest()
    hashed_password = v_pass
    usr = User(login=v_login, passw=hashed_password, salt=salt, user_role=v_role)
    sess.add(usr)
    sess.commit()


def check_token(sess, v_token):
    try:
        token = sess.query(Token).filter(Token.token == v_token).one()
        usr = sess.query(User).filter(User.login == token.login).one()
        return json.dumps({'role': usr.user_role, 'login': usr.login})
    except sqlalchemy.orm.exc.NoResultFound:
        return json.dumps({'role': None, 'login': None})


def auth_user(sess, v_login, v_pass):
    try:
        usr = sess.query(User).filter(and_(User.login == v_login, User.passw == v_pass)).one()
        try:
            token = sess.query(Token).filter(Token.login == v_login).one()
        except sqlalchemy.orm.exc.NoResultFound:
            stringLength = 32
            letters = string.ascii_letters
            tkn = ''.join(random.choice(letters) for i in range(stringLength))
            token = Token(login=v_login, token=tkn)
            sess.add(token)
            sess.commit()
        return json.dumps({'role': usr.user_role, 'token': token.token, 'login': v_login, 'greeting': 'Иван Иванович'})
    except sqlalchemy.orm.exc.NoResultFound:
        return json.dumps({'role': None, 'token': None, 'login': None, 'greeting': None})


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    _sess = get_session()
    #add_user(_sess, 'user1', 'pass1', 'MINISTRY_LABOR_SOCIAL_POLICY')
    #add_user(_sess, 'user2', 'pass2', 'MUNICIPAL_AUTHORITY')
    #add_user(_sess, 'user3', 'pass3', 'EDU_ORGANIZATION')
    #add_user(_sess, 'user4', 'pass4', 'MINISTRY_EDU')
    #add_user(_sess, 'user5', 'pass5', 'EMPLOYER')
    res = auth_user(_sess, 'user1', 'pass1')
    res = check_token(_sess, 'HIYTcvAsXfnLvTtzMpYzYJpfPZSYhmHz')
    logging.info(res)

