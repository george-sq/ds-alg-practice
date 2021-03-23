#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2021/1/5 08:55
@Author : qiangzi
@File   : common.py
@Todo   : something
"""


class Node(object):
    """
    数据节点
    """

    def __init__(self, data=None, pre_node=None, next_node=None, children=None):
        """
        数据节点(Node)初始化
        Args:
            data: 当前节点的数据值
            pre_node: 前驱结点
            next_node: 后继结点
            children: 子节点列表
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
