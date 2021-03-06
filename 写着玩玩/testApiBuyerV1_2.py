# -*- coding:utf-8 -*-
import requests
import pymysql
import time
import re
import urllib

HOSTNAME = '127.0.0.1'      #公共变量

def readSQLcase():                                    #读取测试用例，循环遍历相应项目的所有测试用例，读取产品id，
    sql = 'select * from zt_case'
    coon = pymysql.connect(host = '127.0.0.1',user = 'root',password = 'test123456',db = 'zentao',charset = 'utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        case_list = []
        case_list.append(ii)
        GetToken()      #获取token（）
        interfaceTest(case_list)
    coon.commit()
    cursor.close()
    coon.close()

def interfaceTest(case_list):     #读取一条接口测试用例
    res_flags = []
    request_urls = []
    responses = []
    for case in case_list:
        try:
            case_id = case[0]   #读取测试用例id
            interface_name = case[1]    #读取测试用例接口名称
            method = case[3]    #读取接口方法
            url = case[5]   #读取接口url地址
            param = case[2]     #读取接口参数列表
            res_check = case[4]     #读取接口返回校验
        except Exception e:
            return '格式不正确'
        if param=='':
            new_url = 'http://'+HOSTNAME+url  #如果接口没有参数，接口设置为hostname+url
        elif param=='null':
            new_url = 'http://'+HOSTNAME+url    #如果接口没有参数，接口设置为hostname+url
        else:
            new_url = 'http://'+HOSTNAME+url+'?'+urlParam(param)     #如果接口有参数，接口设置为hostname+url+param
            request_urls.append(new_url)

        if method.upper() == 'GET':     #如果为get方法，读取get方法请求和返回数据
            print(str(case_id)+''+new_url)       #打印用例id和接口地址
            headers = {
                'Host':HOSTNAME,
                'Connection':'keep-alive',
                'token':token,
                'Content-Type':'application/x-www-from-urlencoded',
                'User-Agent':'Apache-HttpClient/4.2.6(java 1.5)'
            }       #设置http头信息，包括主机名和用户登路token值
            data = None
            results = requests.get(new_url,data,headers=headers).text       #发送get请求，results得到请求的返回数据
            responses.append(results)
            res = readRes(results,res_check)        #对请求的返回数据进行校验，采用正则表达式校验，校验结果有三种（pass ， fail ，jFIF）

            if 'pass' == res:
                writeResult(case_id,'pass')     #结果为pass写入关联的用例id
                res_flags.append('pass')
                if JFIF(results):
                    results = 'JFIF ok'     #校验jfif则为图片
                else:
                    print('接口名称'+interface_name)
                    print('接口地址'+new_url)
                    print('相应数据'+results)
                    print(str(case_id)+'~~~~~~~~~~~~success~~~~~~~~~~~~~~')
                print('接口名称' + interface_name)
                print('接口地址' + new_url)
                print('相应数据' + results)
                print(str(case_id) + '~~~~~~~~~~~~success~~~~~~~~~~~~~~')
            else:
                res_flags.append('fail')
                writeResult(case_id,'fail')     #结果为fail写入关联用例id
                if reserror(results):
                    writeBug(case_id,interface_name,new_url,'api response is error',res_check)   #如果接口响应异常，打印错误信息记录bug写到数据库
                else:
                    writeBug(case_id, interface_name, new_url, 'api response is error', res_check)      #如果接口验证数据错误，打印错误信息记录bug写到数据库
                    print('接口名称'+interface_name)
                    print('接口地址'+new_url)
                    print('相应数据'+results)
                    print(str(case_id)+'~~~~~~~~~~~~success~~~~~~~~~~~~~~')
                print('接口名称' + interface_name)
                print('接口地址' + new_url)
                print('相应数据' + results)
                print(str(case_id) + '~~~~~~~~~~~~success~~~~~~~~~~~~~~')

        else:       #请求为post
            headers = {
                'Host': HOSTNAME,
                'Connection': 'keep-alive',
                'token': token,
                'Content-Type': 'application/x-www-from-urlencoded',
                'User-Agent': 'Apache-HttpClient/4.2.6(java 1.5)'
            }
            data = None
            results = requests.get(new_url, data, headers=headers).text
            responses.append(results)
            res = readRes(results, res_check)

            if 'pass' == res:
                writeResult(case_id, 'pass')
                res_flags.append('pass')
                if JFIF(results):
                    results = 'JFIF ok'
                else:
                    print('接口名称' + interface_name)
                    print('接口地址' + new_url)
                    print('相应数据' + results)
                    print(str(case_id) + '~~~~~~~~~~~~success~~~~~~~~~~~~~~')
                    continue
                print('接口名称' + interface_name)
                print('接口地址' + new_url)
                print('相应数据' + results)
                print(str(case_id) + '~~~~~~~~~~~~success~~~~~~~~~~~~~~')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
                if reserror(results):
                    writeBug(case_id, interface_name, new_url, 'api response is error', res_check)
                else:
                    writeBug(case_id, interface_name, new_url, 'api response is error', res_check)

                print('接口名称' + interface_name)
                print('接口地址' + new_url)
                print('相应数据' + results)
                print(str(case_id) + '~~~~~~~~~~~~success~~~~~~~')

def readRes(res,res_check):     #校验结果。如果通过返回pass，否则返回错误提示
    res = res.replace(':',"=").replace('','=')      #校验时替换符号为=号，在进行校验
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return u'错误，返回参数和预期结果不一致'+str(s)
    return 'pass'

def urlParam(param):    #参数值替换
    param1 = param.replace('*','&')     #如果参数在数据库中为*，替换为&
    param2 = param1.replace('&quot','\"')
    return param2.replace(';','&')

def GetToken():     #取用户登录的token值
    global token    #定义token为全局变量
    url = 'http://'+HOSTNAME+'/buyer/user/login.do'     #接口url
    params = {
        'phone':'123456',
        'pwd':'1234'
    }       #参数为登录手机号和密码
    request = urllib2.Request(url=url,data=urllib.urlencode(params))    #发送接口库请求url和参数
    response = urllib2.urlopen(request)     #打开url
    data = response.read()      #返回响应数据
    regx = '.*"token":"(.*)","ud"'      #正则表达式token，左边匹配“token”:",右边匹配“，“ud”
    pm = re.search(regx,data)       #取token匹配值
    state = pm.group(1)     #如果匹配到state匹配到0，则返回为0；否则为登录
    if state == '0':
        return True
    return False

def reserror(results):      #接口页面返回匹配到html页面服务器美哦与响应时，改为调用接口错误
    global html
    regx = 'html'       #regx变量赋值为html字符串，如果服务器异常时返回404等html标识，进行匹配
    pm = re.search(regx,results)
    if  pm:
        return regx
    return False

def JFIF(results):      #接口页面返回匹配到JFIF时，说明返回图片格式正确，负责错误
    global JFIF
    regx = 'JFIF'
    pm = re.search(regx,results)
    if  pm:
        return regx
    return False

def writeResult(case_id,result):        #写测试结果到数据库
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")        #当前时间格式
    sql = "updata zt_testrun set lastRunResult = %s , lastRunDate = %s , lastRunner = 'auto' where zt_testrun.task = 8 and zt_testrun.case = %s;"
    param = (result,now,case_id)        #把测试结果，时间，用例id，作为蚕食写到数据库
    coon = pymysql.connect(user = 'root' , passwd = 'test123456' , db = 'zentao' , port = 3306 , host = '192.168.58.79' , charset = 'utf8')     #连接数据库
    cursor = coon.cursor()
    cursor.execute(sql,param)
    coon.commit()
    cursor.close()
    coon.close()

def writeBug(bug_id,interface_name,request,reponse,res_check):
    interface_name = interface_name.encode('utf-8')
    res_check = res_check.encode('utf-8')
    request = request.encode('utf-8')
    reponse = reponse.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    bug_title = str(bug_id) + '_' +interface_name + '_出错了'
    step = '[请求报文]' + request + '<br/>' + '[预期结果]' + res_check + '<br/>' + '[响应报文]' + reponse
    sql = "insert into zt_bug (openedDate , openedBy , lastEditedDate , lastEditedBy , status , steps , stoyVersion ) values ('%s',)"
    coon = pymysql.connect(user = 'root' , passwd = 'test123456' , db = 'zentao' , port = 3306 . host = '172.0.0.1' , charset = 'utf8')
    cursor = coon.cursor()
    cursor.execute(sql)
    coon.commit()
    cursor.close()
    coon.close()