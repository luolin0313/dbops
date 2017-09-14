# encoding:utf-8
# mem resource
import sys
import os
# base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '..')
base_dir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.getcwd()))))
# print base_dir
p_conf = os.path.join(base_dir, '\python_training\env\lib\site-packages')
sys.path.insert(0, p_conf)
sys.path.insert(
    0, 'E:\python_training\env\lib\site-packages\\flask_restful-0.3.6-py2.7.egg')
sys.path.insert(
    0, 'E:\python_training\env\lib\site-packages\\flask-0.12.2-py2.7.egg')
sys.path.insert(
    0, 'E:\python_training\env\lib\site-packages\\flask-0.12.2-py2.7.egg\\flask')
from flask import Flask
