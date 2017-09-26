# encoding:utf-8
# 接收client端传递的数据 然后入库
import sys
sys.path.insert(0, '..')
import json
from flask import Flask, render_template, Blueprint, request
from app import models, db
# from app.models import Hw_mem
api = Blueprint('api', __name__)


@api.route('/mem', methods=['POST'])
def mem():
    # 硬件api
    # 拼接入库字段
    # obj = dict(
    #     host_ip=request.args.get('host_ip', None),
    #     mem_ava=request.args.get('mem_ava', None),
    #     insert_time=request.args.get('insert_time', None)
    # )

    mem_ava =  json.loads(request.form.get('data'))['mem_ava']
    insert_time = json.loads(request.form.get('data'))['insert_time']
    client_ip = str(request.form.get('client_ip'))
    # print mem_ava,insert_time,client_ip
    mem = models.Hw_mem(host_ip=client_ip,
                        mem_ava=mem_ava,
                        insert_time=insert_time
                        )
    db.session.add(mem)
    db.session.commit()
    return json.dumps({'mem':0,'code': 0})

@api.route('/cpu',methods=['POST'])
def cpu():
    # cpu状态数据入库

    return json.dumps({'cpu':0,'code':0})
'''
测试内存收集方法
create table hw_mem(
id int(11) unsigned not null auto_increment,
host_ip varchar(15) not null default '' comment '被监控的IP',
mem_ava int(11) unsigned not null default 0 comment 'available memory',
insert_time int(11) unsigned not null default 0 comment '入库时间',
primary key(id),
key idx_time (insert_time)
)engine=innodb default charset=utf8;

 # cpu 使用率
create table cpu_info(
id int(11) unsigned not null auto_increment,
host_ip varchar(15) not null default '' comment 'client ip',
cpu_used int(11) unsigned not null default 0 comment 'cpu used%',
insert_time int(11) unsigned not null default 0 comment '统计时间',
primary key(id),
key idx_time(insert_time)
)engine=innodb default charset=utf8;

# disk 读写率
create table io_rw_info(
id int(11) unsigned not null auto_increment,
host_ip varchar(15) not null default '' comment 'client ip',
mount_point varchar(15) not null default '' comment '分区名称',
read_io int(11) unsigned not null default 0 comment '磁盘io读字节',
write_io int(11) unsigned not null default 0 comment '磁盘io写字节',
insert_time int(11) unsigned not null default 0 comment '统计时间',
primary key(id),
key idx_time(insert_time)
)engine=innodb default charset=utf8;

# network recv/send byte
create table network_info(
id int(11) unsigned not null auto_increment,
host_ip varchar(15) not null default '' comment 'client ip',
net_recv int(11) unsigned not null default 0 comment '接收网络byte',
net_send int(11) unsigned not null default 0 comment '发送网络byte',
insert_time int(11) unsigned not null default 0 comment '统计时间',
primary key(id),
key idx_time(insert_time)
)engine=innodb default charset=utf8;
'''
