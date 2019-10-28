# -*- coding:utf-8 -*-
# @Time   : 2019/10/21 10:52
# @Author : Dg


def count(a):
    if a > 100:
        raise Exception, "Too Big"


try:
    count(101)
except Exception as e:
    print (e)
