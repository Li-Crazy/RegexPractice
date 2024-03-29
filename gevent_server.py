'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/28 21:27
@Software: PyCharm
@File    : gevent_server.py
'''
import gevent
from gevent import monkey
# 在导入socket前执行，改变socket的阻塞状态
monkey.patch_all()
from socket import *
from time import ctime

def server(port):
    s = socket()
    s.bind(('0.0.0.0',port))
    s.listen(5)

    while True:
        c,addr = s.accept()
        print("Connect from ",addr)
        gevent.spawn(handler,c)

def handler(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print("Recv:",data)
        c.send(ctime().encode())
    c.close()

if __name__ == '__main__':
    server(8080)