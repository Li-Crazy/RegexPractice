'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/24 19:29
@Software: PyCharm
@File    : demo1.py
'''
import re

#1.匹配某个字符串
test = "hello!"
ret = re.match('he',test)#match从开头匹配字符
print(ret.group())

#2.点(.):匹配任意字符
test = "hello!"
ret = re.match('.',test)# .匹配任意一个字符，不能匹配换号符'\n'
print(ret.group())

#3.\d: 匹配任意数字（0-9）
test = "2"
ret = re.match('\d',test)
print(ret.group())

#4.\D: 匹配任意非数字
test = "+"
ret = re.match('\D',test)
print(ret.group())

#5.\s: 匹配空白字符（\n,\t,\r,空白）
test = "\n"
ret = re.match('\s',test)
print(ret.group())

#6.\w: 匹配a-z、A-Z、数字和下划线
test = "2"
ret = re.match('\w',test)
print(ret.group())

#7.\W: 与\w相反
test = "+"
ret = re.match('\W',test)
print(ret.group())

#8.[]组合的方式，只要满足中括号里的字符就可以匹配
test = "a2"
ret = re.match('[a2]',test)
print(ret.group())

test = "0731-88888888"
ret = re.match('[\d\-]+',test)#+ 匹配一个或多个前面的字符
print(ret.group())

#以[]组合表示\d、\D、\w、\W
test = "2q"
ret = re.match('[0-9]',test)#\d
ret1 = re.match('[^0-9]',test)#^非0-9=\D
ret2 = re.match('[a-zA-Z0-9_]',test)#\w
ret3 = re.match('[^a-zA-Z0-9_]',test)#\W
print(ret.group())

#匹配多个字符
#9.*: 匹配0或任意多个字符
test = "0731"
ret = re.match('\d*',test)
print(ret.group())

#10.+: 匹配一或任意多个字符
test = "ab+cd"
ret = re.match('\w+',test)
print(ret.group())

#11.?: 匹配一个或0个字符
test = "ab+cd"
ret = re.match('\w?',test)
print(ret.group())

#12.{m}: 匹配m个字符
test = "abcd"
ret = re.match('\w{2}',test)
print(ret.group())

#12.{m,n}: 匹配m-n个字符(尽可能多的匹配）
test = "abcd"
ret = re.match('\w{2,5}',test)
print(ret.group())
