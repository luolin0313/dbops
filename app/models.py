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
