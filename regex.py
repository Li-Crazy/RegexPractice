'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/25 16:38
@Software: PyCharm
@File    : regex.py
'''
import re

pattern = r'ab'

# 获取正则表达式对象
obj = re.compile(pattern=pattern,flags=0)
l = obj.findall("abcdfeabcabab")
l1 = obj.findall("abcdfeabcabab",6,9)
l2 = re.findall(pattern,"abcdfeabcabab",flags=0)
print(l)
print(l1)
print(l2)

# 匹配目标字符串进行切割
l3 = obj.split("hello ab world")
l4 = re.split(pattern,"hello ab world")
print(l3)
print(l4)

# 替换目标字符串中匹配到的内容
s = obj.sub("cd","abd133ab554ab",2)
s2 = obj.subn("cd","abd133ab554ab",2)
s1 = re.sub(pattern,"cd","abd133ab554ab",2)
s3 = re.subn(pattern,"cd","abd133ab554ab",2)
print(s)
print(s1)
print(s2)
print(s3)