#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import datetime
import psycopg2.extras
import logging
from docxtpl import DocxTemplate
from entity import get_connection


def get_vw_rep_form_12(conn):
    curr = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    curr.execute("SELECT * FROM vw_rep_form_12")
    data = curr.fetchall()
    #['р-ны Новосибирска', '00.01', 'Тестовая организация', 'Текстовая запись ОКПДТР.1', '0.1', '7211', 'СПО', 'Тестовая запись1', 1, 3, 1, 985, 1, 10, 11, 12, 13, 14, 15]
    logging.debug(data)
    logging.debug(data[0]['raion'])

    len_data = len(data)
    for i in range(0, len_data):
        n6 = ((int(data[i]['y_0'])) + (int(data[i]['y_1'])) + (int(data[i]['y_2'])) + (int(data[i]['y_3'])) + (int(data[i]['y_4'])) + (int(data[i]['y_5'])))
        data[i]['y_6'] = n6
    return data


def render_vw_rep_form_12(conn, templ_path):
    data = get_vw_rep_form_12(conn)
    tpl_name = templ_path + 'templates/rep_form_12.docx'
    tpl = DocxTemplate(tpl_name)

    today = datetime.datetime.today()
    date_here = (today.strftime("%Y.%m.%d-%H.%M.%S"))
    tpl.render({'data': data})
    gen_path = templ_path+'generated/rep_form_12-{0}.docx'.format(date_here)
    tpl.save(gen_path)
    return gen_path


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    res = render_vw_rep_form_12(get_connection(), "")
    logging.debug(res)

