# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 11:20
# @Author : Dg

from multiprocessing import Process, Queue
n = 100  # 在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
a = Queue()
a.put(1)
a.put(2)


def work():
    global n
    n = 0
    print('子进程内: ', n, a.get())


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    print('主进程内: ', n, a.get())

    # 主进程内:  100
    # 子进程内:  0
    # 进程直接的内存空间是隔离的