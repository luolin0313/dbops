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
from plugins import plugin_api
import time
reload(sys)
sys.setdefaultencoding('utf-8')


class ClientHandle:
    def invoke_plugin(self):
        # 内存监控频率60秒
        while True:
            xx = plugin_api.mem()
            report_data = {
                'client_ip': settings.configs.get('Hostid'),
                'data': json.dumps(xx)
            }

            self.url_request(report_data)
            time.sleep(60)




    def url_request(self, args_data):
        # pass
        # # http://localhost:9092/api/mem?host_ip=192.168.137.12&mem_ava=128&insert_time=1484875998
        url_pre = "http://%s:%s/%s" % (settings.configs.get('Serverip'),
                                       settings.configs.get('Serverport'),
                                       settings.configs.get('urls')['service_report'][0]['service_name'])
        # print args_data, url_pre

        try:
            r = requests.post(url_pre, args_data)
            print r.json()
        except Exception as e:
            print e
