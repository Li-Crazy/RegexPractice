'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/25 17:03
@Software: PyCharm
@File    : regex1.py
'''
import re
pattern  = r'\d+'
obj = re.compile(pattern,flags=0)

# 匹配内容返回迭代器
it = re.finditer(pattern,'2008年是多事之秋，512地震08奥运')
it1 = obj.finditer('2008年是多事之秋，512地震08奥运')
print(it)
for i in it:
    # print(i)
    print(i.group())
print(it1)
for i in it1:
    print(i)

# match匹配
pattern1 = r'foo'
obj = re.compile(pattern1,flags=0)

obj1 = re.match(pattern1,'foo,food on the table')
print(obj1.group())
obj2 = obj.match('foo,food on the table')
print(obj2.group())

# search匹配
obj3 = re.search(pattern1,'Foo,food on the table,foo')
print(obj3.group())
obj4 = obj.search('Foo,food on the table,foo')
print(obj4.group())

try:
    obj5 = re.fullmatch(pattern1,'foo')
    # obj5 = re.fullmatch(pattern1,'foo')
    obj6 = obj.fullmatch('foo')
    # obj6 = obj.fullmatch('fooo')
    print(obj5.group())
    print(obj6.group())
except AttributeError as e:
    print(e)