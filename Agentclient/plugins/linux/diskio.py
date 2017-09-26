#encoding:utf-8

import  psutil

import psutil
import time

def disk_io_rw():
    #磁盘io读写字节单位KB
    #[read_byte,write_byte]
    disk_io_rw = {'insert_time':time.time()}
    data = psutil.disk_io_counters(perdisk=True)
    for k,v in data.items():
        disk_io_rw.setdefault(k,[v[2]/1024,v[3]/1024])
    return disk_io_rw


while True:
    print disk_io_rw()
    time.sleep(60)
