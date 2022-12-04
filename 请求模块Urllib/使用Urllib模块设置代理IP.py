from urllib import request

url = 'http://www.python.org/get'
#创建代理IP
proxy_handler = request.ProxyHandler({'http':'182.139.110.128:9000'})
#创建opener对象
opener = request.build_opener(proxy_handler)
response = opener.open(url, timeout=300)
print(response.read().encode('utf-8'))