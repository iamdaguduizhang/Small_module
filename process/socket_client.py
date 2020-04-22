# -*- coding:utf-8 -*-
# @Time    :2020/4/11 2:06 下午
# @Author  :Dg

from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',10000))


while True:
    msg=str(input('>>: ')).strip()
    if not msg:continue

    client.send(msg.encode('utf-8'))
    print(1)
    msg=client.recv(1024)
    print(2)
    print(msg.decode('utf-8'))