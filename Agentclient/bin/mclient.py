# encoding:utf-8

import sys
import os

# base_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(base_dir)
sys.path.insert(0, '..')
from core import main

if __name__ == '__main__':
    client = main.command_handler(sys.argv)
