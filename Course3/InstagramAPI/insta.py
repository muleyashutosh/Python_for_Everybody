
import urllib.request, urllib.parse, urllib.error
import requests
import json
import os
from get_token import get_access_token_user_id
from get_media import get_media
import re
from dotenv import load_dotenv
load_dotenv()

access_token, user_id = get_access_token_user_id()

base_url = 'https://graph.instagram.com/'

user_id = '17841404689087341'
base_url += user_id + '?'
parms = {}
parms['fields'] = 'id,username,account_type,ig_id,media_count'
parms['access_token'] = access_token

#url = base_url + urllib.parse.urlencode(parms)

response = requests.get(base_url, params = parms)

js = json.loads(response.text)
os.system('clear')
print("_______________________________________________")
print("YOUR ACCOUNT DETAILS:___\n")
print('ID: ', js['id'])
print('USERNAME: ', js['username'])
print('ACCOUNT_TYPE: ', js['account_type'])
print('IG_ID: ', js['ig_id'])
print('MEDIA_COUNT: ', js['media_count'])
print("_______________________________________________")

media = get_media(access_token)
count = 1
print('\nYOUR MEDIA DETAILS:---')
    
for item in media['data']:
    print('MEDIA NO: ', count,':--')
    cap = re.findall('([\w\s]*)?', item['caption'])[0]
    print('\tCAPTION: ', cap)
    print("\tID: ", item['id'])
    print('\tMEDIA_TYPE: ', item['media_type'] )
    print('\tMEDIA_URL: ', item['media_url'])
    date = re.findall('(.*)?T', item['timestamp'])[0]
    time = re.findall('T(.*)?\+', item['timestamp'])[0]
    print('\tDATE(YYYY-MM-DD): ', date)
    print('\tTIME(HH:MM:SS): ', time)
    print('----------------------------------------------------------------')
    count += 1



