#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import logging
import requests
import json

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    headers = {'Content-Type': 'application/json',
               'X-OpenAM-Username': 'oleg',
               'X-OpenAM-Password': '0'}
    r = requests.post('https://login.nstu.ru/ssoservice/json/authenticate', headers=headers)
    resp = r.json()
    logging.info(resp)
    token = resp['tokenId']
    #token = None
    r = requests.post("https://login.nstu.ru/ssoservice/json/sessions/%s?_action=validate" % token, headers={'content-type': 'application/json'}).content
    logging.info(r)
    r = r.decode('utf8').replace("'", '"')
    logging.info(r)
    resp2 = json.loads(r)
    logging.info(resp2)

