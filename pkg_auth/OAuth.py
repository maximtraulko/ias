#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Обертка к http api OpenAM"""
import json
import requests
import logging


class OA:
    """Статический класс, обертка к http api OpenAM"""
    @staticmethod
    def init(_config):
        logging.debug(_config)
        OA.config = {"login_url": _config["login_url"], "logout_url": _config["logout_url"],
                     "validate_url": _config["validate_url"], "token": _config["token"]}

    @staticmethod
    def login_url(return_url):
        """URL страницы аутентификации"""
        return OA.config["login_url"] % return_url

    @staticmethod
    def get_token(req):
        """Возврат токена аутентификации из request"""
        try:
            return req.cookies.get(OA.config["token"])
        except KeyError:
            return None

    @staticmethod
    def validate_token(token):
        """Проверка токена и получение логина и реалма"""
        url = OA.config["validate_url"] % token
        logging.debug(url)
        res = requests.post(url, headers={'content-type': 'application/json'}).content
        logging.debug(res)
        res = res.decode('utf8').replace("'", '"')
        resp = json.loads(res)
        logging.debug(resp)
        if u"uid" not in resp:
            return None
        else:
            return {"login": resp[u"uid"], "realm": resp[u"realm"]}

    @staticmethod
    def logout(token):
        """Завершение сеанса"""
        url = OA.config["logout_url"] % token
        resp = requests.post(url,
                             headers={'content-type': 'application/json',
                                      OA.config["token"]: token}
                             ).content
        return resp


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    # logging.debug(CONFIG)
    # OA.init(CONFIG['sso'])
    # logging.debug(OA.login_url('https://10.0.25.11'))
