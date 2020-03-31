# -*- coding:utf-8 -*-
# @Time   : 2019/10/10 11:06
# @Author : Dg
import os
import time
import random
from multiprocessing import Process


class MyProcess(Process):

    def __init__(self, name, data=None):
        super().__init__()  # 执行父类的构造函数，使得我们能够调用父类的属性。
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
if __name__ == "1__main__":  # super().__init__ test
    class A(object):
        def __init__(self):
            self.name = "aa"
            print ("this is A 实例化")

        def run(self):
            print("this is A.run")

    class B(A):
        def __init__(self):
            super().__init__()
            self.name_b = 'bb'
            print("this is B 实例化")
    b = B()
    b.run()
    print(b.name)
