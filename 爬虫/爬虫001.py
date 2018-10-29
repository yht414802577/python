# encoding: utf-8
"""
@version:??
@author:df
"""

from urllib.error import URLError, HTTPError
from urllib import request

def download(url, num_retries=2, user_agent='wswp'):
    print('Download:', url)
    header = {'User-agent': user_agent}
    requests = request.Request(url, headers=header)
    try:
        html = request.urlopen(requests).read()
    except HTTPError as a:
        print('Download error:', a.reason)
        html = None
        if num_retries > 0:
            if hasattr(a, 'code') and 400 <= a.code < 500:
                return download(url, num_retries-1)
    except URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html

if __name__ == '__main__':
    url = 'http://www.taobao.com'
    ll = download(url)
    print(ll)