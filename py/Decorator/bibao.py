# -*- coding:utf-8 -*-
# @Time   : 2019/12/11 17:32


def out(a):
    b = 10

    def inn():
        print(id(a), id(b))  # 使用闭包的过程中，一旦外函数被调用一次返回了内函数的引用，虽然每次调用内函
        # 数是开启一个函数执行过后消亡，但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量 id(b) 不变
        print(a + b)
        return

    return inn


demp1 = out(5)
demo2 = out(7)
print(demp1())
print(demo2())
# 在python3中，可以用nonlocal 关键字声明 一个变量， 表示这个变量不是局部变量空间的变量，需要向上一层变量空间找这个变量。
# 闭包可以用来实现装饰器，用来实现单列模式。