from urllib import request, parse
import http.cookiejar
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
data = bytes(parse.urlencode({'username':'mrsoft','password':'mrsoft'}),encoding='utf-8')
cookie_file = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(cookie_file)
#生成cookie处理器
cookie_processor = request.HTTPCookieProcessor(cookie)
#创建opener对象
opener = request.build_opener(cookie_processor)
response = opener.open(url,data=data)
response = json.loads(response.read().decode('utf-8'))['msg']
if response == '登录成功！':
    cookie.save(ignore_discard=True, ignore_expires=True)