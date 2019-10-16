# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 16:54
# @Author : Dg

import time
import random
import os
from multiprocessing import Process, JoinableQueue, Queue


def consumer(q):
    while True:
        # if q.empty(): break
        res = q.get()
        print(res)
        if not res: break
        time.sleep(random.random())
        print('\033[45m%s 吃 %s\033[0m' %( os.getpid(), res))
        q.task_done()


def producer(q):
    for i in range(3):
        time.sleep(random.random())
        res = '包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))
    q.join()


if __name__ == '__main__':
    q = JoinableQueue()
    # q = Queue()
    # 生产者们:即厨师们
    p1 = Process(target=producer,args=(q,))

    # 消费者们:即吃货们
    c1 = Process(target=consumer,args=(q,))
    c1.daemon = True
    # c1 是怎么跳出while呢， q.join()阻塞这生产者进程（目的是为了让消费者完成消费），是通过task_done，
    # 直到队列中的每个项目均调用此方法之后，便不再阻塞。然后主进程得以执行，执行结束，消费者进程随之结束。c1跳出while

    # 开始
    p1.start()
    c1.start()

    p1.join()
    print('主')

