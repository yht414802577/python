import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://www.weather.com.cn/weather/101190401.shtml')
html_data = req.read().decode('UTF-8')
#print(html_data)

bs = BeautifulSoup(html_data , 'html.parser')
body = bs.body
data = body.find('div',{'id':'7d'})  #查询div标签id = 7d
input_bq = data.find('input')   #查询div标签id = 7d 下面的所有input标签
#print(input_bq)
ul = data.find('li')
print(ul)
