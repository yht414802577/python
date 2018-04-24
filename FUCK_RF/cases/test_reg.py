import unittest
from conf.setting import HOST_INFO
from lib.tools import my_request,my_mysql,my_redis,myMd5
from nose_parameterized import parameterized
class Reg(unittest.TestCase):
	def setUp(self):
		self.url = HOST_INFO+'/api/user/user_reg'
		#请求地址

	@parameterized.expand(
		[
			[
				{'username':'lihainan_fuck123','pwd':'aA123456','cpwd':'aA123456'},
				"delete from app_myuser where username='lihainan_fuck123'",
				1000,
				'注册成功！'
			 ],
			[
				{'username': 'lihainan_fuck789', 'pwd': 'aA123456', 'cpwd': 'aA123456'},
				"delete from app_myuser where username='lihainan_fuck789'",
				1000,
				'注册成功！'
			],
		]
	)
	def test_reg_success(self,data,sql,hope1,hope2):
		'''正常注册'''
		# data = {'username':'lihainan_fuck123','pwd':'aA123456','cpwd':'aA123456'}
		res = my_request('post',self.url,data)
		print(res)
		self.assertIsInstance(res,dict)#校验返回的类型
		self.assertEqual(hope1,res.get('error_code'))#校验code值
		self.assertEqual(hope2,res.get('msg'))#校验msg值
		# sql= "delete from app_myuser where username='lihainan_fuck123'"
		my_mysql.other_sql(sql)
	def test_reg_exist(self):
		'''测试已经存在的'''
		sql = 'insert into app_myuser (username,passwd) VALUE ("lihainan_fuck456","%s")'%myMd5('123456')
		my_mysql.other_sql(sql)
		data = {'username':'fuck456','pwd':'aA123456','cpwd':'aA123456'}
		res = my_request('post',self.url,data)
		self.assertIsInstance(res,dict)#校验返回的类型
		self.assertEqual(3005,res.get('error_code'))#校验code值
		self.assertEqual('用户已存在',res.get('msg'))#校验msg值
		delete_sql = "delete from app_myuser where username='lihainan_fuck456';"
		my_mysql.other_sql(delete_sql)
if __name__=='__main__':
	unittest.main()
