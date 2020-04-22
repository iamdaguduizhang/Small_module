# -*- coding:utf-8 -*-
# @Time    :2020/4/10 11:07 上午
# @Author  :Dg
import random
import time

import redis

#  维持100个可用的ip， ip可用性用一个数值表示（初始为10，小于6的就淘汰掉）。一个ip请求失败-1
import requests, threading

# r = redis.Redis(host='116.255.163', port=6379, password='000')
pool = redis.ConnectionPool(host='116.255.163', port=6379, password='0')
r = redis.Redis(connection_pool=pool)
r.h
index = str(random.randint(0, 10))
# r.hset('IP_pool', '2', '{"1.1.1.2:3128":"10"}')
# ip = eval(r.hget('IP_pool', index))
# ip = ip.keys()[0]
# value = ip.values()[0]
# print(r.hgetall("IP_pool"), len(r.hgetall("IP_pool").keys()))


def get_ip():
    ip_dict = r.hgetall("IP_pool")
    index = random.choice(ip_dict.keys())
    ip = ip_dict.get(str(index))
    print(ip)
    return [ip, str(index)]


def add_ip2pool():
    index = random.randint(0, 100)
    r.hset('IP_pool', str(index), '{"1.1.1.2:3128":"10"}')


def del_num(ip):
    dict_ip = eval(ip)
    dict_ = {}
    key = dict_ip.keys()[0]
    value = str(int(dict_ip.values()[0]) - 1)
    dict_[key] = value
    return str(dict_)


def ip_check():
    ip, index = get_ip()
    # index =
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Upgrade-Insecure-Requests':'1'
    }

    proxies = {
        "http": "http://" + ip,
        "https": "https://" + ip
    }
    # response = requests.get('https://www.baidu.com', headers=headers, proxies=proxies)

    # if response.status_code == 200:
    #     return True
    # else:
    #     return False
    a = [1, 0]
    print("检测ip 可用性中")
    time.sleep(1)
    if not random.choice(a):
        print("不可用，系数减一{}".format(index))
        ip = del_num(ip)
        r.hset("IP_pool", index, ip)
    return random.choice(a)


def ip_num_check():

    # print("检测ip 可用数量中")
    time.sleep(1)
    ip_num = len(r.hgetall("IP_pool").keys())
    print("检测ip 可用数量中,数量为{}".format(ip_num))
    while ip_num < 5:
        add_ip2pool()
        ip_num += 1


a = threading.Thread(target=ip_check)

b = threading.Thread(target=ip_num_check)

# while 1
print(r.hgetall("IP_pool"))

a.start()
a.join()
# print(r.hgetall("IP_pool"))
b.start()
b.join()
print(r.hgetall("IP_pool"))
