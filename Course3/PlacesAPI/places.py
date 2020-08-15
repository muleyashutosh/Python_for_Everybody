import requests
from dotenv import load_dotenv
import os
load_dotenv()

baseurl = 'https://maps.googleapis.com/maps/api/place/details/json?'
key = os.getenv('GOOGLE_API_KEY')

parameters = {}
parameters['key'] = key
place = input('Enter Place to Search: ')
parameters['input'] = place
parameters['inputtype'] = 'textquery'
parameters['language'] = 'en'
parameters['fields'] = 'address_component,name,geometry,rating,opening_hours'

urlhandle = requests.get(baseurl,params=parameters)
print(urlhandle.text)


