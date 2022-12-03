import urllib.request
import urllib.parse

url = 'https://www.httpbin.org/post'
#定义请求头信息
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
#将表单数据转换为bytes类型，并设置编码方式为UTF-8
data = bytes(urllib.parse.urlencode({'hello':'python'}),encoding='utf-8')
#创建Request对象
r = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
response = urllib.request.urlopen(r)
print(response.read().decode('utf-8'))