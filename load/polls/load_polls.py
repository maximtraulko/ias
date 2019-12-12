#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import logging
import requests
import json
import pandas as pd

URL = 'http://ias-poll.cloud.nstu.ru/admin/result_json_by_user/{0}?token=k97ho05x1rcjhwwiv4ox'


def load_poll1():
    """опрос школьников"""
    res = json.loads(requests.get(URL.format('1')).text)
    for i in res:
        for j in res[i]:
            logging.info('{0}-{1}'.format(j, res[i][j]))


def load_poll2():
    """опрос студентов"""
    res = json.loads(requests.get(URL.format('2')).text)
    educ_orgs = []
    for i in res:
        try:
            v35 = res[i]['35']['answers']
            logging.debug(v35)
            if type(v35) == dict:
                educ_orgs.append(v35['0'].strip())
            else:
                educ_orgs.append(v35[0].strip())
        except KeyError:
            pass
    return educ_orgs


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    eo = load_poll2()
    for i in eo:
        print(i)



