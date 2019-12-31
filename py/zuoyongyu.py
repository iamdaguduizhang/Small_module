# -*- coding:utf-8 -*-
# @Time   : 2019/12/11 18:03
# @Author : Dg


def num():
    lt = []
    i = 10
    for i in range(4):

        def a(x):
            print(i)
            return(x * i)
        lt.append(a)
    return lt


# print(num())
print([x(2) for x in num()])
# python 中，函数不执行的话，就是一个引用而已，函数的名字 对应的指向函数代码块的内存地址。
# 在向lt中添加a的时候，只是添加了函数a的的代码块的引用。 然后在print语句中牵扯到了执行，执行的时候a函数作用域咩有i，
# 所以要向上一层去找i， 找的时候 num()函数是执行结束的，所以内部的for循环也是执行结束的，所以只能找到最后的i 也就是3.