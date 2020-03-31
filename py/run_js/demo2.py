# -*- coding:utf-8 -*-
# @Time   : 2019/12/31 10:23
# @Author : Dg
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# js写入文件中，只是多了一步读取而已
# import PyV8
# ctxt = PyV8.JSContext()
# ctxt.enter()
#
# with open("test1.js", "r") as fp:
#     a = fp.read()
# func = ctxt.eval(a)  # 直接执行js函数
# print(func())

import js2py


def get_sign(user_id):
    print(u"用户id 为：", user_id)
    try:
        ec = js2py.EvalJs()
        with open("test2.js", "r") as fp:
            fin_js = fp.read()

        # print(fin_js)
        ec.execute(fin_js)
        signature = ec.test()
        # print(signature)
        return signature
    except Exception as e:
        print(e)
        return ""
print get_sign('111')