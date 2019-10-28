# -*- coding:utf-8 -*-
# @Time   : 2019/10/21 11:19
# @Author : Dg


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()  # generator
print(next(g))  # 执行一次，将4返回，但是res并没有给赋值
print("*"*20)
print(next(g))
print(g.send(10))  # next的加枪版，给res传了值
