from urllib import request
from http import cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://site2.rjkflm.com:666/index/index/index.html'
cookie_file = 'cookie.txt'
cookie = cookiejar.LWPCookieJar()   #创建LWPCookieJar对象
#读取Cookie文件内容
cookie.load(cookie_file,ignore_expires=True,ignore_discard=True)
#生成Cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#创建opener对象
opener = request.build_opener(handler)
response = opener.open(url)
print(response.read().decode('utf-8'))