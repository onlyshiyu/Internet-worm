from urllib import request
from urllib import error

url = 'http://site2.rjkflm.com:666/123index.html'
try:
    response = request.urlopen(url=url)
except error.URLError as error:
    print(error.reason)