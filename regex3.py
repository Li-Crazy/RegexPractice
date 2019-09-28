'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/27 14:54
@Software: PyCharm
@File    : regex3.py
'''
import re

s = "Hello World"

# l = re.findall('h\w+',s)
l = re.findall('h\w+',s,re.I)
print(l)

s1 = """hello world
Hello kitty
hello China
"""
l1 = re.findall('^hello',s1)
l2 = re.findall('^Hello',s1,re.M)
l3 = re.findall('China$',s1)
l4 = re.findall('world$',s1,re.M)
l5 = re.findall('.+',s1)
l6 = re.findall('.+',s1,re.S)
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)

pattern1 = """(?P<dog>hello) #dog 组
\s+ #空字符
(world) #第二组用来匹配world
"""
s2 = """hello world
Hello kitty
hello China
"""
z = re.findall(pattern1,s2)
z1 = re.findall(pattern1,s2,re.X|re.I)
print(z)
print(z1)