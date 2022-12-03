from urllib import request, parse

url = 'https://www.baidu.com/'
#将表单数据转换为bytes类型，并设置编码类型为UTF-8
data = bytes(parse.urlencode({'hello':'ShiYu'}),encoding='utf-8')
response = request.urlopen(url=url,data=data)
print(response.read().decode('utf-8'))