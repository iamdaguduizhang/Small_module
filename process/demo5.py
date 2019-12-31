# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 11:49
# @Author : Dg

from multiprocessing import Process, Lock
import os
import time


def work(lock):
    # lock.acquire()  # 加锁牺牲了效率，这和单进程效率
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())
    # lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock, ))
        p.start()

    # 加锁可以保证多个进程修改同一块数据时，同一时间只能有一个任务可以进行修改，即串行的修改，没错，速度是慢了，但牺牲了速度却保证了数据安全。
    # 虽然可以用文件共享数据实现进程间通信，但问题是：
    # 1.
    # 效率低（共享数据基于文件，而文件是硬盘上的数据）
    # 2.
    # 需要自己加锁处理

    # 因此我们最好找寻一种解决方案能够兼顾：1、效率高（多个进程共享一块内存的数据）2、帮我们处理好锁问题。这就是mutiprocessing模块为我们提供的基于消息的IPC通信机制：队列和管道。
    # 1
    # 队列和管道都是将数据存放于内存中
    # 2
    # 队列又是基于（管道 + 锁）实现的，可以让我们从复杂的锁问题中解脱出来，
    # 我们应该尽量避免使用共享数据，尽可能使用消息传递和队列，避免处理复杂的同步和锁问题，而且在进程数目增多时，往往可以获得更好的可获展性。