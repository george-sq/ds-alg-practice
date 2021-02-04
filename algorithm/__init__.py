#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2021/1/4 17:29
@Author : qiangzi
@File   : __init__.py
@Todo   : 算法模块
"""

import logging

# __all__ = []

__log_format = "%(asctime)s [ %(levelname)-7s ] | %(filename)-24s(line:%(lineno)-4s)-%(process)d(%(thread)d) || %(message)s"
__date_format = "%Y-%m-%d(%A) %H:%M:%S(%Z)"
logging.basicConfig(level=logging.DEBUG, format=__log_format, datefmt=__date_format)
logger = logging.getLogger(__name__)


def app():
    pass


if __name__ == '__main__':
    app()
