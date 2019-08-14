#!/usr/bin/python
#coding:utf-8

"""
@author: thumb0422
@contact: thumb0422@163.com
@software: PyCharm
@file: app.py
@time: 2019-08-14 21:44
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

if __name__=='__main__':
    app.run(debug=True,port=5005)