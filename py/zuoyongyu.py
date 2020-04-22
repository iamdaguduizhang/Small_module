# -*- coding:utf-8 -*-
# @Time   : 2019/12/11 18:03
# @Author : Dg
import threading


def num():
    lt = []
    i = 10
    for i in range(4):

        def a(x):
            # print(i)
            return(x * i)
        lt.append(a)
    print(u"num 中I 的值为",str(i))
    return lt


# print(num())
for x in num():
    print(x(3))
# python 中，函数不执行的话，就是一个引用而已，函数的名字 对应的指向函数代码块的内存地址。
# 在向lt中添加a的时候，只是添加了函数a的的代码块的引用。 然后在print语句中牵扯到了执行，执行的时候a函数作用域咩有i，
# 所以要向上一层去找i， 找的时候 num()函数是执行结束的，所以内部的for循环也是执行结束的，所以只能找到最后的i 也就是3.
# 当lt中的函数未执行时，只是四个引用，执行的时候才去获取值运行，x是传递的参数。i要通过作用域去寻值


# 当一个函数被另一个模块引用时，如果该函数有使用到自己模块内的全局变量时.
# 模块间变量的调用。https://punchagan.muse-amuse.in/blog/python-globals/

test_a = 4
def test():
    print("====1"  # 错误时只能将这里打印出来。python代码在执行前首先会被编译成字节码，这就会导致某些时候实际执行的程序会和我们看到的产生出入。
    print(test_a)  # 打印可以但是不能赋值，如果未加说明而在函数内对一个变量赋值，那么就认为你定义了一个局部变量，从而把外部的同名对象屏蔽了
    # b = test_a + 1  # 这样可以
    # test_a = 4
    print("====2")
    test_a = test_a + 1  # 这样不可以
    # print(b)

# test_a = [1,2,3]
# def test():
#     print(test_a)
#     test_a.append(4)  # 这样可以 这样的操作并没有产生辅助语句。
#                       # 可变对象与不可变对象改变时。可变对象内存地址发生了改变，不可变对象地址改变
#     print(test_a)


def test_2():
    # global test_a
    test_a = 5
    test()
test_2()


exit()
i = 0
def f():
  print(i)
  i += 1
  print(i)

f()
print(i)

# ==> UnboundLocalError: local variable 'i' referenced before assignment

# python对函数的代码是独立编译的，如果未加说明而在函数内对一个变量赋值，那么就认为你定义了一个局部变量，从而把外部的同名对象屏蔽了。
# 这么做无可厚非，毕竟python没有独立的声明一个局部变量的语法，但结果就会造成我们看到的类似暂时性死区的现象。https://www.cnblogs.com/apocelipes/p/10408836.html


# i = 0
# def f(i):
#   print(i)
#   i += 1
#   print(i)
#
# f(i)
# print(i)
# 0,1,0 python函数参数的传递，当对象为可变对象是传的是引用，不可变对象是传递的是值。

