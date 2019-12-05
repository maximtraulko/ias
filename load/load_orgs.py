#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import logging
import csv
from entity import Organization, get_session

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    with open("../load/orgs.txt", encoding='utf-8') as tsvfile:
        sess = get_session()
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            org = Organization(inn=line[0], name=line[1], id_mrigo=1, id_okfs=12)
            sess.add(org)
        sess.commit()
