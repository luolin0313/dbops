#encoding:utf-8

import psutil
import time

def cpu_stats():
    cpu_used = psutil.cpu_percent(interval=1)
    return  cpu_used

# while True:
#     print cpu_stats()
#     time.sleep(60)