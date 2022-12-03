from urllib import request, error
import socket

url = 'https://www.baidu.com/'
try:
    response = request.urlopen(url=url,timeout=0.1)
    print(response.read().decode('utf-8'))
except error.URLError as error:
    if isinstance(error.reason,socket.timeout):
        print('当前任务超时，即将执行下一任务！')
