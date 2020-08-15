import requests
import urllib.parse
import json
import webbrowser
from dotenv import load_dotenv
import os
import re


load_dotenv()
def get_auth_code():
    baseurl = 'https://accounts.spotify.com/authorize?'
    params = {}
    params['client_id'] = os.getenv('Spotify_client_id')
    params['response_type'] = 'code'
    params['redirect_uri'] = 'https://github.com/muleyashutosh'

    url = baseurl + urllib.parse.urlencode(params)
    while True:
        webbrowser.open(url,new = 2)
        print('\nPaste the URL of the Redirected WebPage after Authorization...\n')

        auth_url = input()
        if 'error=access_denied' in auth_url:
            print('Please Provide Authorization Permission!')
        else:
            break
    code = re.findall('\?code\=(.*)$',auth_url)[0]
    return code

def get_access_token_refresh_token():
    baseurl = 'https://accounts.spotify.com/api/token'
    params = {}
    params['client_id'] = os.getenv('Spotify_client_id')
    params['client_secret'] = os.getenv('Spotify_client_secret')
    params['grant_type'] = 'authorization_code'
    params['code'] = get_auth_code()
    params['redirect_uri'] = 'https://github.com/muleyashutosh'

    while True:
        response = requests.post(baseurl,data = params)
        if 'Error' in response.text:
            file = open('response.html','w')
            file.write(response.text)
            webbrowser.open('response.html',new = 2)
        else:
            break
    js = json.loads(response.text)
    access_token = js['access_token']
    refresh_token = js['refresh_token']
    return (access_token, refresh_token)


if __name__ == '__main__':
    baseurl = 'https://api.spotify.com/v1/search'
    access_token = get_access_token_refresh_token()[0]
    params = {}
    params['q'] = input('Search : ')
    params['type'] = 'track'#artist'#playlist,track,show,episode'
    params['market'] = 'IN'
    params['limit'] = '5'
    auth = 'Bearer ' + access_token
    response = requests.get(baseurl, params = params, headers = {'Authorization' : auth })
    js = json.loads(response.text)
    print(json.dumps(js, indent=4))




