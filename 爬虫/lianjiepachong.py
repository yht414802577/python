# encoding: utf-8
"""
@version:??
@author:df
"""

from urllib import request
from urllib.error import HTTPError, URLError
import re
import itertools

def link_crawler(sead_url, link_regex):
    craw_queue = [sead_url]
    while craw_queue:
        url = craw_queue.pop()
        html = request.urlopen(url).read().decode()
        for link in get_links(html):
            if re.match(link_regex, link):
                craw_queue.append(link)

def get_links(html):
    webpage_regex = re.compile('<a[~>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)