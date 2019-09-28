'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/29 9:47
@Software: PyCharm
@File    : call.py
'''
class CallTest():
    def __call__(self, a,b):
        print("This is call test")
        print('a = ',a,'b = ',b)

test = CallTest()

test(1,2)