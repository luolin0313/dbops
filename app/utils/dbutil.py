# encoding:utf-8
import os
import sys
sys.path.insert(0, '..')
# print sys.path
from models import User


def listapi():
    data = User.query.all()
    return data
