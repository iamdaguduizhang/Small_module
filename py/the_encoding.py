#coding=utf-8

s = "小"

print(s.decode(encoding='utf-8'), type(s.decode(encoding='utf-8')))
print(s.decode(encoding='utf-8').encode(encoding='utf-8'), type(s.decode(encoding='utf-8').encode(encoding='utf-8')) )
# (u'\u5c0f\u7532', <type 'unicode'>)
# ('\xe5\xb0\x8f\xe7\x94\xb2', <type 'str'>)
# 11100101   10110000  10001111  \xe5\xb0\x8f   这里是utf-8形式表现的unicode（规则如下）
# 1011100    00001111   \u5c0f    23567    这里是unicode码表中的表示 2个字节

# unicode               utf-8 形式的unicode
# 1011100 00001111 == 11100101 10110000 10001111==》\xe5\xb0\x8f

