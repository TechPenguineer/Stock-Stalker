import requests
import json
import urllib.request
import urllib3
def CallAPIData():

    data = open('app/api/markets.json', 'r')
    MARKET = json.load(data)
    API_URL = (MARKET['NYSC_F'])

    res = urllib.request.urlopen(API_URL)
    print(res)
    return res

CallAPIData()