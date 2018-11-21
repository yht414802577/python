from urllib import request
from urllib.error import HTTPError, URLError
import re

def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<div>(.*?)</div>', sitemap)
    for link in links:
        html = download(link)
        return html

def download(url, num_retries=2, user_agent='wswp'):
    print('Downloading:', url)
    headers = {'User-agent':user_agent}
    request1 = request.Request(url, headers=headers)
    try:
        html = request.urlopen(request1).read().decode()
    except HTTPError as a:
        print('Download HTTPerror:', a.reason)
        # html = None
        if num_retries > 0:
            if hasattr(a, 'code') and 400 <= a.code < 500:
                return download(url, num_retries-1)
    except URLError as e:
        print('Download URLerror:', e.reason)
        # html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html

if __name__ == '__main__':
    ll = crawl_sitemap('http://www.taobao.com')
    print(ll)
