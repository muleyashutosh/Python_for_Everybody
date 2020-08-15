import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
uh = urllib.request.urlopen(url).read().decode()
print('Retrieving', url)
print('Retrieved', len(uh), 'characters.')
js = json.loads(uh)

users = js['comments']
sums = 0
count = 0
for user in users:
    sums += user['count']
    count += 1

print('Count:', count)
print('Sum:', sums)