from bs4 import BeautifulSoup
from googlesearch import search

import urllib3
import re
import requests

bscScanURL = "https://bscscan.com/address/"
text = "site:poocoin.app"
contracts = []
for url in search(text, stop=20, tbs='qdr:d'):
    contract = url.split('/')[-1]
    contracts.append(contract)
    currentContractURL = bscScanURL+contract

    http = urllib3.PoolManager()
    response = requests.get(currentContractURL)
    soup = BeautifulSoup(response.text, "lxml")
    countTicks =0
    for link in soup.findAll('i', class_="fa fa-check-circle text-success"):
        countTicks += 1
    if countTicks == 0:
        print(contract+': NO VERIFIED')
    elif countTicks == 1:
        print(contract+': HALF VERIFIED')
    elif countTicks == 2:
        print(contract+': VERIFIED')
    else:
        print(countTicks)



print(contracts)
