# -*- coding:utf-8 -*-
# @Time   : 2019/12/31 17:58
# @Author : Dg
# 深浅拷贝，区别就在于对于深层元素(除第一层)，深拷贝的话是重新创建的，浅拷贝只是添加了引用，修改对象的值会影响所有引用其对象的变量。
import copy

a = [1, 2, 3, [1,2,3]]
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a), id(b), id(c))