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
        'get_configs': ['api/config', 'get'],
        'service_report': ['api/report/', 'post']
    },
    'Requesttimeout': 30,
    'ConfigUpdateInterval': 300  # 5 mins as default
}

# print configs.get('Hostid')
