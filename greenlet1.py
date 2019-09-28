'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/28 21:01
@Software: PyCharm
@File    : greenlet1.py
'''
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

# 生成协程对象
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()