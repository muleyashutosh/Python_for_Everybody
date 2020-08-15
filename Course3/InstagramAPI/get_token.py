
import urllib.request, urllib.parse, urllib.error
import requests
import json
from authorize import get_authorize_code
from dotenv import load_dotenv
import os


def get_access_token_user_id():
    load_dotenv()
    base_url = 'https://api.instagram.com/oauth/access_token'
    parms = {}
    parms['client_id'] = os.getenv('Insta_client_id')
    parms['client_secret'] = os.getenv('Insta_client_secret')
    parms['grant_type'] = 'authorization_code'
    parms['redirect_uri'] = 'https://github.com/muleyashutosh'
    parms['code'] = get_authorize_code()

    #url = base_url + urllib.parse.urlencode(parms)
    response = requests.post(base_url, data = parms)

    js = json.loads(response.text)
    #data = json.dumps(js,indent = 4)
    access_token = js['access_token']
    user_id = js['user_id']
    
    return (access_token, user_id)

if __name__ == '__main__':
    access_token, user_id = get_access_token_user_id()
    print('Access_token: ', access_token)
    print('User_ID:', user_id)
