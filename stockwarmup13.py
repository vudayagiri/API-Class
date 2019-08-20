#!/usr/bin/python3

import requests
import time

def main():
    i=0
    apikey1 = (with open ('apikey','r') as api:).read()
        #apikey1 = api.read()
    print(apikey1)
    for i in range(4):
        mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=5min&apikey=TIYA7BDBBA4P8D4R"
        stockdata = requests.get(mylookup)
        amznstock = stockdata.json()
        amzn_last = amznstock["Meta Data"]["3. Last Refreshed"]
        #i += 1

        amznlatest = amznstock["Time Series (5min)"][amzn_last]
        print(amznlatest)
        
        time.sleep(20)
    


    #print(stocks)


main()



