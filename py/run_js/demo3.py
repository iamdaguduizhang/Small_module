# -*- coding:utf-8 -*-
# @Time   : 2019/12/31 10:36
# @Author : Dg
# 获得console 的值
from subprocess import Popen, PIPE

script = '''
console.log('hi');
'''

p = Popen(['node'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
out, err = p.communicate(script)
print(out)
