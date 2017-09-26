#encoding:utf-8

import  psutil
import  time

def get_network_status():
    dt = time.time()
    net_recv = list(psutil.net_io_counters())[1]/1024
    net_send = list(psutil.net_io_counters())[0]/1024

    net = {'net_recv':net_recv,'net_send':net_send,'insert_time':dt}
    return  net

# while True:
#     print get_network_status()
#     time.sleep(60)
