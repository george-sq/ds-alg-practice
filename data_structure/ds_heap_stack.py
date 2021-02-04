#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2021/1/6 17:10
@Author : qiangzi
@File   : ds_heap_stack.py
@Todo   : 堆栈: 元素后进先出(LIFO)
"""


class HeapStack(object):
    """堆栈"""

    def __init__(self, element_list=(), size=None):
        self.element_list = []  # 堆栈元素集合
        self.top = None  # 栈顶元素
        self.size = size  # 堆栈长度
        self.length = 0  # 堆栈元素数目
        self.data_init(element_list)  # 堆栈数据初始化
        pass

    def __str__(self):
        return f"<HeapStack-{id(self)}: elements={self.element_list}>"

    def data_init(self, element_list):
        for item in element_list:
            self.push(item)
            pass
        pass

    def push(self, element):
        """入栈"""
        if not self.size or self.length < self.size:
            if self.element_list:
                self.element_list.append(element)
                pass
            else:
                self.element_list = [element]
                pass
            self.top = element
            self.length += 1
        else:
            raise EOFError("堆栈已满")
        return self

    def pop(self):
        """出栈"""
        ret_val = None
        if self.element_list:
            ret_val = self.element_list[-1]
            self.element_list = self.element_list[:-1]
            self.length -= 1
            pass
        else:
            raise EOFError("堆栈已空")
        pass
        return ret_val

    def get_top(self):
        """返回栈顶元素"""
        return self.top

    def clear(self):
        """清空栈"""
        self.element_list = []
        self.length = 0
        self.top = None
        pass
        return self

    def is_full(self):
        pass

    def is_empty(self):
        pass

    pass


def app():
    a = [1, 5, 9, 8, 2]
    hst = HeapStack(a)
    print(hst)
    hst.push(4)
    print(hst)
    hst.pop()
    print(hst)
    hst.clear()
    print(hst)
    print("---" * 20)
    hst.push(100)
    print(hst)
    hst.pop()
    print(hst)
    "[{]}"
    pass


if __name__ == '__main__':
    app()
