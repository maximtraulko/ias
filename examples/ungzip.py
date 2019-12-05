#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Про что этот файл?"""
import logging
import zlib

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s')
    zdata = b'7b226e616d65223a22d0a2d0b5d181d182d0bed0b2d18bd0b920d0bfd180d0bed0b5d0bad182222c2269645f6f7267616e697a6174696f6e223a312c22696e766573745f73756d223a22323030303030222c22646174655f7374617274223a22323031392d31312d3031222c22646174655f66696e697368223a22323032342d31322d3331227d'
    zlib.decompress(zdata, 16+zlib.MAX_WBITS)

