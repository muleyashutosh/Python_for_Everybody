import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL- ")
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data,'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
