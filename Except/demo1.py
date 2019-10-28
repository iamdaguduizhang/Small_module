# -*- coding:utf-8 -*-
# @Time   : 2019/10/21 10:46
# @Author : Dg
try:
    print (1)
    try:
        print (a)
    except KeyError:
        print("未命名变量")
    else:
        print("No Except")
    finally:
        print("End")
except Exception as e:
    print("Wai")