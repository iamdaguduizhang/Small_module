# -*- coding:utf-8 -*-
# @Time   : 2019/12/31 10:00
# @Author : Dg
# 直接在python代码中执行js代码并获取返回值
import PyV8
ctxt = PyV8.JSContext()
ctxt.enter()
func = ctxt.eval("""
(function(){
return "hello js2";
})
""")  # 直接执行js函数
print(func())
