#!/usr/bin/python
# -*- coding:utf-8 -*-

# @file    : __init__.py
# @Time    : 2019-08-19 14:31
# @Author  : thumb0422@163.com

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config/dev.cfg')
db = SQLAlchemy(app)