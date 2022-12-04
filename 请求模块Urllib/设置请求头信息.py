from urllib import request, parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.baidu.com/'
#定义请求头信息
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
#将表单数据转换为bytes类型，并设置编码方式为UTF-8
data = bytes(parse.urlencode({'hello':'python'}),encoding='utf-8')
#创建Request对象
r = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(r)
print(response.read().decode('utf-8'))