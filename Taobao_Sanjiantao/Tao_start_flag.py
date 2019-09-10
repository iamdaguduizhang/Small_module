# -*- coding: utf-8 -*-
import time
import redis

# while 1:
#     time.sleep(1)
#     a = time.time()
#     print int(a * 1000)
#     if int(a * 1000) == 1553853750000:
#         print 'aaaa'
r = redis.Redis(host='116.255.163.127', port=6379, password='BDVxnhaTmYl0w42o')

# time.sleep(10000)
# while 1:
# time.sleep(43200)
# for x in range(30):
#     r.set('pc_flag', 2)
#     time.sleep(600)
#
# time.sleep(43200)
# for x in range(60):
#     r.set('pc_flag', 2)
#     time.sleep(600)
r.set('pc_flag', 2)
# time.sleep(32400)
# print task_lt[101]