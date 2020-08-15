import urllib.request, urllib.parse, urllib.error
import json
from twurl import augment
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    accn = input("Enter Username:- ")
    if len(accn) < 1: break

    url = augment('https://api.twitter.com/1.1/friends/list.json',
                    {'screen_name': accn, 'count': '80'})
    print('Retrieving: ', url)
    uh = urllib.request.urlopen(url, context = ctx)

    data = uh.read().decode()
    headers = dict(uh.getheaders())
    print('Remaining Request: ', headers['x-rate-limit-remaining'])
    
    js = json.loads(data)
    x = open('output.json', 'w')
    x.write(json.dumps(js,indent = 4))
    #print(json.dumps(js, indent = 2))
    users = js['users']
    for user in users:
        print('-------------------------------')
        print('Screen-Name: ', user['screen_name'])
        if 'status' not in user:
            print('\tNO STATUS UPDATES')
        else:
            print('\tStatus: ', user['status']['text'] )
        print('\tNo. Of Followers: ', user['followers_count'])
        print('\tNo. Of Friends: ', user['friends_count'])
        print('\tVerified: ', user['verified'])
        print('-----------------------------')

