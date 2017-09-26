# encoding:utf-8
import sys
sys.path.insert(
    0, 'e:\python_training\env\lib\site-packages\psutil-5.2.2-py2.7-win32.egg')
import psutil
import time


def monitor():
    mem = psutil.virtual_memory().available
    mem_mb = mem * 1.0 / (1024 * 1024)
    dt = int(time.time())

    obj = {'mem_ava': mem_mb, 'insert_time': dt}
    return obj
