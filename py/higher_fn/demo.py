# -*- coding:utf-8 -*-
# @Time   : 2019/12/31 16:59
# @Author : Dg
# 几个高阶函数的简单复习


def big_than_10(x):
    if x > 10:
        return True
    else:
        return False


result = map(big_than_10, (1, 2, 3, 18,))  # 返回列表
print(result, type(result))


def fn(x, y):
    return x * 10 + y


r_ = reduce(fn, [1, 2, 3])
print(r_, type(r_))


def is_o(x):
    return int(x) % 2 ==0


f_ = filter(is_o, "1234")  # 可迭代对象是什么类型就返回什么类型
print(f_, type(f_))


lt = [1, 3, 2, 5]
lt2 = sorted(lt)
print(lt, lt2)

lt3 = sorted(lt, reverse=True)
print(lt3)

dict_ = {1: 2, 3: 1, 2: 3, 4: 0}
print(dict_.items())
dict2 = sorted(dict_.items(), key=lambda x: x[0])
print(dict2)
