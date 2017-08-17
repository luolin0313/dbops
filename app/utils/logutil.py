# encoding:utf-8
# 记录log信息到文件中


import logging
import logging.handlers
import sys
import os

# base_dir = os.path.dirname(os.path.abspath(__file__))

basedir = os.path.dirname(os.path.abspath(__file__)).split('utils')[0]
log_home = os.path.join(basedir, 'log', 'stdout.log')
# print basedir, log_home


def write_log(log_name):
    log_file = log_home
    log_level = logging.DEBUG

    # 定义日志格式
    log_format = logging.Formatter(
        '%(asctime)s %(filename)s [line:%(lineno)2d]-%(funcName)s %(levelname)s %(levelname)s %(message)s')
    fh = logging.handlers.RotatingFileHandler(
        log_file, mode='a', maxBytes=1024 * 1024 * 10, backupCount=5)
    fh.setFormatter(log_format)

    # 实例化日志对象
    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)

    # 每调用一次就会添加一个logger.handler,每次就额外多打印一次日志，if判断使其只调用一次
    if not logger.handlers:
        logger.addHandler(fh)

    return logger




'''
 该日志调用方法
 logutil.py 上级目录，创建test.py文件测试

 from utils import logutil

 logutl.write_log('名称').info('info:%s' %msg)
 

'''