#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import logging
import csv
from iastables import ps_classes

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    with open("../load/orgs.txt", encoding='utf-8') as tsvfile:
        sess = ps_classes.get_session()
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            org = ps_classes.Organization(inn=line[0], name=line[1], id_mrigo=1, id_okfs=12)
            sess.add(org)
        sess.commit()
