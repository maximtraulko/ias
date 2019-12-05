#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from iastables import ps_classes


def get_menu_items(sess):
    """
    возврат меню
    :param sess:
    :return:
    """
    res = []
    for i in sess.query(ps_classes.MenuItem).order_by(ps_classes.MenuItem.id):
        t = {'href': i.href, 'caption': i.caption, 'descr': i.descr}
        subitems = []
        for j in sess.query(ps_classes.MenuSubitem).filter(ps_classes.MenuSubitem.id_menu_items == i.id
                                                           ).order_by(ps_classes.MenuSubitem.id):
            subitems.append({'href': j.href, 'caption': j.caption})
        t['subitems'] = subitems
        res.append(t)
    return res


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    Session = sessionmaker(bind=create_engine('postgresql://dba:UdrqNjWx@localhost/ias'))
    _sess = Session()
    logging.info(get_menu_items(_sess))
    #217.71.129.139:4194