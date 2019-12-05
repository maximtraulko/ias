#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mytables import *
from squtils import *


Base = declarative_base()
metadata = Base.metadata


def get_refs_data(_sess, ref_name):
    """возврат данных справочников"""
    tclass = REFS_CLASSES[ref_name.lower()]
    _res = _sess.query(tclass).all()
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def get_entity_data(_sess, entity_name, entity_id):
    """возврат данных сущности"""
    tclass = ENTITY[entity_name.lower()]
    _res = None
    if entity_id > 0:
        _res = _sess.query(tclass).get(entity_id)
    else:
        _res = _sess.query(tclass).all()
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def get_entity_lines_data(_sess, lines_name, entity_id):
    """возврат данных сущности"""
    tclass = ENTITY_LINES[lines_name.lower()]['class']
    tid = ENTITY_LINES[lines_name.lower()]['parent_id']
    sort_col = ENTITY_LINES[lines_name.lower()]['sort']
    _res = _sess.query(tclass).\
        filter(tid == entity_id).order_by(sort_col).all()
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def get_organization_poll(_sess, year_for, id_mrigo):
    _res = _sess.query(VWOrganizationPollForm).\
        filter(VWOrganizationPollForm.year_for == year_for and VWOrganizationPollForm.id_mrigo == id_mrigo).all()
    return json.dumps(_res, cls=new_alchemy_encoder(False, ['parents']), check_circular=False)


def set_entity_data(_sess, _entity_name, _entity_id, _data):
    """редактирование сущности"""
    try:
        tclass = ENTITY[_entity_name.lower()]
    except KeyError as ke:
        return 'error:/api/set/lines/ not implemented "{0}"'.format(ke.args[0])
    tr = json2attrs(tclass, _data)
    _sess.query(tclass).filter(tclass.id == _entity_id).update(tr[0])
    _sess.commit()
    return "{'result':'ok'}"


def set_entity_lines_data(_sess, _lines_name, _entity_id, _data):
    """редактирование подчиненных строк сущности"""
    try:
        tclass = ENTITY_LINES[_lines_name.lower()]['class']
        _tid = ENTITY_LINES[_lines_name.lower()]['id']
        _teid = ENTITY_LINES[_lines_name.lower()]['parent_id']
    except KeyError as ke:
        return json.dumps({'result': 'error:/api/set/lines/ not implemented "{0}"'.format(ke.args[0])})
    # преобразуем в массив
    trls = json2attrs(tclass, _data)
    _tid_name = str(_tid).split('.')[1]
    _teid_name = str(_teid).split('.')[1]
    _res = ''
    # удаление
    old_ids = {i[0] for i in _sess.query(_tid).filter(_teid == _entity_id).all()}
    new_ids = {i[_tid_name] for i in trls}
    delta_ids = old_ids - new_ids
    _ = [_sess.query(tclass).filter(_teid == _entity_id and _tid == did).delete() for did in delta_ids]
    # добавление и изменение
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
    return _res


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    sess = get_session()
    # res = get_refs_data(sess, 'okved')
    # res = set_entity_lines_data(sess, 'invest_proj_line_add', 1, '[{"id_type":7, "id_okpdtr":1, "y_0":100},
    # {"id_type":7, "id_okpdtr":44657, "y_0":200}]')
    # res = set_entity_data(sess, 'invest_proj', 1, '{"name":"Тестовый проект","id_organization":1,
    # "invest_sum":"400001","date_start":"2019-11-01","date_finish":"2024-12-31"}')
    # res = get_entity_lines_data(sess, 'invest_proj_line', 1)
    res = set_entity_lines_data(sess, 'invest_proj_okved', 1, '[{"id_okved":4921},{"id_okved":4920}]')
    logging.debug(res)
