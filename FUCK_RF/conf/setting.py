REDIS_INFO = {
	'host':'116.196.122.221',
	'port':6379,
	'password':'123456'
}

MYSQL_INFO  = {
	'host':'116.196.122.221',
	'port':3306,
	'user':'besttest',
	'password':'123456',
	'db':'main',
	'charset':'utf8'
}
HOST_INFO = 'http://api.nnzhp.cn'
#对应的环境信息
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_Path= os.path.join(BASE_PATH,'report')
XML_path = os.path.join(REPORT_Path,'xml')
HTML_path = os.path.join(REPORT_Path,'html')
CASE_PATH = os.path.join(BASE_PATH,'cases')