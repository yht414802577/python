REDIS_INFO = {
	'host':'47.93.161.229',
	'port':6379,
	'password':''
}

MYSQL_INFO  = {
	'host':'47.93.161.229',
	'port':3306,
	'user':'root',
	'password':'123456',
	'db':'circle_talk',
	'charset':'utf8'
}
HOST_INFO = 'http://test.teamin.cc:18308'
#对应的环境信息
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_Path= os.path.join(BASE_PATH,'report')
XML_path = os.path.join(REPORT_Path,'xml')
HTML_path = os.path.join(REPORT_Path,'html')
CASE_PATH = os.path.join(BASE_PATH,'cases')
TESTCASE_PATH=os.path.join(BASE_PATH,'testcase')
# HEADER={'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJsb2dpbkluZm8iOnsidXNlcklkIjoyOCwidGVybWluYWxUeXBlIjoid2VjaGF0X3NtYWxsIn0sImlhdCI6MTUxNzc5Njc1MywiZXhwIjoxNTE3ODY4NzUzfQ.2WSznAidkUX7nvnU1eDmmTEb2y1YbYrKElggCWcWmzU'}
