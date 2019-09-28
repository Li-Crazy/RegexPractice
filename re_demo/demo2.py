'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/25 16:22
@Software: PyCharm
@File    : demo2.py
'''
import re
#验证手机号码
try:
    test = "13875797758"
    ret = re.match('1[34578]\d{9}',test)
    print(ret.group())
except AttributeError:
    print("No")

#验证邮箱
try:
    test = "QaDedcxzas_123@qwd.com"
    ret = re.match('\w+@[a-z0-9]+\.[a-z]+',test)
    print(ret.group())
except AttributeError:
    print("No")

#验证URL
try:
    test = "https://www.baidu.com"
    ret = re.match('(http|https|ftp)://[\S]+',test)
    print(ret.group())
except AttributeError:
    print("No")

#验证身份证
try:
    test = "12345678901234567x"
    ret = re.match('\d{17}[\dxX]',test)
    print(ret.group())
except AttributeError:
    print("No")
