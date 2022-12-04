from urllib import request, parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://site2.rjkflm.com:666/index/chklogin.html'
#将表单数据转换为bytes类型，并设置编码方式为UTF-8
data = bytes(parse.urlencode({'username':'mrsoft','password':'mrsoft'}),encoding='utf-8')
#创建Request对象
r = request.Request(url=url,data=data,method='POST')
response = request.urlopen(r)
print(response.read().decode('utf-8'))