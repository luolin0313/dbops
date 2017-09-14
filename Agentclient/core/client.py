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


class ClientHandle:
    def __init__(self):
        self.monitored_services = {}

    def load_latest_config(self):
        '''
        从监控服务器中加载最新的监控配置
        '''
        request_type = settings.configs['urls']['service_report']
        self.monitored_services['api_service'] = request_type
        return self.monitored_services

    def forever_run(self):
        '''
        永久开启client
        '''
        exit_flag = False
        config_last_update_time = 0
        while not exit_flag:
            if time.time() - config_last_update_time > settings.configs['ConfigUpdateInterval']:
                self.load_latest_config()
                # print "loaded lasted config:", self.monitored_services
                config_last_update_time = time.time()
            # 开始监控服务
            # {'api_service': [{'service_name': 'api/mem', 'type': 'post', 'monitor_interval': 300}]}
            service = self.load_latest_config()
            for x in service['api_service']:
                # print x.items()
                service_name = x.items()[0][1]
                monitor_interval = x.items()[2][1]
                # print monitor_interval
                last_invoke_time = 0
                if time.time() - last_invoke_time > monitor_interval:
                    # print "last_invoke_time:", time.time()
                    last_invoke_time = time.time()
                    t = threading.Thread(target=self.invoke_plugin, args=(
                        service_name, monitor_interval))
                    t.start()
                    print "开始监控 %s" % service_name
                else:
                    print "开始在 %s in %s secs 监控" % (service_name, monitor_interval - (time.time() - last_invoke_time))
            time.sleep(1)
            exit_flag = True

    def invoke_plugin(self, plugin_name, val):
        # if hasattr(plugin_api, plugin_name):
            # func = getattr(plugin_api, plugin_name)
            # plugin_callback = func()

            # report_data = {
            #     'client_id': settings.configs.get('Hostid')
            #     'data': json.dumps(plugin_callback)
            # }
        print plugin_name, val

    def url_request(self, request_type, url, **args_data):
        # pass
        # http://localhost:9092/api/mem?host_ip=192.168.137.12&mem_ava=128&insert_time=1484875998
        url_pre = "http://%s:%s/%s" % (settings.configs.get('Serverip'),
                                       settings.configs.get('Serverport'),
                                       'url')

        if request_type in ('get', 'GET'):
            print url_pre + 'get'
        elif request_type in ('post', 'POST'):
            # print url_pre + 'post'
            t = requests.post()


cc = ClientHandle()
print cc.forever_run()


# s = settings.configs['urls']['service_report']
# # s = {'api_service': [{'service_name': 'api/mem',
# #                       'type': 'post', 'monitor_interval': 300}]}
# for x in s:
#     print x.items()
