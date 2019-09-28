'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/25 16:51
@Software: PyCharm
@File    : demo3.py
'''
import re

#1.^(脱字号)：以……开始,等同于match函数,[^]在中括号里表示取反
try:
    test = "hello!"
    # ret = re.match('^h',test)
    ret = re.search('^h',test)#search函数，从整个字符串里查找
    print(ret.group())
except AttributeError:
    print("No")

#2.$：以……结束
try:
    test = "13rsfsdf@163.com"
    ret = re.match('\w+@163.com$',test)
    print(ret.group())
except AttributeError:
    print("No")

#3.|：匹配多个表达式或字符
try:
    test = "http://www.163.com"
    ret = re.match('http|https',test)
    print(ret.group())
except AttributeError:
    print("No")

#4.贪婪模式和非贪婪模式
try:
    test = "1234567890"
    ret1 = re.match('\d+',test)#贪婪模式，尽可能多的匹配
    ret2 = re.match('\d+?',test)#非贪婪模式，尽可能少的匹配
    print(ret1.group())
    print(ret2.group())
except AttributeError:
    print("No")

try:
    test = "<h1>标题<\h1>"
    ret1 = re.match('<.+>',test)#贪婪模式，尽可能多的匹配
    ret2 = re.match('<.+?>',test)#非贪婪模式，尽可能少的匹配
    print(ret1.group())
    print(ret2.group())
except AttributeError:
    print("No")

#5.:匹配0-100之间数字
#不能以0开头，三种情况，1，11，100.
try:
    test = "99"
    ret = re.match('[1-9]\d?$|100$',test)#[1-9]\d?$匹配1-99,\d?匹配0或1个数字
    print(ret.group())
except AttributeError:
    print("No")

