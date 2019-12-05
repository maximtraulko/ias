#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import psycopg2
import logging
from flask import jsonify
from iastables import db_config
# инвестпроект


def set_invest_proj_line(conn, id_invest_proj, id_type, year_start, y_0, y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8):
    cur = conn.cursor()
    update_sql = """
    update vw_invest_proj_lines
    set y_0 = %(y_0)s,
      y_1 = %(y_1)s,
      y_2 = %(y_2)s,
      y_3 = %(y_3)s,
      y_4 = %(y_4)s,
      y_5 = %(y_5)s,
      y_6 = %(y_6)s,
      y_7 = %(y_7)s,
      y_8 = %(y_8)s,
      id_type = %(id_type)s,
      id_invest_proj = %(id_invest_proj)s,
      year_start = %(year_start)s
    where id_type = %(id_type)s
      and year_start = %(year_start)s
      and id_invest_proj = %(id_invest_proj)s
    """
    cur.execute(update_sql, {"id_invest_proj": id_invest_proj, "id_type": id_type, "year_start": year_start,
                             "y_0": y_0, "y_1": y_1, "y_2": y_2, "y_3": y_3,
                             "y_4": y_4, "y_5": y_5, "y_6": y_6, "y_7": y_7, "y_8": y_8})
    conn.commit()
    cur.close()


def set_invest_proj_line_add(conn, id_invest_proj, id_type, year_start, y_0, y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8):
    cur = conn.cursor()
    update_sql = """
    update vw_invest_proj_lines_add
    set y_0 = %(y_0)s,
      y_1 = %(y_1)s,
      y_2 = %(y_2)s,
      y_3 = %(y_3)s,
      y_4 = %(y_4)s,
      y_5 = %(y_5)s,
      y_6 = %(y_6)s,
      y_7 = %(y_7)s,
      y_8 = %(y_8)s,
      id_type = %(id_type)s,
      id_invest_proj = %(id_invest_proj)s,
      year_start = %(year_start)s
    where id_type = %(id_type)s
      and year_start = %(year_start)s
      and id_invest_proj = %(id_invest_proj)s
    """
    cur.execute(update_sql, {"id_invest_proj": id_invest_proj, "id_type": id_type, "year_start": year_start,
                             "y_0": y_0, "y_1": y_1, "y_2": y_2, "y_3": y_3,
                             "y_4": y_4, "y_5": y_5, "y_6": y_6, "y_7": y_7, "y_8": y_8})
    conn.commit()
    cur.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    _conn = psycopg2.connect(dbname=db_config.DB, user=db_config.USER, password=db_config.PASSWORD, host=db_config.HOST, port=db_config.PORT)
    logging.debug(_conn)
    set_invest_proj_line(_conn, 1, 1, 2019, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    set_invest_proj_line(_conn, 1, 2, 2019, 11, 21, 31, 41, 51, 61, 71, 81, 91)
    set_invest_proj_line(_conn, 1, 3, 2019, 12, 22, 32, 42, 52, 62, 72, 82, 92)
    set_invest_proj_line(_conn, 1, 4, 2019, 13, 23, 33, 43, 53, 63, 73, 83, 93)
    _conn.close()

