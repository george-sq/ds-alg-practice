#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2021/1/5 08:56
@Author : qiangzi
@File   : ds_linked_list.py
@Todo   : 链表
"""
from typing import List
from collections.abc import Iterable

from common import Node


class LinkedList(object):
    head = None
    tail = None
    size = 0
    cursor = Node()
    
    def __init__(self):
        pass

    def __str__(self):
        return f"<LinkedList-{id(self)}: element size={self.size}, head={self.head}, tail={self.tail}>"

    def data_init(self, element_list: List[object]):
        """
        链表元素初始化
        :param element_list:
        :return:
        """
        raise NotImplementedError("需要实现链表的元素初始化")

    def data_iter(self):
        """
        链表元素迭代
        :return:
        """
        pass

    def add_element(self, element, index=-1):
        """
        链表元素新增
        :param element: 新增元素
        :param index: 元素添加的位置，默认=-1: 表示在链表尾部添加元素
        :return:
        """
        raise NotImplementedError("需要实现链表的元素添加逻辑")

    def remove_element(self, element):
        """
        链表元素删除
        :param element: 删除元素
        :return:
        """
        raise NotImplementedError("需要实现链表的元素删除逻辑")

    def get_element(self, element):
        """
        链表元素查询
        :param element: 查询元素
        :return:
        """
        raise NotImplementedError("需要实现链表的元素查询逻辑")

    def has_loop(self):
        """
        判断链表是否有环
        :return:
        """
        pass

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        pass
    pass


class SingleLinkedList(LinkedList):

    def __init__(self, elements: List[object] = None):
        """
        :param elements: 数据元素列表
        """
        super(SingleLinkedList, self).__init__()
        if elements:
            self.data_init(elements)
            pass
        pass

    def __str__(self):
        return f"<SingleLinkedList-{id(self)}: size={self.size}, data={self.get_show_data()}>"

    def get_show_data(self):
        l_data = []
        if self.head:
            temp_node = self.head
            while temp_node.next_node is not None:
                l_data.append(temp_node.data)
                temp_node = temp_node.next_node
                pass
            l_data.append(temp_node.data)
            pass
        pass
        return l_data

    def data_init(self, element_list: List[object]):
        for item in element_list:
            self.add_element(item)
            pass
        pass
        return self

    def get_end_node(self):
        pre_node = None
        end_node = None
        if not self.head:
            print("空链表")
            pass
        else:
            pre_node, end_node = self.head, self.head
            while end_node.next_node is not None:
                pre_node, end_node = end_node, end_node.next_node
                pass
            self.tail = end_node
            pass
        pass
        return pre_node, end_node

    def add_element(self, element, index=-1):
        # 实例化元素node
        element_node = Node(element)
        if not self.head:  # 空链表添加
            # 执行插入逻辑
            self.head, self.tail = element_node, element_node
        else:
            if -1 == index:  # 末尾添加
                if self.tail:
                    # 执行插入逻辑
                    self.tail.next_node, self.tail = element_node, element_node
                else:
                    self.get_end_node()
                    # 执行插入逻辑
                    self.tail.next_node, self.tail = element_node, element_node
                    pass
                pass
            else:  # 指定位置添加
                end_index = self.size - 1
                if end_index < index:  # index位置 > 链表长度, 执行末尾添加
                    self.add_element(element=element)
                    pass
                elif end_index == index:  # 末尾之前添加node
                    pre_node, end_node = self.get_end_node()
                    # 执行插入逻辑
                    pre_node.next_node, element_node.next_node = element_node, end_node
                    self.tail = end_node
                    pass
                else:
                    idx = 0
                    pre_node, temp_node = self.head, self.head
                    while (idx + 1) != index:  # fixme
                        temp_node = temp_node.next_node
                        idx += 1
                        pass
                    # 执行插入逻辑
                    element_node.next_node, temp_node.next_node = temp_node.next_node, element_node
                    pass
                pass
            pass
        pass
        self.size += 1
        return self

    def remove_element(self, element):
        if self.head:
            pre_node, temp_node = self.head, self.head
            while temp_node.data != element:
                pre_node, temp_node = temp_node, temp_node.next_node
                pass
            # 执行删除逻辑
            if temp_node.data == element:
                if temp_node == self.head:  # 删除元素为head
                    self.head = temp_node.next_node
                    pass
                else:
                    pre_node.next_node = temp_node.next_node
                self.size -= 1
            pass
        return self

    def get_element(self, element_data):
        ret_node = None
        if self.head:
            temp_node = self.head
            while temp_node.data != element_data:
                temp_node = temp_node.next_node
                pass
            if temp_node.data == element_data:
                ret_node = temp_node
                pass
            pass
        pass
        return ret_node


def app():
    element_list = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]
    sll = SingleLinkedList(elements=element_list)
    print(sll)
    sll = SingleLinkedList()
    sll.add_element(1)
    sll.add_element(10)
    print(sll)
    sll.add_element(100)
    print(sll)
    sll.add_element(999)
    print(sll)
    sll.remove_element(1)
    print(sll)
    pass


if __name__ == '__main__':
    app()
