import urllib.request, urllib.parse, urllib.error
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()


baseurl = 'https://www.googleapis.com/youtube/v3/videos?'
api_key = os.getenv('GOOGLE_API_KEY')


params = {}
params[ 'key'] = api_key
params[ 'part' ] = 'statistics'


pattern = '\?v\=(\w*)'
videoURL =  input('Enter URL: ')
id1 = re.findall(pattern, videoURL)
#print(id1)
params['id'] = id1[0]

url = baseurl + urllib.parse.urlencode(params)
print(url)
uh = urllib.request.urlopen(url)

data = uh.read().decode()
js = json.loads(data)
x = open('output.json','w')
x.write(json.dumps(js,indent = 4))

#print(json.dumps(js,indent = 4))
#print('\n')
print("\nSTATISTICS: ")
print('No. of Views:', js['items'][0]['statistics']['viewCount'])
print('No. of Likes:', js['items'][0]['statistics']['likeCount'])
print('No. of DisLikes:', js['items'][0]['statistics']['dislikeCount'])
print('No. of Comments:', js['items'][0]['statistics']['commentCount'])
