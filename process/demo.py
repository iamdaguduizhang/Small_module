# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 10:57
# @Author : Dg
import time
from multiprocessing import Process


def sleep(data):
    time.sleep(data)
    print("休息{}秒".format(data))


if __name__ == "__main__":
    p1 = Process(target=sleep, args=(1, ))
    p2 = Process(target=sleep, args=(2, ))
    p3 = Process(target=sleep, args=(3, ))
    p4 = Process(target=sleep, args=(4, ))

    p2.daemon = True  # deamon属性默认为False,True的时候进程随主进程的结束而结束。
    p1.start()  # 进程start 就会开始运行， 4个start就相当与已经有四个并发的进程了。
    p2.start()
    p3.start()
    p4.start()
    p1.join()  # join方法，让主进程阻塞，直到该进程执行结束。

    print(1, p1.is_alive())
    print(2, p2.is_alive())
    print(3, p3.is_alive())
    print('主线程')

    # https://www.cnblogs.com/hwlong/p/8952510.html
