
import urllib.request, urllib.parse, urllib.error
import re
from dotenv import load_dotenv
import os
import webbrowser



def get_authorize_code():
    load_dotenv()
    base_url = 'https://api.instagram.com/oauth/authorize?'
    parms = {}
    parms['client_id'] = os.getenv('Insta_client_id')
    parms['redirect_uri'] = 'https://github.com/muleyashutosh'
    parms['scope'] = 'user_profile,user_media'
    parms['response_type'] = 'code'
    url = base_url + urllib.parse.urlencode(parms)
    print(url)
    webbrowser.open(url,new = 2)
    print("\nOpen the Above URL and Authorize your app and PASTE the URL of Redirected Website")
    code_url  = input()
    code = re.findall('\?code=(.*)\#\_$',code_url)
    return code[0]

if __name__ == '__main__':
    print(get_authorize_code())
