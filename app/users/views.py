# encoding:utf-8

from flask import render_template, Blueprint, redirect

user_page = Blueprint('user_page', __name__)


@user_page.route('/logs')
def log():
    return render_template('log.html')

@user_page.route('/users')
def user():
	return render_template('user.html')