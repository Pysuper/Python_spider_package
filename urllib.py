# get请求
import urllib.request

url = 'https://www.baidu.com/'
response = urllib.request.urlopen(url)
print(response.read().decode('utf-8'))


# post 请求
import urllib.parse
import urllib.request
# 不加data就是以get的方式发送请求
data = bytes(urllib.parse.urlencode({'word':'python'}),encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post',data = data)
print(response.read())


# timeout 超时报错
import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get',timeout = 1)
print(response.read())

# 设置超时时间
import socket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout = 1)
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):     #
        print('Time Out')


# POST请求
import urllib.request
url = 'http://python.org'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))


from urllib import request,parse
# 参数
url = 'http://httpbin.org/post'
headers = {'User-Agent':'','Host':''}
dict = {'name':'G'}
data = bytes(parse.urlencode(dict),encoding = 'utf-8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

from urllib import request,parse
url = 'http://httpbin.org/post'
dict = {'name':'G'}
data = bytes(parse.urlencode(dict),encoding = 'utf-8')
req = request.Request(url = url,data = data,method = 'POST')
req.add_header('User-Agent','Mozllla/4.0(compatlble;MSIE 5.5;Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# 响应类型
import urllib.request

url = 'http://www.python.org'
response = urllib.request.urlopen(url)
print(type(response))

# 状态码、响应头
import urllib.request

url = 'http://fanyi.baidu.com/'
response = urllib.request.urlopen(url)
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))     # 服务器是用什么做的


# 访问不存在的网站
from urllib import request,error

try:
    url = '一个不存在的网址'    # 404 not found
    response = request.urlopen(url)
except error.URLError as e:
    print(e.reason)

# 具体可以捕获那些异常
from urllib import request,error

try:
    url = ''
    response = request.urlopen('')
except error.HTTPError as e:    # 先捕捉子类异常
    print(e.reason,e.headers,e.code,sep='\n')
    # reason 返回出错信息
    # headers 返回响应头的错误信息
    # code 错误的数码(404)
except error.URLError as e:     # 再捕捉父类异常
    print(e.reason)
else:
    print('Request Successfully')

# 返回错误类型
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://www.baidu.xom',timeout=0.01)
except urllib.error.URLError as e:
    print(e.reason)
    if isinstance(e.reason,socket.timeout):
        print('Time Out')


# 使用浏览器打开连接
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://m.weibo.com')


# Handler 代理(切换代理，总是从不同区域获得数据，服务器就不会封掉爬虫)
import urllib.request

# 传入http代理
proxy_handler = urllib.request.ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')
print(response.read())


# Cookie(用来维持登录状态)
# 获取cookie(如果cookie没有失效，可以从文本中再次读取cookie)
import http.cookiejar,urllib.request

cookie = http.cookiejar.CookieJar()     # 声明cookie为一个对象
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name +'='+ item.value)

# 将cookie保存为一个文本(火狐浏览器的cookie保存格式)
import http.cookiejar,urllib.request

filename = 'cookie.txt'
# MozillaCookieJar-->LWPCookieJar 另一找嗯cookie保粗格式，什么格式保存的，就要用什么格式打开
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

#　cooki读取(再读取网站时，就自动把cookie附着进去)
import http.cookiejar,urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener((handler))
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))


# parse的三个参数
# urllib.parse.urlparse(urlstring,scheme,allow_fragment=True)

# 将url划分为6个标准的结构
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com')
print(type(result),result)

# scheme='https'    默认的协议类型
# 如果没有协议类型，则自动补充为https
# 访问的网站有协议类型的时候，第二个参数就没有实际意义
from urllib.parse import urlparse
result = urlparse('http:www.baidu.com',scheme='https')
print(result)

# allow_fragments=False     拼接#comment 自动往前拼接
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com',allow_fragments=False)
print(result)


# urlunparse    拼接url
from urllib.parse import urlunparse
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))


#　urljoin url之间的拼接
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))


# urlencode (把字典对象转换成get请求参数)
from urllib.parse import urlencode
params = {'name':'Allen','age':'22'}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(base_url)
print(url)

