#!/usr/bin/python
# -*- coding:utf-8 -*-

# @file    : models
# @Time    : 2019-08-19 12:23
# @Author  : thumb0422@163.com

from datetime import datetime
from api import db,app

class Todo(db.Model):
    __tablename__ = 'todos'
    __table_args__ = {"useexisting": True}
    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()
    def to_Json(self):
        json_data = {
            "id":self.id,
            "title":self.title,
            'text':self.text,
            'done':self.done,
            'pub_date':self.pub_date,#需要格式化
            'desc':"我来了"
        }
        # return json.dumps(json_data,cls=DateEncoder) #有多余的 \ 返回
        return json_data

db.create_all()
