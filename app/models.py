# encoding:utf-8
# 模型类 数据库中的一张张表

from flask import current_app
from app import db
from datetime import datetime


class User(db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True)
    password = db.Column(db.String(40))
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, username, password, create_time, modify_time):
        self.username = username
        self.password = password
        self.create_time = create_time
        self.modify_time = modify_time

    def __repr__(self):
        return '<User %r %r %r %r>' % (self.id, self.username, self.create_time, self.update_time)


class Hw_mem(db.Model):
    # 测试内存收集方法 restful api
    __tablename__ = 'hw_mem'
    id = db.Column(db.Integer, primary_key=True)
    host_ip = db.Column(db.String(15), nullable=False)
    mem_ava = db.Column(db.Integer, nullable=False)
    insert_time = db.Column(db.Integer, index=True)

    def __init__(self, host_ip, mem_ava, insert_time):
        self.host_ip = host_ip
        self.mem_ava = mem_ava
        self.insert_time = insert_time

    def __repr__(self):
        return '<Hw_mem %r %r %r %r' % (self.id, self.host_ip, self.mem_ava, self.insert_time)
