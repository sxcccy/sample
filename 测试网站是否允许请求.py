import urllib.request
import urllib.error
from urllib.request import urlopen
request=urllib.request.Request('http://www.thevapingforum.com/Forum-General-Discussion')
try:
    urllib.request.urlopen(request)
    print('可以访问')
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
