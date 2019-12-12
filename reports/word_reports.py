#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import datetime
import psycopg2.extras
from docxtpl import DocxTemplate
postgreSQL_connect = "dbname='ias' user='dba' host='217.71.129.139' port='4194' password='UdrqNjWx'"
name_view = 'vw_rep_form_12'


def get_record():
    connection_postgreSQL = psycopg2.connect(postgreSQL_connect)
    cursor_postgreSQL = connection_postgreSQL.cursor(cursor_factory=psycopg2.extras.RealDictCursor) #psycopg2.extras.DictCursor
    cursor_postgreSQL.execute("SELECT * FROM {0}".format(name_view))
    data = cursor_postgreSQL.fetchall() #['р-ны Новосибирска', '00.01', 'Тестовая организация', 'Текстовая запись ОКПДТР.1', '0.1', '7211', 'СПО', 'Тестовая запись1', 1, 3, 1, 985, 1, 10, 11, 12, 13, 14, 15]
    # print(data)
    # print(data[0]['raion'])

    len_data = len(data)
    for i in range(0, len_data):
        n6 = ((int(data[i]['y_0'])) + (int(data[i]['y_1'])) + (int(data[i]['y_2'])) + (int(data[i]['y_3'])) + (int(data[i]['y_4'])) + (int(data[i]['y_5'])))
        data[i]['y_6'] = n6
    return data

def create_record(data, templ_path):
    tpl_name = templ_path + 'templates/list.docx'
    tpl = DocxTemplate(tpl_name)

    today = datetime.datetime.today()
    date_here = (today.strftime("%Y.%m.%d-%H.%M.%S"))
    tpl.render({'data': data})# '
    gen_path = templ_path+'generated/list-{0}.docx'.format(date_here)
    tpl.save(gen_path)
    return gen_path

if __name__ == '__main__':
    data_data = get_record()
    if data_data:
        create_record(data_data, "")
