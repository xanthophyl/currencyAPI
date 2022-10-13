#import libraries to handle request to api
import requests
import json
import pprint


# api url for request 
url = 'yourapiurlrightthere'
response = requests.get(url)

# retrive response in json format
data = response.json()
Display = {}

def get_currency(value):
    new_value = data['data'][value.upper()]
    print(new_value)

get_currency('BTC')