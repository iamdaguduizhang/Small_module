# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 11:06
# @Author : Dg
import os
import time
import random
from multiprocessing import Process


class MyProcess(Process):

    def __init__(self, name, data=None):
        super().__init__()  #
        self.name = name
        self.data = data

    def run(self):
        time.sleep(self.data)
        print('im child', os.getpid(), os.getppid())
        print('睡了{}秒'.format(self.data))


if __name__ == "__main__":
    p1 = MyProcess('aaa', 1)
    p2 = MyProcess('bbb', 2)
    p3 = MyProcess('ccc', 3)
    p4 = MyProcess('ddd', 4)

    p1.start()  # start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    print('主线程')

# class myProcess(Process):
#
#     def __init__(self, name, data=None, *args):
#         self.name = name
#         self.data = data
#         self.args = args
#
#     def run(self):
#         print(self.data)
#         for x in self.args:
#             print(x)