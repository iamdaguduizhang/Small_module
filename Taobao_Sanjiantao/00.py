# -*- coding:utf-8 -*-
# @Time    :2019-06-25 10:46
# @Author  :Dg

import time

a = [1, 2, 3]
b = []

while 1:
    if len(a) > 0:
        c = a.pop()
        b.append(c)
        print c
    else:
        a.extend(b)
        # c = b[-1]
        # print c
        continue
    time.sleep(1)
