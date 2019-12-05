#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import logging
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import db_config
import datetime
import decimal


def get_session():
    """
    Возврат сессии
    """
    _sess = sessionmaker(bind=create_engine('postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        db_config.USER, db_config.PASSWORD, db_config.HOST, db_config.PORT, db_config.DB)))()
    return _sess


def json2attrs(_tclass, _data):
    """преобразуем json в список словарей и убираем лишние атрибуты"""
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


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
