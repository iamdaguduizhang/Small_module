# -*- coding:utf-8 -*-
# @Time   : 2019/12/11 15:34
# @Author : Dg
# from functools import wraps


def fnname_dec(fn):
    # @wraps(fn)
    def wapper(*args, **kwargs):  # 为什么wapper 要接收参数呢。 因为被装饰后的函数其实就是wapper，
        # 然后要接受被装饰后的函数speak的参数供原来的speak函数使用来达到不影响原函数的功能。
        print("My name is " + fn.__name__)
        a = fn(*args, **kwargs)
        print ("原函数执行结束后在执行的事件")
        return a
    return wapper


# @fnname_dec
def speak(word):
    print("i say:" + word)
    return "speak"


if __name__ == "__main__":
    speak = fnname_dec(speak)  # 这句话的功能与@fanname_dec 这个语法糖是一样的。 当执行fnname_dec(speak)的时候，
    # 就像当于执行了wapper函数，因为fnname_dec 的返回值是wapper 是这个函数而不是某个值。
    speak("haha")  # 就相当于wapper("haha"), 而wapper的返回值是原来speak的返回值，并且在返回的时候执行了 speak()函数
    # 所以也就到达了不修改原来函数的情况下 给原有的函数增加了功能。
    print(speak.__name__)  # ==> wapper 其实现在的函数根本就是wapper函数，只是被赋予了原函数的名字而已
    # 由此可以看出,装饰器会对原函数的元信息进行更改,可以使用wraps,进行原函数信息的添加
    # wraps本身也是一个装饰器, 他能把函数的元信息拷贝到装饰器函数中使得装饰器函数与原函数有一样的元信息

