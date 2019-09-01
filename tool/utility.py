#!/usr/bin/python
# coding:utf-8

"""
@author: thumb0422
@contact: thumb0422@163.com
@software: PyCharm
@file: utility.py
@time: 2019-08-18 19:33
"""
from random import Random
import json
from decimal import Decimal
import datetime


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d")


def random_str(randomLength=12):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomLength):
        str += chars[random.randint(0, length)]
    return str


def getModelKey(keyPrefix):
    localTimeStr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    localTime = localTimeStr.replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
    result = keyPrefix + localTime + random_str(4).upper()
    return result


'''JSON 转 Dictionary'''


def converJsonToDic(jsonValue):
    jsonStr = json.dumps(jsonValue)
    dic = eval(jsonStr)
    return dic


'''对象转Dictionary'''


def classToDict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict


def rowToArray(objs):
    d = []
    for obj in objs:
        row_as_dict = dict(obj)
        resultDic = {}
        for (k, v) in row_as_dict.items():
            resultDic[str(k)] = str(v)
        d.append(resultDic)
    return d


def rowToTuple(objs):
    d = []
    for obj in objs:
        if obj.__len__() > 1:
            k = obj[0]
            v = obj[1]
            resultTuple = (str(k), str(v))
            d.append(resultTuple)
    return d
