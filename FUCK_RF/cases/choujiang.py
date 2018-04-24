import unittest
from lib.tools import my_redis,my_request,my_mysql
from conf.setting import HOST_INFO
class Choujiang(unittest.TestCase):
	def setUp(self):
		self.choujiang_url = HOST_INFO + '/api/product/choice'
		self.login_url = HOST_INFO + '/api/user/login'
		self.reg_url = HOST_INFO + '/api/user/user_reg'
	def tearDown(self):
		sql= "delete from app_myuser where username='lhn_1235'"
		my_mysql.other_sql(sql)

	def reg(self):
		'''正常注册'''
		data = {'username':'lhn_1235','pwd':'aA123456','cpwd':'aA123456'}
		res = my_request('post',self.reg_url,data)
		print(res)
		self.assertIsInstance(res,dict)#校验返回的类型
		self.assertEqual(1000,res.get('error_code'))#校验code值
		self.assertEqual('注册成功！',res.get('msg'))#校验msg值

	def login(self):
		'''登录'''
		data = {'username': 'lhn_1235', 'passwd': 'aA123456'}
		res = my_request('post', self.login_url, data)
		self.assertIsInstance(res, dict)  # 校验返回的类型
		self.assertEqual(0, res.get('error_code'))  # 校验code值
		self.sign = res.get('login_info').get('sign')
		self.userId = res.get('login_info').get('userId')

	def testChangjiang(self):
		'''正常抽奖'''
		self.reg()
		self.login()
		my_redis.set('choujiang:lhn_1235',0)
		data = {'userid':self.userId,'sign':self.sign}
		res = my_request('get',self.choujiang_url,data)
		self.assertIsInstance(res, dict)
		self.assertEqual(0, res.get('error_code'))  # 校验code值

	def testChangjiangErr(self):
		'''抽奖次数用尽'''
		self.reg()
		self.login()
		my_redis.set('choujiang:lhn_1235',3)
		data = {'userid':self.userId,'sign':self.sign}
		res = my_request('get',self.choujiang_url,data)
		self.assertIsInstance(res, dict)
		self.assertEqual(1099, res.get('error_code'))  # 校验code值


if __name__ =='__main__':
	unittest.main()
