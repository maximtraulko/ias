#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
from api import *
from squtils import *
__all__ = ["get_refs_data", "get_entity_lines_data", "get_session", "get_organization_poll", "get_entity_data",
           "set_entity_data", "set_entity_lines_data"]


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(lineno)d %(asctime)s %(message)s')
