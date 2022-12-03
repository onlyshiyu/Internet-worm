from urllib import request

url = 'https://www.baidu.com/'
response = request.urlopen(url=url,timeout=0.5)
print(response.read().decode('utf-8'))