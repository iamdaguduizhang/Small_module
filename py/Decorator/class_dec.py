# -*- coding:utf-8 -*-
# @Time   : 2019/12/12 10:59
# @Author : Dg


class Dec(object):
    def __init__(self, fun):
        print('111')
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print('hhh')
        self.fun(*args, **kwargs)
        print('ppp')


# @Dec
def fn(a):
    print('oooo' + a)
# fn('p')


fn = Dec(fn)  # __call__ 在init 之后执行
fn('p')
