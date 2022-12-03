import urllib.request

response = urllib.request.urlopen('https://www.baidu.com/')
print('响应数据类型为：',type(response))