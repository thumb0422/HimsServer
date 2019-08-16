#!/usr/bin/python
#coding:utf-8

"""
@author: thumb0422
@contact: thumb0422@163.com
@software: PyCharm
@file: run.py
@time: 2019-08-14 21:44
"""

from flask import Flask, request,url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config/devConfig.cfg')
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


@app.route('/')
def show_all():
    return Todo.query.order_by(Todo.pub_date.desc()).all()


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        if not request.form['title']:
            pass
        elif not request.form['text']:
            pass
        else:
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()

            return redirect(url_for('show_all'))
    return


@app.route('/update', methods=['POST'])
def update_done():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
    db.session.commit()
    return redirect(url_for('show_all'))


if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
    app.run()