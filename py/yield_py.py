# -*- coding:utf-8 -*-
# @Time   : 2019/10/21 11:19
# @Author : Dg


# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)


# g = foo()  # generator
# print(next(g))  # 执行一次，将4返回，但是res并没有给赋值
# print("*"*20)
# print(next(g))
# print(g.send(10))  # next的加枪版，给res传了值
# print(next(g))

# iterator
import time

a = [1, 2]  # 可迭代对象 只有iter 没有 next，可迭代对象通过iter 可以得到一个迭代器
print(dir(a))  # 查看方法
b = a.__iter__()
print(b)  # 迭代器 既有__iter__ 还有next
print(b, type(b), dir(b))
print(b.next())  # 迭代器保存的是生成值的算法，而可迭代对象保存的是值. 所以迭代器比列表节省空间。


# **生成器函数：**常规函数定义，但是，使用yield语句而不是return语句返回结果。yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次从它离开的地方继续执行
# **生成器表达式：**类似于列表推导式，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表

gen_ = (x for x in range(5))
print(gen_)  # generator object


def gen_test():
    for x in range(5):
        d = yield x
        print(d, 999)


print(gen_test())  # generator object
gen = gen_test()
print(gen.next())
c = gen.send(6)  # 将6赋给了d. next 方法是单纯的取值，而send在取值的同时，还可以给yield 语句赋值。
# print(c)       # c的值是1. 这里的c应该叫返回值，但是d叫什么就不晓得了
print(gen.next())
print(gen.next())
print(gen.next())


def triangles():
    m = [1]
    while 1:
        yield m
        m = [1] + [m[x] + m[x+1] for x in range(len(m)-1)] + [1]
        # n = n - 1
        # if n <= 0:
        #     break


# 主函数
a = triangles()

for x in range(4):
    print(a.next())
    
# 利用yield 可以在返回值返回后利用返回值进行进一步操作。来获得下次的返回值


def feibo(n):
    a, b = 0, 1
    while n:
        yield b
        a, b = b, a+b
        n -= 1
        if n <= 0:
            break


a = feibo(6)
for x in a:
    print(x)