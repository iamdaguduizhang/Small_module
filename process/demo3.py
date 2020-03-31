# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 11:20
# @Author : Dg
import os
import time
from multiprocessing import Process, Queue
n = 100  # 在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
a = Queue()
a.put(1)
a.put(2)
a.put(2)
b = [1,2,3]


def work(n, b):

    print(n)
    n = 0
    # print('子进程内: ', id(n), a.get(), id(a), "线程id", os.getpid())
    b.append(4)
    print(b)
    print(n)


def mycallback(x):
    list1.append(x)


if __name__ == '__main__':
    p = Process(target=work, args=(n, b))  # 疑问，为什么子进程的参数的id是一样的。a.get() 取的值也是一样的
    p.start()
    print(b)
    # time.sleep(3)
    p2 = Process(target=work, args=(n, b))
    p.join()
    p2.start()
    print('主进程内: ', id(n), a.get(),id(a))
    print(b)
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
# python 向函数传递参数的时候，如果传递的是可变的对象，那么传递的就是可变对象的引用，在函数内对对象的操作
# 影响了原来的对象的值。 但是如果在函数内部变量进行新的赋值操作，那么原来的变量，就停留在修改之前。
