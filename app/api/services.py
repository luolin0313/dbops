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
    mem = models.Hw_mem(host_ip=request.json.get('host_ip'),
                        mem_ava=request.json.get('mem_ava'),
                        insert_time=request.json.get('insert_time')
                        )
    db.session.add(mem)
    db.session.commit()
    return json.dumps({'code': 0})


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
'''
