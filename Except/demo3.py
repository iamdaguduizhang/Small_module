# -*- coding:utf-8 -*-
# @Time   : 2019/10/21 10:55
# @Author : Dg


class Timeouterror(Exception):
    def __init__(self, arg):
        self.arg = arg


try:
    raise Timeouterror("Time out")

except Exception as e:
    print(e.arg)


def test(*a):
    for x in a:
        print(x)


def test2(**b):
    for k, v in b.items():
        print k, v


test2(x=1, y=2, c=3)
