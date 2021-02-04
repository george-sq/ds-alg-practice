#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2021/1/4 16:56
@Author : qiangzi
@File   : ds_tree.py
@Todo   : 树
"""

from typing import List
from .common import Node


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
