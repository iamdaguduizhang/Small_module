# -*- coding:utf-8 -*-

from Chrom import MyChrom

if __name__ == '__main__':
    chrom = MyChrom()
    url = 'https://www.zhihu.com/signup?next=%2F'
    cookie = chrom.get_noheadless_cookie(url, 35,)
    chrom.use_cookie(url, )