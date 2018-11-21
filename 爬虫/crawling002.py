from urllib import request
from urllib.error import HTTPError, URLError
import re
import itertools

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' %page
    html = request.urlopen(url).read().decode()
    print(url)
    print(html)
    if html is None:
        break
    else:
        pass
