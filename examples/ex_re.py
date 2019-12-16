#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import re
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    with open('mytables.txt') as fp:
        for ln in fp:
            try:
                res = re.findall(r"Column(.*)", ln)[0][1:-1].split(',')
                print('{0} = Column({1})'.format(res[0].strip()[1:-1].strip(), res[1].strip()))
            except:
                print(ln)
