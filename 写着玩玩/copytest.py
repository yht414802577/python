from urllib.request import urlopen

def main():
    url = 'http://www.taobao.com'
    re = urlopen(url)
    print(re.read().decode())
    print(re.info())

if __name__ == '__main__':
    main()
