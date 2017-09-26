# encoding:utf-8

from linux import memory,cpu
import time


def mem():
    return memory.monitor()



def get_cpu_status():
    return  cpu.cpu_stats()

# if __name__ == '__main__':
#     while True:
#         # print mem()
#         print  get_cpu_status()
#         time.sleep(1)

