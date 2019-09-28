'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/25 21:48
@Software: PyCharm
@File    : demo5.py
'''
import re

#分组
try:
    test = "apple's price is $299，orange's price is $199"
    ret = re.search('.*(\$\d+).*(\$\d+)',test)#
    print(ret.group())
    print(ret.group(0))#整个大的分组
    print(ret.group(1))#第一个括号的分组
    print(ret.group(2))
    print(ret.group(1,2))
    print(ret.groups())#所有子分组
except AttributeError:
    print("No")

#findall函数,找出所有满足条件的 并返回一个列表
try:
    test = "apple's price is $299，orange's price is $199"
    ret = re.findall('\$\d+',test)#
    print(ret)
except AttributeError:
    print("No")

#sub函数，字符串替换
try:
    test = "apple price is $299，orange price is $199"
    ret = re.sub('\$\d+','0',test)#
    print(ret)
except AttributeError:
    print("No")
#提取文本
html = """
<div class="job-detail">
<p>岗位职责：</p>
<p>1、参与公司内部产品系统的设计与方案讨论；</p>
<p>2、开发并且维护内部产品系统平台；</p>
<p>3、建立并且持续维护开发文档；</p>
<p>4、完善并遵守团队的开发规范，编写高质量、结构清晰、易读、易维护的代码。</p>
<p><br></p>
<p>任职要求：</p>
<p>1、1年以上python开发工作经验；精通python2或python3编程语言；</p>
<p>2、熟练使用Git管理代码；熟悉Linux开发、部署环境；</p>
<p>3、熟练使用一种关系型数据库，如MySQL/PostgreSQL/SQLServer等;</p>
<p>4、有良好的编程习惯，沟通能力强，能够独自编写技术文档；</p>
<p>5、具备较好的学习能力、问题分析能力，可以独立调试解决问题；</p>
<p>6、良好的沟通协调能力和团队合作意识，工作踏实，态度积极，能够承受工作压力；</p>
<p>7、参与过开源项目者或对社区软件项目有贡献者优先；</p>
<p>8、较好的英文阅读以及搜索能力；</p>
<p>9、会bootstrap、odoo框架的优先。</p>
        </div>"""

ret = re.sub('<.+?>','',html)
print(ret)

#split函数：分割字符串，返回列表
try:
    test = "apple's price is $299，orange's price is $199"
    ret = re.split(' ',test)#
    print(ret)
except AttributeError:
    print("No")

#compile函数：编译正则表达式,可指定flag = re.VERBOSE添加注释，便于复习
try:
    test = "the number is 20.30"
    # r = re.compile('\d+\.?\d*')
    r = re.compile(r"""
        \d+ #小数点前
        \.? #小数点本身
        \d* #小数点后 
""",re.VERBOSE)
    ret = re.search(r,test)#
    print(ret)
except AttributeError:
    print("No")