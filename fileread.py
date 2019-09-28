'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/27 14:37
@Software: PyCharm
@File    : fileread.py
'''
import re

l = []
pattern = r'[A-Z][_.0-9a-zA-Z]*'

with open('regex.txt','r',encoding='utf-8') as f:
    for line in f:
        l += re.findall(pattern,line)

print(l)