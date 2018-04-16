# -*- coding:utf-8 -*-
import requests
import pymysql
import time
import re
import urllib
from httplib import ResponseNotReady


HOSTNAME = '127.0.0.1'
def readSQLcase():        #提交订单流程的相关接口，循环遍历响应项目的所有接口
    sql = 'select * from zt_casestep group by zt_casestep.case as t1'
    coon = pymysql.connect(user = 'root' , passwd = 'test123456' , db = 'zentao' , port = 3306 , host = '127.0.0.1' , charset = 'uft8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        case_list = []
        case_list.append(ii)
        GetToken()
        interfaceTest(case_list)
    coon.commit()
    cursor.close()
    coon.close()

def interfaceTest(case_list):       #读取一条接口测试用例的内容
    res_flags = []
    request_urls = []
    responses = []
    strinfo = re.compile('{preOrderSN}')    #判断参数中如果有动态参数{preOrderSN}，则在代码中取值，作为订单号
    for case in case_list:
        try:
            case_id = case[0]
            interface_name = case[1]
            method = case[3]
            url = case [2]
            param = case[4]
            res_check = case[5]
        except Exception,e:
            return '测试用例格式不正确！%s'%e
        if  param=='':
            new_url = 'http://'+HOSTNAME+url
        elif param=='null':
            new_url = 'http://'+HOSTNAME+url
        else:
            param = strinfo.sub(preOrderSN , param)  #如果有动态关联参数，则用值替换变量参数名，把返回值传递到该订单号
            new_url = 'http://'+HOSTNAME+url+'?'+urlParam(param)
            request_urls.append(new_url)
        if method.upper() == 'GET':     #如果为GET方法，读取如下get请求和返回
            print(str(case_id)+' '+new_url)
            headers = {
                'Host':HOSTNAME,
                'Connerion':'keep-alive',
                'token':token,
                'Content-Type':'application/x-wwww-form-urlencoded',
                'User-Agent':'Apache-HttpClint/4.2.6(java 1.5)'
            }       #设置http头信息，包括主机名和用户登陆的token值
            data = None
            results = requests.get(new_url,data,headers = headers).text       #获取返回数据
            responses.append(results)
            res = readRes(results,res_check)     #采用正则表达式校验，请求的返回数据，校验结果有三种：pass，fail，JIFI
            print(results)
            if 'pass' == res:
                writeResult(case_id,'pass')
                res_flags.append('pass')
            else:
                writeResult(case_id, 'fail')
                res_flags.append('fail')
                writeBug(case_id,interface_name,new_url,results,res_check)
        else:
            print(str(case_id)+' '+new_url)
            headers = {
                'Host':HOSTNAME,
                'Connerion':'keep-alive',
                'token':token,
                'Content-Type':'application/x-wwww-form-urlencoded',
                'User-Agent':'Apache-HttpClint/4.2.6(java 1.5)'
            }
            data = None
            results = requests.post(new_url,data,headers=headers).text
            responses.append(results)
            res = readRes(results,res_check)
            print(results)
            if 'pass' == res:
                writeResult(case_id,'pass')
                res_flags.append('pass')
            else:
                writeResult(case_id,'fail')
                res_flags.append('fail')
                if reserror(results):
                    writeBug(case_id,interface_name,new_url,'api response is error',res_check)
                else:
                    writeBug(case_id,interface_name,new_url,results,res_check)
            try:
                preOrderSN(results)
            except:
                print('ok')

def readRes(res,res_check):     #正则表达式校验，校验结果一致，返回pass，否则返回错误信息
    res = res.replace(':','=')
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return '错误，返回参数不一致'+str(s)
    return 'pass'

def urlParam(param):      #参数值替换
    param1 = param.replace('*','&')                 #如果参数在数据库中为*，替换为&
    return param1.replace('&quot;','\"')

def GetToken():
    global token
    url = 'http://'+HOSTNAME+'/buyer/user/login.do'
    params = {
        'phone':'1279888888',
        'pwd':'12341234123412341234'
    }
    request = urllib2.Requset(url=url,data=urllib.urlencode(params))
    response = urllib2.urlopen(request)
    data = response.read()
    regx = '.*"token":"(.*)","ud"'
    pm = re.search(regx,data)
    token = pm.group(1)
    regy = r'"state":(\d+)}'
    pn = re.search(regy,data)
    state = pn.group(1)
    if state =='0':
        return True
    return False

def preOrderSN(results):       #预提交订单，参数动态获取
    global preOrderSN
    regx = '.*"preOrderSN":"(.*)","toHome"'     #提交订单，正则表达式，左边匹配：preOrderSN ， 右边匹配：toHome
    pm = re.search(regx,results)
    if pm:
        preOrderSN = pm.group(1),encode('utf-8')   #如果匹配到，则转换为中文，并返回值
        return preOrderSN
    return False

def reserror(results):    #接口返回匹配到为html页面服务器没有响应，则改调用接口错误
    global html
    regx = 'html'
    pm = re.search(regx.results)     # regx变量赋值为html的字符串，如果服务器异常则会返回404等html标识，进行匹配
    if pm:
        return regx
    return False

def writeResult(case_id,result):
    result = result.encode('utf-8')
    now = time.strftime('%Y-%m-%d  %H:%M:%S')
    sql = 'updata zt_testrun set lastRunResult = %2 where zt_testrun.task = 8'
    param = (result,now,case_id)
    print(result)
    coon = pymysql.connect(user='root',passwd='test123456',db='zentao',port=3306,host='127.0.0.1',charset='utf8')
    cursor = coon.cursor()
    cursor.execute(sql,param)
    coon.commit()
    cursor.close()
    coon.close()

def writeBug(bug_id,interface_name,request,response,res_check):
    interface_name = interface_name.encode('utf-8')
    res_check = res_check.encode('utf-8')
    response = response.encode('utf-8')
    request = request.encode('utf-8')
    bug_title = str(bug_id)+'_'+interface_name+'报错'
    step = '[请求]<br />'
    sql = ''
    coon = pymysql.connect(user='root',passwd='test123456',db='zentao',port=3306,host='127.0.0.1',charset='utf8')
    cursor = coon.cursor()
    cursor.execute(sql)
    coon.commit()
    cursor.close()
    coon.close()

if __name__=='__main__':
    readSQLcase()
    print(done)
    time.sleep(60)
