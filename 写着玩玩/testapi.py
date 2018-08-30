# encoding: utf-8
"""
@version:??
@author:df
"""


import urllib
import urllib.request
import urllib.parse
import pymysql

import sqlite3



re = urllib.request.urlopen('http://www.baidu.com').read()
data = re.decode("UTF-8")
print(data)

datapost = urllib.parse.urlencode({'usename':'aaa','password':'111'})
datapost2 = datapost.encode('UTF-8')
request = urllib.request.Request("http://www.baidu.com")
request.add_header("Content-Type","appasdfasdfasdf")
f = urllib.request.urlopen( request , datapost2 )