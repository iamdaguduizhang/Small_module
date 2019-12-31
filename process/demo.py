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

    p2.daemon = True  # deamon属性默认为False,True的时候进程随主进程的结束而结束。 因为p1执行结束后，p2还要执行一秒，但是在这一秒之前
    # 主进程已经执行完毕了,所以p2就随之结束了,就不会有打印了.
    p1.start()  # 进程start 就会开始运行， 4个start就相当与已经有四个并发的进程了。
    p2.start()
    p3.start()
    p4.start()
    p1.join()  # join方法，让主进程阻塞，直到该进程执行结束。 因为p1阻塞主进程，所以p1的打印在主进程的打印之前
    # p1.join()#  而且在主主进程打印之前p1就执行结束了，所以p1的存货状态是False
    print(1, p1.is_alive())
    print(2, p2.is_alive())
    print(3, p3.is_alive())
    print('主线程')

    # https://www.cnblogs.com/hwlong/p/8952510.html

# from multiprocessing import Process
# def aa():
#     pass
#
# p1 = Process(target=aa, args=())
# p1 = Process(target=aa, args=())
# p1 = Process(target=aa, args=())
# p1 = Process(target=aa, args=())
