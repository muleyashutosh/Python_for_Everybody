import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
name = ''
while count >= 0:
    html = urllib.request.urlopen(url).read()
    print('Retrieving: ', url )
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[pos-1].get('href', None)
    if count == 1:
        name = tags[pos-1].contents[0]
    count -= 1
print(name)