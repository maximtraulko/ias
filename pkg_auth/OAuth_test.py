#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Обертка к http api OpenAM"""
import json
import requests
import logging
from oa_config import CONFIG


class OA2:
    """Статический класс, обертка к http api OpenAM"""
    @staticmethod
    def init(_config):
        logging.debug(_config)
        OA2.config = {"login_url": _config["login_url"], "logout_url": _config["logout_url"],
                     "validate_url": _config["validate_url"], "token": _config["token"]}

    @staticmethod
    def login_url(return_url):
        """URL страницы аутентификации"""
        return OA2.config["login_url"] % return_url

    @staticmethod
    def get_token(req):
        """Возврат токена аутентификации из request"""
        try:
            return req.cookies.get(OA2.config["token"])
        except KeyError:
            return None

    @staticmethod
    def validate_token(token, sentry):
        """Проверка токена и получение логина и реалма"""
        url = OA2.config["validate_url"] % token
        resp = json.loads(requests.post(url,
                                        headers={'content-type': 'application/json'}).content)
        if u"uid" not in resp:
            return None
        else:
            return {"login": resp[u"uid"], "realm": resp[u"realm"]}

    @staticmethod
    def logout(token):
        """Завершение сеанса"""
        url = OA2.config["logout_url"] % token
        resp = requests.post(url,
                             headers={'content-type': 'application/json',
                                      OA2.config["token"]: token}
                             ).content
        return resp


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    logging.debug(CONFIG)
    OA2.init(CONFIG['sso'])
    logging.debug(OA2.login_url('https://10.0.25.11'))
