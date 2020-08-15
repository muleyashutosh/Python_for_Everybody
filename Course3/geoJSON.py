import urllib.request, urllib.parse, urllib.error
import json

location = input("Enter Location: ")
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
parms = {'address': location, 'key': api_key}
url = serviceurl + urllib.parse.urlencode(parms)

uh = urllib.request.urlopen(url)
print("Retrieving", url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
print('Place_id', js['results'][0]['place_id'])