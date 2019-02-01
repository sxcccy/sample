import urllib.request
import urllib.error
from urllib.request import urlopen
wangzhi=''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=wangzhi, headers=headers)
request=urllib.request.Request(req)
try:
    urllib.request.urlopen(request)
    print('可以访问')
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
