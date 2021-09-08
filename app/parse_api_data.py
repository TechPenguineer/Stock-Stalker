import json
from api_data_fetcher import CallAPIData
def ParseData():
    APID=CallAPIData()
    data = json.load(APID)
    #isStockClosed=data['Meta Data']
    print(data)

ParseData()