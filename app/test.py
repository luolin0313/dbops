# encoding:utf-8

import time
from utils import logutil

from flask import Flask
try:
    1 / 0
except Exception, e:
    # print e
    logutil.write_log('db').info("error:%s" % e)

# def time_consumer():
#     def timess(func):
#         start = time.time()
#         func()
#         end = time.time()
#         print '用时:%.3fs' % (end - start)
#         return
#     return timess


# @time_consumer()
# def x():
#     for i in range(10):
#         print 'i:%s' % i
