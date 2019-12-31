# -*- coding:utf-8 -*-
# @Time    :2019/11/27 9:43 上午
# @Author  :Dg

from multiprocessing import Process, JoinableQueue


def custom(q):
    while 1:
        print("消费者消费{}".format(q.get()))
        q.task_done()


def produce(q):
    for x in range(4):
        q.put(x)
        print("生产者生产{}".format(x))
    q.join()


if __name__ == "__main__":
    q = JoinableQueue()
    c = Process(target=custom, args=(q, ))
    p = Process(target=produce, args=(q, ))
    c.daemon = True
    c.start()
    p.start()
    p.join()
