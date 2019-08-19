#!/usr/bin/python
# -*- coding:utf-8 -*-

# @file    : views
# @Time    : 2019-08-19 14:21
# @Author  : thumb0422@163.com

from flask import request,url_for, redirect,jsonify
from . import db,api
from .models import Todo

@api.route('/',methods = ['GET'])
def show_all():
    querys = Todo.query.order_by(Todo.pub_date.desc()).all()
    results = []
    for item in querys:
        results.append(item.to_Json())
    """
    #通过SQL查询返回json
    querys = db.session.execute('select * from todos')
    from tool.utility import rowToArray
    results = rowToArray(querys)
    """
    return jsonify({'datas':results})

@api.route('/get',methods = ['GET','POST'])
# @api.route('/get/',methods = ['GET','POST'])
def show_index():
    if request.method == 'POST':
        data = request.get_json()
        if data.get('id'):
            querys = Todo.query.filter_by(id=data.get('id'))
            results = []
            for item in querys:
                results.append(item.to_Json())
            return jsonify({'datas':results})
        else:
            return jsonify({'status':-1})
    return jsonify({'status':-1})

@api.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        if (not data.get('title'))  or (not data.get('text')):
            pass
        else:
            todo = Todo(data.get('title'), data.get('text'))
            db.session.add(todo)
            db.session.commit()

            return redirect(url_for('api.show_all'))
    return jsonify({'status':-1})


@api.route('/update', methods=['POST'])
def update_done():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.get_json()
    db.session.commit()
    return redirect(url_for('api.show_all'))

@api.route('/delete', methods=['POST'])
def deleteAll():
    Todo.query.delete()
    db.session.commit()
    return redirect(url_for('api.show_all'))