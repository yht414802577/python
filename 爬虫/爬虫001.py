# encoding: utf-8
"""
@version:??
@author:df
"""

from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def download(url, num_retries=2):
    print('Download:', url)
    try:
        html = urlopen(url).read()
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