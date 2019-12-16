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
    len_data = len(data)
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0
    sum_5 = 0
    sum_6 = 0
    for i in range(0, len_data):
        sum_1 = sum_1 + int(data[i]['y_0'])
        sum_2 = sum_2 + int(data[i]['y_1'])
        sum_3 = sum_3 + int(data[i]['y_2'])
        sum_4 = sum_4 + int(data[i]['y_3'])
        sum_5 = sum_5 + int(data[i]['y_4'])
        sum_6 = sum_6 + int(data[i]['y_5'])
    data_sum = [sum_1, sum_2, sum_3, sum_4, sum_5, sum_6]


    tpl_name = templ_path + 'templates/rep_form_12.docx'
    tpl = DocxTemplate(tpl_name)
    today = datetime.datetime.today()
    date_here = (today.strftime("%Y.%m.%d-%H.%M.%S"))
    m_0 = data_sum[0]
    m_1 = data_sum[1]
    m_2 = data_sum[2]
    m_3 = data_sum[3]
    m_4 = data_sum[4]
    m_5 =  data_sum[5]
    tpl.render({'data': data, 'm_0': m_0, 'm_1': m_1, 'm_2': m_2, 'm_3': m_3, 'm_4': m_4, 'm_5': m_5})
    gen_path = templ_path+'generated/rep_form_12-{0}.docx'.format(date_here)
    tpl.save(gen_path)
    return gen_path


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
    res = render_vw_rep_form_12(get_connection(), "")
    logging.debug(res)

