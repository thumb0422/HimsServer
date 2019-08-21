#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@author: thumb0422
@contact: thumb0422@163.com
@software: PyCharm
@file: run.py
@time: 2019-08-14 21:44
"""

from common import app

from api import api as apiBP
app.register_blueprint(apiBP,url_prefix='/api')

if __name__ == '__main__':
    app.run(port=8081)