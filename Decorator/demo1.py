# -*- coding:utf-8 -*-
# @Time    :2019/11/26 5:55 下午
# @Author  :Dg
import logging


# def d_sayname(fn):
#     def wapper(*l, **d):
#         print (fn.__name__)
#         return fn(*l, **d)
#     return wapper
#
#
# @d_sayname
# def say():
#     print("hello")
#
# say()

def use_logging(func):

    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args)
    return wrapper


@use_logging
def bar():
    print("i am bar")


bar()
