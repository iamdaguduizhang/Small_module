# -*- coding:utf-8 -*-
# @Time    :2020/4/11 3:03 下午
# @Author  :Dg
import datetime
import threading
import time


def work(t):
    time.sleep(t)


a = threading.Thread(target=work, args=(3,))
b = threading.Thread(target=work, args=(3,))

print(datetime.datetime.now())
a.start()
b.start()
a.join()
print(datetime.datetime.now())
