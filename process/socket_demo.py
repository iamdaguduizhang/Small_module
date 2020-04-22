# -*- coding:utf-8 -*-
# @Time    :2020/4/11 2:00 下午
# @Author  :Dg
import os
from socket import *
from multiprocessing import Pool

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_USELOOPBACK, 1)
server.bind(('127.0.0.1', 10000))
server.listen(5)


def talk(conn,  client_addr):
    print('进程pid: %s' % os.getpid(), client_addr)
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break
            print('《=====', msg)
            a = 'hi'
            print(a)
            conn.send(a.encode('utf-8'))
            print('send..')
        except Exception as e:
            print(e)
            # break


if __name__ == '__main__':
    p=Pool()
    while True:
        print("===")
        conn,client_addr = server.accept()
        p.apply_async(talk, args=(conn, client_addr))
        # p.apply(talk,args=(conn,client_addr)) #同步的话，则同一时间只有一个客户端能访问