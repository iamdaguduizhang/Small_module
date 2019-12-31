# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 11:20
# @Author : Dg

from multiprocessing import Process, Queue
n = 100  # 在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
a = Queue()
a.put(1)
a.put(2)
a.put(2)


def work():

    global n
    print(n)
    n = 0
    print('子进程内: ', id(n), a.get())
    print(n)


from multiprocessing import Pool
import time


def mycallback(x):
    list1.append(x)


def sayHi(num):
    return num


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    p2 = Process(target=work)
    p2.start()
    print('主进程内: ', id(n), a.get())
    # print(n)

    # 主进程内:  100
    # 子进程内:  0
    # 进程直接的内存空间是隔离的
    # pool = Pool(4)
    list1 = []
    # for i in range(4):
    #     pool.apply_async(sayHi, (i,), callback=mycallback)
    #     # print(x)
    # pool.close()
    # pool.join()
    #
    # print(list1)
