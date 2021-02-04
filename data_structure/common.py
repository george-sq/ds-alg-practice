#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2021/1/5 08:55
@Author : qiangzi
@File   : common.py
@Todo   : something
"""

import logging

# __all__ = []
#
# __log_format = "%(asctime)s [ %(levelname)-7s ] | %(filename)-24s(line:%(lineno)-4s)-%(process)d(%(thread)d) || %(message)s"
# __date_format = "%Y-%m-%d(%A) %H:%M:%S(%Z)"
# logging.basicConfig(level=logging.DEBUG, format=__log_format, datefmt=__date_format)
# logger = logging.getLogger(__name__)


class Node(object):

    def __init__(self, data=None, pre_node=None, next_node=None, children=None):
        """

        :param data: 当前节点的数据值
        :param pre_node: 前驱结点
        :param next_node: 后继结点
        :param children: 子节点列表
        """

        self.data = data
        self.next_node = next_node
        self.pre_node = pre_node
        self.children = children
        pass

    def __str__(self):
        return f"<Node-{id(self)}: data={self.data}, next={id(self.next_node)}, pre={id(self.pre_node)}, children={id(self.children)}>"
    pass


def app():
    pass


if __name__ == '__main__':
    app()
