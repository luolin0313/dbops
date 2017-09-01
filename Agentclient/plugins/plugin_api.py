# encoding:utf-8

from linux import memory
import time


def get_linux_mem():
    return memory.monitor()


# if __name__ == '__main__':
#     while True:
#         get_linux_mem()
#         time.sleep(1)
