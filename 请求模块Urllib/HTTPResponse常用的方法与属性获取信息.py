from urllib import request

url = 'https://www.baidu.com/'
response = request.urlopen(url=url)
print('响应状态码为：',response.status)
print('响应头所有信息为：',response.getheaders())
print('响应头指定信息为：',response.getheader('Accept-Ranges'))
# 读取HTML代码并进行UTF-8解码
print('Python官网HTML代码如下：\n',response.read().decode('utf-8'))