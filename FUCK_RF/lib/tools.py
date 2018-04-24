import pymysql
import redis
import requests
from conf.setting import MYSQL_INFO,REDIS_INFO
from hashlib import md5
class MyConnect(object):
	def __init__(self, host, port, user, password, db, charset='utf8'):
		self.__host = host
		self.port = port
		self.user = user
		self.passwd = password
		self.db = db
		self.charset = charset
		self.__get_cur()  # 在类初始化的时候就去调用创建游标的函数

	def __get_cur(self):
		try:
			self.coon = pymysql.connect(
				host=self.__host, port=self.port, user=self.user, passwd=self.passwd,
				charset=self.charset, db=self.db
			)
		except Exception as e:
			print('这里出错了，错误信息是【%s】' % e)
		else:
			self.cur = self.coon.cursor()  # 建立游标

	def select_sql(self, sql):
		self.cur.execute(sql)
		return self.cur.fetchall()

	def other_sql(self, sql):
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
		self.pool = redis.ConnectionPool(host=host, port=port, password=password)
		self.r = redis.Redis(connection_pool=self.pool)

	def get(self, k):
		return self.r.get(k)


	def set(self, k, v):
		self.r.set(k, v)

def my_request(method,url,data):
	try:
		if method.upper()=='GET':
			r = requests.get(url,data).json()
		else:
			r = requests.post(url,data).json()
	except Exception as e:
		return '出错了，错误是%s'%e
	return r

def myMd5(st):
	SECRET_KEY = '68@63fc1jkyu4m+wlvyc5(0gik12u9o90tm5q^l^_w^9^%7=zl'
	st = str(st)
	md = md5()
	st = SECRET_KEY+st
	md.update(st.encode())
	return md.hexdigest()

my_mysql = MyConnect(**MYSQL_INFO)
my_redis = MyRedis(**REDIS_INFO)

