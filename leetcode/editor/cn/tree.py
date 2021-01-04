#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2021/1/4 16:56
@Author : qiangzi
@File   : tree.py
@Todo   : something
"""

import logging
from typing import List

# __all__ = []
#
# __log_format = "%(asctime)s [ %(levelname)-7s ] | %(filename)-24s(line:%(lineno)-4s)-%(process)d(%(thread)d) || %(message)s"
# __date_format = "%Y-%m-%d(%A) %H:%M:%S(%Z)"
# logging.basicConfig(level=logging.DEBUG, format=__log_format, datefmt=__date_format)
# logger = logging.getLogger(__name__)


class Node(object):

    def __init__(self, data, children):
        """
        :param data: 当前节点值
        :param children: 子节点列表
        """
        self.data = data
        self.children = children
    pass


class TreeNode(Node):

    def __init__(self, data, children):
        super().__init__(data, children)
        self.left = None
        self.right = None

    pass


class Tree(object):

    def __init__(self, node_list: List[Node]):
        self.node_size = len(node_list)
        self.depth = None  # 树的深度
        self.level = None  # 树的层数
        pass
    pass


class BinaryTree(object):
    pass


def app():
    pass


if __name__ == '__main__':
    app()
