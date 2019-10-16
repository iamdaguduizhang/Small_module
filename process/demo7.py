# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 17:26
# @Author : Dg

from multiprocessing import Manager, Process, Lock
import os

m = 0


def work(n, lock=None):
    # with lock: #不加锁而操作共享的数据,肯定会出现数据错乱
    global m
    m += 1
    print(m)


if __name__ == '__main__':
    lock = Lock()
    p_l = []
    n = 0
    for i in range(10):
        p = Process(target=work, args=(n, ))
        p_l.append(p)
        p.start()
    for p in p_l:
        p.join()
    print(m)
    #{'count': 94}

