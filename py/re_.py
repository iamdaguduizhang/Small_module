# -*- coding:utf-8 -*-
# @Time   : 2020/1/3 14:52
# @Author : Dg

import re

a = """
<script>
adsfsdtff
</script>
ewrsdf
</script>
"""
r = re.compile(r"<script>(.*)</script>", re.S,)
resule = r.findall(a)[0]
print(resule)