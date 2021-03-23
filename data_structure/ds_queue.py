#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2021/1/6 18:12
@Author : qiangzi
@File   : ds_queue.py
@Todo   : 队列: 元素先进先出(FIFO)
"""


class Queue(object):
    """
    队列
        主要属性
            队头元素
            队尾元素
            队列元素容器
        主要操作
            入队
            出队
        重要逻辑
            队空逻辑
            队满逻辑
        应用类型
            顺序队列
            循环队列
            阻塞队列: 入队 或 出队 阻塞
            并发队列: 操作具有线程安全特点的队列
    """

    def __init__(self, element_list=(), max_length=256):
        self.element_list = []  # 队列元素
        self.head = None  # 队头元素
        self.tail = None  # 队尾元素
        self.max_length = max_length  # 队列的最大长度
        self.length = 0  # 队列元素数目
        self.data_init(element_list)  # 队列数据初始化
        pass

    def data_init(self, element_list):
        pass

    def enqueue(self, element):
        """入队"""
        pass

    def dequeue(self):
        """出队"""
        pass

    def get_head(self):
        """获取队头元素"""
        pass

    def get_tail(self):
        """获取队尾元素"""
        pass

    pass


def app():
    pass


if __name__ == '__main__':
    app()
