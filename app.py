#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, Response, Request, abort
from flask_cors import CORS
from pkg_app import menu
from iastables import ps_classes
from pkg_auth import OAuth, oa_config
from functools import wraps
import logging
import zlib

HEADER_NAME = "AUTH-TOKEN"
CHECK_KEY = "iMjy8ysuPr3q7xApOGRF"
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)
SESS = ps_classes.get_session()
logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')


def ret_json(func):
    """Декоратор. Перед выполнением функции проверяется наличие ключа, если его нет, возвращается запрет"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            client_key = request.headers[HEADER_NAME]
            if client_key == CHECK_KEY:
                return Response(func(*args, **kwargs), content_type='application/json; charset=utf-8')
            else:
                return abort(401)
        except KeyError:
            return abort(403)
    return decorated_function


@app.after_request
def apply_header_for_cors(response):
    """Разрешение CORS, запрет кэширования"""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS, PATCH"
    response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept, AUTH-TOKEN"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers["Server"] = "ias-api"
    return response


@app.route('/')
def hello_world():
    return '.'


@app.route('/spa/check_auth')
def spa_check_auth():
    OAuth.OA.init(oa_config.CONFIG['sso'])
    app.logger.debug(request)
    token = OAuth.OA.get_token(request)
    auth_data = OAuth.OA.validate_token(token)
    app.logger.debug(auth_data)
    res = 1
    return jsonify(res)


@app.route('/spa/start_session')
def spa_start_session():
    OAuth.OA.init(oa_config.CONFIG['sso'])
    app.logger.debug(request.headers)
    token = OAuth.OA.get_token(request)
    auth_data = OAuth.OA.validate_token(token)
    app.logger.debug(auth_data)
    res = 1
    return jsonify(res)


@app.route('/spa/menu')
def spa_menu():
    _menu = menu.get_menu_items(SESS)
    return jsonify(_menu)


@app.route('/api/refs/<ref_name>')
@ret_json
def get_refs_data(ref_name):
    """возврат справочников"""
    try:
        _res = ps_classes.get_refs_data(SESS, ref_name)
        return _res
    except KeyError:
        return abort(404)


@app.route('/api/get/<entity_name>', defaults={'entity_id': 0})
@app.route('/api/get/<entity_name>/<int:entity_id>')
@ret_json
def get_entity_data(entity_name, entity_id):
    """возврат сущности"""
    try:
        _res = ps_classes.get_entity_data(SESS, entity_name, entity_id)
        return _res
    except KeyError:
        return abort(404)


@app.route('/api/get/lines/<lines_name>/<int:entity_id>')
@ret_json
def get_lines_data(lines_name, entity_id):
    """возврат сущности"""
    try:
        _res = ps_classes.get_entity_lines_data(SESS, lines_name, entity_id)
        return _res
    except KeyError:
        return abort(404)


@app.route('/api/set/<entity_name>/<int:entity_id>', methods=['POST'])
@ret_json
def edit_entity_data(entity_name, entity_id):
    """редактирование сущности"""
    _res = ps_classes.set_entity_data(SESS, entity_name, entity_id, request.data)
    return _res


@app.route('/api/set/lines/<lines_name>/<int:entity_id>', methods=['POST'])
@ret_json
def set_lines_data(lines_name, entity_id):
    """возврат сущности"""
    try:
        _res = ps_classes.set_entity_lines_data(SESS, lines_name, entity_id, request.data)
        return '{"result": "ok"}'
    except KeyError:
        return abort(404)


@app.route('/api/list/organization_poll', methods=['GET'])
@app.route('/api/list/organization_poll/', methods=['GET'])
@ret_json
def list_organization_poll():
    """список опросов"""
    year = request.args.get('year')
    id_mrigo = request.args.get('id_mrigo')
    _res = ps_classes.get_organization_poll(SESS, year, id_mrigo)
    return _res


if __name__ == '__main__':
    app.run(host='0.0.0.0')
