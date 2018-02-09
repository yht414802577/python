#!/usr/bin/env python   
# -*- coding: UTF-8 -*-

import base64
import urllib
import urllib2


def jiam(jiami):
	encode = base64.b64encode(jiami)
	return encode 


def jiem(jiemi):
	data = base64.b64decode(jiemi)
	return data

def jiekou(data,):
	data = data
	urllib.urlopen()
	urllib2.HTTPCookieProcessor()

if __name__ == '__main__':
    aaa=jiam('asdfasdf')
    print aaa
