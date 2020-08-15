import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter URL - ")
xml = urllib.request.urlopen(url).read().decode()
print('Retrieving', url)
print('Retrieved', len(xml),'characters')
tree = ET.fromstring(xml)
#print(xml)
lst = tree.findall('.//count')
total = 0
count = 0
for item in lst:
    total += int(item.text)
    count += 1
print('Count:', count)
print('Sum:', total)
