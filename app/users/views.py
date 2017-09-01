# encoding:utf-8
# 用户列表
import sys
sys.path.insert(0, '..')
# from utils import dbutil
import json
from flask import render_template, Blueprint, redirect, request, jsonify
from app.models import User


user_page = Blueprint('user_page', __name__)


@user_page.route('/userlist')
def userlist():
    res = User.query.all()
    return render_template('userlist.html', users=res)


@user_page.route('/useradd')
def useradd():
    return render_template('useradd.html')


@user_page.route('/userdel', methods=['POST'])
def userdel():
    # pass
    row_id = request.form.get('id')
    print row_id
    return 'ok'


@user_page.route('/listapi')
def listapi():
    data = User.query.all()
    # res = [{col: getattr(d, col) for col in cols} for d in data]
    res = [d.__dict__ for d in data]
    print res
    # return jsonify(result=res)
    return 'ok'
