from urllib import request, parse
import http.cookiejar
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
#将表单数据类型转换为bytes类型，并设置编码方式为UTF-8
data = bytes(parse.urlencode({'user':'mrsoft','password':'mrsoft'}),encoding='utf-8')
cookie = http.cookiejar.CookieJar()
cookie_processor = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(cookie_processor)
response = opener.open(url,data=data)
response = json.loads(response.read().decode('utf-8'))['msg']
if response == '登录成功！':
    for i in cookie:
        print(i.name+'='+i.value)