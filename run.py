#!/usr/bin/python
#coding:utf-8

"""
@author: thumb0422
@contact: thumb0422@163.com
@software: PyCharm
@file: run.py
@time: 2019-08-14 21:44
"""
import json
from flask import Flask, request,url_for, redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from tool.utility import rowToArray

app = Flask(__name__)
app.config.from_pyfile('config/dev.cfg')
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
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
            "title":self.title,
            'text':self.text,
            'done':self.done,
            'desc':"我来了"
        }
        # return json.dumps(json_data,cls=DateEncoder) #有多余的 \ 返回
        return json_data

@app.route('/')
def show_all():
    querys = Todo.query.order_by(Todo.pub_date.desc()).all()
    results = []
    for item in querys:
        results.append(item.to_Json())
    """
    #通过SQL查询返回json
    querys = db.session.execute('select * from todos')
    results = rowToArray(querys)
    """
    return jsonify({'datas':results})

@app.route('/add', methods=['GET', 'POST'])
def add():
    data = request.get_json()
    if request.method == 'POST':
        if not data['title']:
            pass
        elif not data['text']:
            pass
        else:
            todo = Todo(data['title'], data['text'])
            db.session.add(todo)
            db.session.commit()

            return redirect(url_for('show_all'))
    return


@app.route('/update', methods=['POST'])
def update_done():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.get_json()
    db.session.commit()
    return redirect(url_for('show_all'))


if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
    app.run()