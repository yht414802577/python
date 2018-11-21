from urllib import request
from urllib.error import HTTPError, URLError
import itertools

max_errors = 5
num_errors = 0

def download(url, num_retries=5):
    try:
        html = request.urlopen(url).read().decode()
    except HTTPError as e:
        if num_retries > 0:
            if hasattr(e, 'code') and 400 <= e.code < 500:
                return download(url, num_retries-1)
    except URLError as u:
        if num_retries > 0:
            if hasattr(a, 'code') and 500 <= u.code < 600:
                return download(url, num_retries)
if __name__ == '__main__':
    for page in itertools.count(1):
        print(page)
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                break
        else:
            num_errors = 0
        print(html)
