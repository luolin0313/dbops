# encoding:utf-8

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/idc')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/idc')
def idc():
    return render_template('idc.html')


@app.route('/pc')
def pc():
    return render_template('pc.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
