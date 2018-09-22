import pymysql
import redis
import requests
from conf.setting import MYSQL_INFO,REDIS_INFO,TESTCASE_PATH
from hashlib import md5
class Myconnect(object):
    def __init__(self,host,port,user,password,db,charset='utf8'):
        self.__host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.__get_cur()

    def __get_cur(self):
        try:
            self.coon = pymysql.connect(
                host = self.__host,port = self.port,user = self.user,passwd = self.password,
                charset = self.charset,db = self.db
            )
        except Exception as e:
            print('这里出错了，错误信息是【%s】' % e)
        else:
            self.cur = self.coon.cursor()

    def select_sql(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def other_sql(self,sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            print('sql执行失败%s' % e)
        else:
            self.coon.commit()

    def close(self):
        self.cur.close()
        self.coon.close()

class MyRedis(object):
    def __init__(self,host,port,password):
        # self.pool = redis.Connection(host=host,port=port,password=password)
        # self.r = redis.Redis(connection_pool=self.pool)
        self.r = redis.Redis(host=host,port=port,password=password)

    def get(self,k):
        return self.r.get(k)

    def set(self,k,v):
        self.r.set(k,v)

def my_request(method,url,data,header=None):
    try:
        if method.upper()=='GET':
            r = requests.get(url=url,data=data,headers=header).json()
        elif method.upper()=='POST':
            r = requests.post(url=url,data=data,headers=header).json()
        elif method.upper()=='DELETE':
            r = requests.delete(url=url,data=data,headers=header).json()
        elif method.upper()=='PUT':
            r = requests.put(url=url,data=data,headers=header).json()
        else:
            return False
    except Exception as  e:
        return '出错了，错误是%s'%e
    return r

def my_code(method,url,data,header):
    try:
        if method.upper()=='GET':
            r = requests.get(url=url,data=data,headers=header).status_code
        elif method.upper()=='POST':
            r = requests.post(url=url,data=data,headers=header).status_code
        elif method.upper()=='DELETE':
            r = requests.delete(url=url,data=data,headers=header).status_code
        elif method.upper()=='PUT':
            r = requests.put(url=url,data=data,headers=header).status_code
        else:
            return False
    except Exception as e:
        return '出错了，错误是%s'%e
    return  r
def get_circle(url,data=None,header=None):
    '''获取圈子'''
    r = requests.get(url, data, headers=header).json()
    return  r[0]['circleId']
def get_task(url,data=None,header=None):
    res = requests.get(url,data,headers=header).json()
    return res[0]['taskId']
def myMd5(st):
    SECRET_KEY = '68@63fc1jkyu4m+wlvyc5(0gik12u9o90tm5q^l^_w^9^%7=zl'
    st = str(st)
    md = md5()
    st = SECRET_KEY+st
    md.update(st.encode())
    return md.hexdigest()
# def case(fw):

def case():
    import os, sys
    # import json
    testcase=[]
    list = [test for test in os.listdir(TESTCASE_PATH) if test.endswith('.txt')]
    for case in list:
        with open(os.path.join(TESTCASE_PATH,case),'r+',encoding='utf8') as f:
            # f.seek(0)
            # print(f.readlines())
            # for line in f:
            #     print(line.strip())
            #     testcase.append([{'plans':line.strip()}])
            # print([{'plans':f.read()}])
            testcase.append([{'plans':f.read()}])
    # print(testcase)
    return testcase
case()

import time,datetime
def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()
    # print(week_day_dict[day])
    return week_day_dict[day]
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
# print(get_week_day(datetime.datetime.now()))
# print(get_week_day(datetime.date.fromtimestamp(time.time())))
# my_mysql = Myconnect(**MYSQL_INFO)
# my_redis = MyRedis(**REDIS_INFO)