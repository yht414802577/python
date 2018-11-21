# encoding: utf-8
"""
@version:接口测试使用requests和json方式
@author:df
"""

import requests
import json

session = requests.session()
reult=session.post('http://www.baidu.com', data={'username':'shuaige','password':'1111'})
reult.content.decode('utf-8')
reult.text

params = {}

#结息json
jsonres = json.loads(reult.text)

if jsonres['status'] == 200:
    print('pass')
else:
    print('fail')

#保存token
params['token'] = jsonres['token']
#添加token头
session.headers['token'] = params['token']