import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

wurl = input('Enter URL: ')
witers = int(input('Enter count: '))
wpos = int(input('Enter position: '))


def getlink(thisurl, xiters, xpos):
    html = urllib.request.urlopen(thisurl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    tags = soup('a')
    for tag in tags:
     link = tag.get('href', None)
     print(link)
     links.append(link)
    if xiters > 1:
        print("the point is", links[xpos - 1])
        return getlink(links[xpos - 1], xiters - 1, xpos)
    else:
        z = links[xpos - 1]
        return z

r = getlink(wurl, witers, wpos)
myreg = "known_by_(\w+)"
z = re.findall(myreg, r)
print(z)
