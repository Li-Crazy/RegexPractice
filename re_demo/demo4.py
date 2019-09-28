'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/25 19:40
@Software: PyCharm
@File    : demo4.py
'''
import re

#1.转义字符'\',转义特殊字符
try:
    test = "apple price is $299"
    ret = re.search('\$\d+',test)#
    print(ret.group())
except AttributeError:
    print("No")

#原生字符串 'r',忽略python的转义
try:
    test = "\\n"
    test1 = r"\n"
    print(test)
    print(test1)
except AttributeError:
    print("No")

try:
    test = "\c"
    #python:'\\n' ->'\n'
    #1.\\\\n -> \\n
    #\\c
    #正则：\n ->
    #2. \\n -> \n
    #\\c -> \c
    # ret = re.search('\\\\c',test)#先将字符串通过python转义，再通过正则表达式转义
    ret = re.search(r'\\c',test)#先将字符串通过python转义，再通过正则表达式转义
    print(ret.group())
except AttributeError:
    print("No")
