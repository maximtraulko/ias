#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mytables import *
from squtils import *
import sqlalchemy.exc
import sqlalchemy.inspection
from sqlalchemy.inspection import inspect


def get_refs_data(_sess, ref_name):
    """возврат данных справочников"""
    try:
        tclass = REFS_CLASSES[ref_name.lower()]
        _res = _sess.query(tclass).all()
        return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)
    except KeyError as e:
        return rpc2resp(error_code=1001, error_message="{0} not implemented".format(e.args[0]))
    except (sqlalchemy.exc.ProgrammingError, sqlalchemy.exc.IntegrityError, sqlalchemy.exc.DataError,
            sqlalchemy.exc.InvalidRequestError) as e:
        try:
            _sess.rollback()
        except:
            pass
        return rpc2resp(error_code=1002, error_message="SQLA error - {0}".format(e))


def get_entity_data(_sess, entity_name, entity_id):
    """возврат данных сущности"""
    try:
        tclass = ENTITY[entity_name.lower()]
        _res = None
        if entity_id > 0:
            _res = _sess.query(tclass).get(entity_id)
        else:
            _res = _sess.query(tclass).all()
        return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)
    except KeyError as e:
        return rpc2resp(error_code=1001, error_message="{0} not implemented".format(e.args[0]))
    except (sqlalchemy.exc.ProgrammingError, sqlalchemy.exc.IntegrityError, sqlalchemy.exc.DataError,
            sqlalchemy.exc.InvalidRequestError) as e:
        try:
            _sess.rollback()
        except:
            pass
        return rpc2resp(error_code=1002, error_message="SQLA error - {0}".format(e))


def get_entity_lines_data(_sess, lines_name, entity_id):
    """возврат данных сущности"""
    try:
        tclass = ENTITY_LINES[lines_name.lower()]['class']
        tid = ENTITY_LINES[lines_name.lower()]['parent_id']
        sort_col = ENTITY_LINES[lines_name.lower()]['sort']
        _res = _sess.query(tclass).\
            filter(tid == entity_id).order_by(sort_col).all()
        return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)
    except KeyError as e:
        return rpc2resp(error_code=1001, error_message="{0} not implemented".format(e.args[0]))
    except (sqlalchemy.exc.ProgrammingError, sqlalchemy.exc.IntegrityError, sqlalchemy.exc.DataError,
            sqlalchemy.exc.InvalidRequestError) as e:
        try:
            _sess.rollback()
        except:
            pass
        return rpc2resp(error_code=1002, error_message="SQLA error - {0}".format(e))


def get_organization_poll(_sess, year_for, id_mrigo):
    _res = _sess.query(VWOrganizationPollForm).all()
    #filter(VWOrganizationPollForm.year_for == year_for and VWOrganizationPollForm.id_mrigo == id_mrigo)
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def set_entity_data(_sess, _entity_name, _entity_id, _data):
    """редактирование сущности"""
    try:
        tclass = ENTITY[_entity_name.lower()]
        tid = ENTITY_ID[_entity_name.lower()]
    except KeyError as ke:
        return rpc2resp(error_code=1001, error_message="{0} not implemented".format(ke.args[0]))
    try:
        tr = json2attrs(tclass, _data)
        _sess.query(tclass).filter(tid == _entity_id).update(tr[0])
        _sess.commit()
        return rpc2resp(res="ok", _id=_entity_id)
    except (sqlalchemy.exc.ProgrammingError, sqlalchemy.exc.IntegrityError, sqlalchemy.exc.DataError,
            sqlalchemy.exc.OperationalError, sqlalchemy.exc.InvalidRequestError, KeyError) as e:
        try:
            _sess.rollback()
        except:
            pass
        return rpc2resp(error_code=1002, error_message="SQLA error - {0}".format(e))


def set_entity_lines_data(_sess, _lines_name, _entity_id, _data):
    """редактирование подчиненных строк сущности"""
    try:
        tclass = ENTITY_LINES[_lines_name.lower()]['class']
        _tid = ENTITY_LINES[_lines_name.lower()]['id']
        _teid = ENTITY_LINES[_lines_name.lower()]['parent_id']
    except KeyError as ke:
        return rpc2resp(error_code=1001, error_message="{0} not implemented".format(ke.args[0]))
    # преобразуем в массив
    trls = json2attrs(tclass, _data)
    _tid_name = str(_tid).split('.')[1]
    _teid_name = str(_teid).split('.')[1]
    _res = ''
    # удаление
    try:
        old_ids = {i[0] for i in _sess.query(_tid).filter(_teid == _entity_id).all()}
        new_ids = {i[_tid_name] for i in trls}
        delta_ids = old_ids - new_ids
        _ = [_sess.query(tclass).filter(_teid == _entity_id and _tid == did).delete() for did in delta_ids]
    except (sqlalchemy.exc.ProgrammingError, sqlalchemy.exc.IntegrityError, sqlalchemy.exc.DataError,
            sqlalchemy.exc.OperationalError, sqlalchemy.exc.InvalidRequestError, KeyError) as e:
        try:
            _sess.rollback()
        except:
            pass
        return rpc2resp(error_code=1002, error_message="SQLA error - {0}".format(e))
    # добавление и изменение
    try:
        for tr in trls:
            _id = tr[_tid_name]
            tr[_teid_name] = _entity_id
            cnt = _sess.query(tclass).filter(_tid == _id).count()
            # если есть такая строка
            has_string = cnt > 0
            _res = None
            if has_string:
                _sess.query(tclass).filter(_tid == _id).update(tr)
                _res = 'ok:updated'
            else:
                obj = tclass(**tr)
                _sess.add(obj)
                _res = 'ok:inserted'
            _sess.commit()
        return rpc2resp(res=_res, _id=_entity_id)
    except (sqlalchemy.exc.ProgrammingError, sqlalchemy.exc.IntegrityError, sqlalchemy.exc.DataError, KeyError) as e:
        try:
            _sess.rollback()
        except:
            pass
        return rpc2resp(error_code=1002, error_message="SQLA error - {0}".format(e))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    sess = get_session()
    res = get_refs_data(sess, 'okopf')
    res = get_refs_data(sess, 'vw_organization_vo')
    # res = set_entity_lines_data(sess, 'invest_proj_line_add', 1, '[{"id_type":7, "id_okpdtr":1, "y_0":100},
    # {"id_type":7, "id_okpdtr":44657, "y_0":200}]')
    #res = set_entity_data(sess, 'invest_proj', 1,
    #                      '{"name":"Тестовый проект","id_organization":1,"invest_sum":"600001","date_start":"2019-11-01","date_finish":"2024-12-31"}')
    #res = set_entity_data(sess, 'organization_form', 1,
                          #'{"cnt": null, "id_form": 1, "id_mrigo": 1, "id_okfs": 1, "id_organization": 1, "mrigo_name": "р-ны Новосибирска", "okfs_name": "Тестовая запись", "organization_name": "Тестовая организация", "salary": null, "year_for": 2019}')
    # res = get_entity_lines_data(sess, 'invest_proj_line', 1)
    #res = set_entity_lines_data(sess, 'organization_okved', 1, '[{"id_okved":4921},{"id_okved":4920}]')
    #res = get_organization_poll(sess, 2019, 1)
    #Organization
    #res = sqlalchemy.inspection.inspect(Organization).primary_key[0]
    #res = sess.query(VWOrganizationPollForm).all()
    logging.debug(res)
