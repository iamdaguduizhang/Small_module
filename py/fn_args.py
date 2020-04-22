# -*- coding:utf-8 -*-
# @Time    :2020/4/16 10:56 上午
# @Author  :Dg
import sys
import time


# def test(a=[]):
#     print(id(a))
#     a.append('1')
#     print(id(a))
#     return a, id(a)
#
# print(test())
# print(test())
#
# def test2(a='abc'):
#     print(id(a))
#     a = a + 'b'
#     print(id(a))
#     return a
#
# print(test2())
# print(test2())
# test2() 中打印的第二个a的id是一样的，说明第一次调用函数时给 a赋值 a=a+'b'后在函数执行之后'adcb'并没有被销毁
# 第二次调用得到值'adcb'发现内存中有此值，就将其引用，所以id才会一样？

# python 的回收机制

a = 'a'
print(id(a))
# print(sys.getrefcount('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'))
# print(sys.getrefcount(1))


del a
# print(sys.getrefcount('abcsdfsfsf'))

# print(locals())
c = 'a'

print(id(c))
# print(a is c)  # 这样的结果和在ipython中的不一样，最开始想法（python运行前变成字节码，字节码中都有引用 然后del a 的时候 c还是有引用的）
# 但del a应该也在字节码中啊，感觉有别的东西

a = object()
print(id(a))
del a
b = object()
print(id(b))