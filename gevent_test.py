'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/28 21:19
@Software: PyCharm
@File    : gevent1.py
'''
import gevent

def foo(a):
    print("Running in foo ",a)
    gevent.sleep(2)
    print("Switch to foo again")

def bar():
    print("Running in bar")
    gevent.sleep(3)
    print("Switch to bar again")

# 将事件加入到协程
f = gevent.spawn(foo,1)
b = gevent.spawn(bar)

# 回收协程
gevent.joinall([f,b])