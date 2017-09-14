# encoding:utf-8
# 服务器端配置信息
import socket
name = socket.getfqdn(socket.gethostname())
ip = socket.gethostbyname(name)

configs = {
    'Hostid': ip,
    'Serverip': 'localhost',
    'Serverport': 9092,
    'urls': {
        # 'get_configs': ['api/config', 'get'],
        # 'service_report': [('api/mem', 'post'), ('api/cpu', 'post')]
        'service_report': [
            {
                'service_name': 'api/mem',
                'type': 'post',
                'monitor_interval': 300  # 5mins as default
            },
            {
            	'service_name':'api/cpu',
            	'type':'post',
            	'monitor_interval': 300 # 5 mins as default
            }
        ]
    },
    'Requesttimeout': 30,
    'ConfigUpdateInterval': 300  # 5 mins as default
}

# print configs.get('Hostid')
