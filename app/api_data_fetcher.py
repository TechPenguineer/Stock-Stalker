import requests
import json



def CallAPIData():
    data = open('app/api/markets.json', 'r')
    MARKET = json.load(data)
    API_URL = (MARKET['NYSC_F'])

    response = requests.get(API_URL)
    API_DATA = response.text
    print(API_DATA)

CallAPIData()