#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Загружаем данные в таблицу"""
import logging
import csv
from entity import UtlSPOGosFgos, WorldSkill, get_session, Okopf
import load_tables


def load_vo_gos(sess):
    with open("vo_gos.txt", encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            sgf = load_tables.UtlVoGosFgos(code_gos=line[0], code_fgos=line[1])
            sess.add(sgf)
        sess.commit()


def load_spo_gos(sess):
    with open("spo_gos.txt", encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            sgf = UtlSPOGosFgos(code_fgos=line[0], name_fgos=line[1], code_gos=line[2], name_gos=line[3])
            sess.add(sgf)
        sess.commit()


def load_ws(sess):
    with open("ws.txt", encoding='utf-8') as tsvfile:
        for line in tsvfile:
            logging.info(line)
            sgf = WorldSkill(code='-', name=line)
            sess.add(sgf)
        sess.commit()


def load_vacs_okz(sess):
    with open("vacs_okz.txt", encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            sgf = load_tables.LdVacsOkz(vac_name=line[0], okz=line[1])
            sess.add(sgf)
        sess.commit()


def load_okopf(sess):
    with open("okopf.txt", encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            sgf = Okopf(code=line[0], name=line[1])
            sess.add(sgf)
        sess.commit()


def load_okz_okved(sess):
    with open("okz_okved.txt", encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            try:
                vokved1 = line[1]
            except:
                pass
            try:
                vokved2 = line[2]
            except:
                pass
            try:
                vokved3 = line[3]
            except:
                pass
            sgf = load_tables.LdOkzOkved(okz=line[0], okved1=vokved1, okved2=vokved2, okved3=vokved3)
            sess.add(sgf)
        sess.commit()


def load_okz_ws(sess):
    with open("okz_ws.txt", encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            try:
                vws1 = line[1]
            except:
                pass
            try:
                vws2 = line[2]
            except:
                pass
            try:
                vws3 = line[3]
            except:
                pass
            sgf = load_tables.LdOkzW(okz=line[0], ws1=vws1, ws2=vws2, ws3=vws3)
            sess.add(sgf)
        sess.commit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    sess = get_session()
    load_okopf(sess)
