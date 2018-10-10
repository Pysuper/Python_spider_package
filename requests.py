# Requests
# requests 是用Python语句编写的，基于Urllib，采用Apache2 Licensed开源协议的HTTP库
# 比urllib更加方便，可以节约大量工作时间，完全满足HTTP测试需求
# 是Python实现的简单易用的HTTP库

# 安装requests--pip3 install requests


# import requests
#
# def write(url):
#
#     response = requests.get(url)
#     with open('/home/python/Desktop/Resquests库/01','wb') as f:
#     # 这里open跟的参数第一个除了选择文件的存储位置外，最后的01还是给文件命名
#         f.write(response.content)
#         f.close()
#
# write('https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=805163359,68275993&fm=27&gp=0.jpg')



### requests.get
# Requests 实例引入
# 获得响应的内容
import requests
url = 'http://www.baidu.com'
response = requests.get(url)
print(type(response))
print(response.status_code)     # 状态码
print(type(response.text))
print(response.text)
print(response.cookies)

# 各种请求方式
import requests
requests.post('http://httpbin.org')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.com/get')
requests.options('http://httpbin.org.get')

# 请求
# 基本get请求
import requests
url = 'http://httpbin.org/get'
response = requests.get(url)
print(response.text)

# 带参数get请求
import requests
response = requests.get('http://httpbin.org/get?name=gamey & age=22')
print(response.text)

import requests
data = {'name':'Allen','age':19}
response = requests.get('http://httpbin.org/get',params=data)   # params的参数是字典的形式
print(response.text)

# 解析Json
import requests
import json
response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(json.loads(response.text))
print(response.json())
print(type(response.json()))

# 获取二进制数据
import requests
response = requests.get('http://www.github.com/favicon.ico')
print(type(response.text),type(response.content))
print(response.text)
print(response.content)

# 通过requests方法，通过图片的url获取图片的二进制数据，并把图片保存到桌面的某个文件夹中
import requests
response = requests.get('http://www.github.com/favicon.ico')
with open('/home/python/Desktop/01','wb') as f:
    f.write(response.content)
    f.close()

# 添加headers
import requests
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36'}
# 在浏览器中查看Requests Headers即可查看User-Agent
response = requests.get('http://www.zhihu.com/explore',headers=headers)
print(response.text)

# response属性
import requests
response = requests.get('http://www.jianshu.com')
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.history),response.history)
print(type(response.url),response.url)


# 状态码判断
import requests
response = requests.get('http://www.jianshu.com')
exit() if not response.status_code == requests.codes.ok else print('Requests Successfully')

import requests
response = requests.get('http://www.jianshu.com')
exit() if not response.status_code == 200 else print('Requests Successfully')

### 基本POST请求
import requests
data = {'name':'Allen','age':'22'}  # 传入字典类型的参数
response = requests.post('http://httpbin.org/post',data=data)
print(response.text)

import requests
data = {'name':'Allen','age':'22'}
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36'}
#　把data,headers都当做参数传入post方法中
response = requests.post('http://httpbin.org/post',data=data,headers=headers)
print(response.json())

# 文件上传
# 将已有的一个文件上传到某一个连接中
import requests
files = {'file':open('/home/python/Desktop/Requests库/01','rb')}
# files中的file是上传之后给文件命的名，后面是源文件的位置及名称
response = requests.post('http://httpbin.org/post',files=files)
print(response.text)


# 获取cookies
# cookies 是requests的一个属性
import requests
response = requests.get('http://www.baidu.com')
print(response.text)
for key,value in response.cookies.items():
    print(key +'='+ value)


# 回话维持－－模拟登录状态
import requests
# 为网站设置一个cookies
# 两个requests是完全独立的－使用两个浏览器，一个用来建立cookies
requests.get('http://httpbin.org/cookies/set/number/123')
# 一个通过cookies访问网站
response = requests.get('http://httpbin.org/cookies')
print(response.text)

# 使用一个浏览器完成上述操作
# 推荐：这样在同一个浏览器中，cookies还是自动处理好的
import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123')
response = s.get('http://httpbin.org/cookies')
print(response.text)


#　证书验证
# 12306的网站证书是一个不安全的证书，SSL认证错误
import requests
response = requests.get('https://www.12306.com')
print(response.status_code)

# 参数verify 消除证书警告
import requests
from requests.packages import urllib3
urllib3.disable_warnings()  # 消除建议加证书验证的警告
response = requests.get('https://www.12306.com',verify=False) # verify的值默认是True
print(response.status_code)

# 参数cert CA证书验证
import requests
response = requests.get('https://www.12306.com',cert=('/path/server.crt','/path/key'))
print(response.status_code)


# 代理设置
import requests
proxies = {'http':'http://123.123.123','https':'http://123.123.123'}
response = requests.get('https://www.taobao.com',proxies=proxies)
print(response.status_code)
# 返回200的状态码－－说明访问成功了

# 需要代理用户名和密码的时候，传入一个代理的字典参数
import requests
proxies = {'http':'http://user.passwoed@127.0.0.1:9743'}
response = requests.get('http:///www,taobao.com',proxies=proxies)
print(response.status_code)

# socks代理--pip install requests[socks]
import requests
proxies = {'http':'socks5://127.0.0.19742','https':'socks5://127.0.0.19742'}
response = requests.get('https://www.taobao.com',proxies=proxies)
print(response.status_code)

# 超时设置
import requests
from requests.exceptions import ReadTimeout
try:
    response = requests.get('https://www.taobao.com',timeout=1)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')

# 认证设置
# 通过auth参数，传入用户名和密码
import requests
from requests.auth import HTTPBasicAuth
response = requests.get('http://120.27.34.24:9001',auth=HTTPBasicAuth('user','123'))
print(response.status_code)

import requests
response = requests.get('http://120.27.34.24:9001',auth=('user','123'))
print(response.status_code)

# 异常处理
import requests
# 导入requests中的异常
from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    response = requests.get('http://httpbin.org/get',timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('HTTPError')
except RequestException:    # 父类的error
    print('Error')

