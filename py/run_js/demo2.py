# -*- coding:utf-8 -*-
# @Time   : 2019/12/31 10:23
# @Author : Dg
# js写入文件中，只是多了一步读取而已
import PyV8
ctxt = PyV8.JSContext()
ctxt.enter()

with open("test1.js", "r") as fp:
    a = fp.read()
func = ctxt.eval(a)  # 直接执行js函数
print(func())
