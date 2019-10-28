# -*- coding:utf-8 -*-
# @Time    :2019-10-16 17:33
# @Author  :Dg

import threading

n = 0


def foo():
    global n
    for x in range(10000):
        n += 1


threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)
