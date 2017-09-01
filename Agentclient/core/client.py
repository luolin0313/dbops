# encoding:utf-8

# import time
import os
import sys
sys.path.insert(0, '..')
# sys.path.insert(
#     0, 'E:\python_training\env\Lib\site-packages\/requests-2.18.2-py2.7.egg')
sys.path.insert(
    0, 'E:\python_training\env\lib\site-packages\/requests-2.18.2-py2.7.egg')
sys.path.insert(0, 'e:\python_training\env\lib\site-packages\urllib3-1.22-py2.7.egg')
sys.path.insert(
    0, 'e:\python_training\env\lib\site-packages\chardet-3.0.4-py2.7.egg')
sys.path.insert(
    0, 'e:\python_training\env\lib\site-packages\certifi-2017.7.27.1-py2.7.egg')
sys.path.insert(
    0, 'e:\python_training\env\lib\site-packages\idna-2.5-py2.7.egg')
# e:\python_training\env\lib\site-packages\certifi-2017.7.27.1-py2.7.egg
from conf import settings
import requests
import json
import threading


class ClientHandle:
    def __init__(self):
        self.monitored_services = {}

    def load_latest_config(self):
        '''
        从监控服务器中加载最新的监控配置
        '''
        request_type = settings.configs['urls']['get_configs'][1]
        url = "%s/%s" % (settings.configs['urls']
                         ['get_configs'][0], settings.configs['Hostid'])
        latest_configs = self.url_request(request_type, url)
        # latest_configs = json.loads(latest_configs)
        # self.monitored_services.update(latest_configs)

        # print monitored_services
        print request_type, url

    def forever_run(self):
        '''
        永久开启client
        '''
        pass

    def url_request(self, request_type, url):
        pass


# cc = ClientHandle()
# cc.load_latest_config()

# print settings.configs.get('Hostid')
