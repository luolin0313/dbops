# encoding:utf-8

import sys
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

sys.path.insert(0, '..')
from core import main

if __name__ == '__main__':
    client = main.command_handler(sys.argv)
    # print client
