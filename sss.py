#!/usr/bin/env python   
# -*- coding: UTF-8 -*-


import urllib
import urllib2
import json
import cookielib

def http_post():
    EntryUrl = "http://tongtool.myddns.com:8003/process";
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    resp = urllib2.urlopen(EntryUrl);
#    loginUrl = "http://wms.omniselling.net:48080/omniv4/webservice/queryInventory";   
    loginUrl = "http://tongtool.myddns.com:8003/process/resume/shippingMethod/admin/maintainShippingMethod";
    para = { 
        "token":"6706015faf3f464091e10c60fde922f",
"data":{
        "confirmRequired":"0",
        "extendParameters":[
                            {
                             "parameterType":"input",
                             "parameterCode":"paramCode1",
                             "parameterName":"paramName1",
                             }
                            ],
        "operationType":"A",
        "hasTrackingNumber":"1",
        "shippingMethodName":"EDA-T-CR-001",
        "shippingMethodCode":"EDA-T-001"
        }
        }  
    msg_body=json.dumps(para)
    #postData = urllib.urlencode(para);
    req = urllib2.Request(loginUrl, msg_body);
    req.add_header('Content-Type', 'application/json');
    req.add_header('Cache-Control', 'no-cache');
    req.add_header('Connection', 'keep-alive');
    resp = urllib2.urlopen(req);
    respInfo = resp.info();
    return resp.read()
response = http_post()
print response.decode('utf-8').encode('gb2312')