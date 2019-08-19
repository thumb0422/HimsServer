#!/usr/bin/python
# -*- coding:utf-8 -*-

# @file    : __init__.py
# @Time    : 2019-08-19 13:30
# @Author  : thumb0422@163.com

from flask import Blueprint
from common import app,db

app = app
db = db

api = Blueprint('api', __name__)

from . import views