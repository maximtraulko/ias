#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""разбиваем позиции в резюме"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from iastables import ps_classes
from sqlalchemy import exists

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    Session = sessionmaker(bind=create_engine('postgresql://dba:UdrqNjWx@217.71.129.139:4194/ias'))
    sess = Session()
    res = sess.query(ps_classes.IasResumeClean).filter(
        ~exists().where(
            ps_classes.IasResumeClean.id == ps_classes.IasResumeOnePosition.id_ias_resume_clean
        ),
        ps_classes.IasResumeClean.title.like('%,%')
    )

    for i in res:
        for j in i.title.split(','):
            logging.info('{} {}'.format(j.strip().capitalize(), len(i.title.split(','))))
            p = ps_classes.IasResumeOnePosition(ias_resume_clean=i,
                                                pos_name=j.strip().capitalize(),
                                                pos_coeff=1./len(i.title.split(','))
                                                )
            sess.add(p)
    sess.commit()


