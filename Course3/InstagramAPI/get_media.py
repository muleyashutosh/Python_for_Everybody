import requests 
import json
from get_token import get_access_token_user_id

def get_media(access_token):
    base_url = 'https://graph.instagram.com/me/media?'
    params = {}
    params['access_token'] = access_token
    params['fields'] = 'caption,id,media_type,media_url,thumbnail_URL,timestamp,username'
    
    data = requests.get(base_url, params = params)
    js = json.loads(data.text)
    return js

if __name__ == '__main__':
    access_token, user_id = get_access_token_user_id()
    js = get_media(access_token)
    print(json.dumps(js, indent = 4))
