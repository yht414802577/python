# encoding: utf-8
"""
@version:??
@author:df
"""

from urllib.error import URLError, HTTPError
from urllib import request
import re

def crawl_sitemap(url):
    """
    每个站点都可以依靠Sitemap文件来爬取站点中的每个网页。有些站点可能根本就没有 Sitemap文件
    目标网站的 robots.txt 文件中发现了网站地图（Sitemap.xml 文件），网站地图中包含了这个站点里面所有网页的URL。
    想要下载目标网站里面的所有网页，我们可以通过一个简单的正则表达式来解析网站地图（Sitemap.xml 文件）。如何解析？很简单，只需要从<loc>标签中提取出 URL 即可
    """
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap) #findall() 函数是找到所有符合条件的Str字符串。<loc>(.*?)</loc>指的是：(.*?) 意思是：匹配所有<loc>(xxxx)</loc> 这样字符串，并将括号内的数据作为结果返回。

    for link in links:
        html = download(link)

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