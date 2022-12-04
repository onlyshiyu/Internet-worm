from urllib import request
from urllib import error

try:
    #向不存在的网络地址发送请求
    response = request.urlopen('http://site2.rjkflm.com:666/123index.html')
    print(response.status)
except error.HTTPError as error:
    print('状态码为：',error.code)
    print('异常信息为：',error.reason)
    print('请求头信息为：',error.headers)