from bs4 import BeautifulSoup
from googlesearch import search

import urllib3
import re
import requests

bscScanURL = "https://bscscan.com/address/"
bscScanURL2 = "https://bscscan.com/token/"
text = "site:poocoin.app"
contracts = []
coins = {}

fake_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url="https://poocoin.app/tokens/0x3d29aa78fb558f84112bbc48a84f371147a920c9"


def printShitCOinsDict(coins):
    for coin in coins:
        print(coin+':\t\t'+coins[coin]['verified'])
        print('\t\t'+coins[coin]['name'])
        print('\t\t'+coins[coin]['contract'])
        print('\t\t'+coins[coin]['chart'])
        print()
        print()


for url in search(text, stop=5, tbs='qdr:d'):
    ## Find in bscScan to verify it
    contract = url.split('/')[-1]
    contracts.append(contract)
    currentContractURL = bscScanURL+contract

    http = urllib3.PoolManager()
    response = requests.get(currentContractURL)
    soup = BeautifulSoup(response.text, "lxml")
    countTicks =0
    for link in soup.findAll('i', class_="fa fa-check-circle text-success"):
        countTicks += 1

    if countTicks > 0:
        newCoin = {}
        newCoin['contract'] = contract
        newCoin['chart'] = url
        if countTicks == 1:
            newCoin['verified'] = 'HALF VERIFIED'
        elif countTicks == 2:
            newCoin['verified'] = 'VERIFIED'
        else:
            newCoin['verified'] = countTicks

        ## Get more info
        name = ''   
        currentContractURL2 = bscScanURL2+contract
        response = requests.get(currentContractURL2)
        soup = BeautifulSoup(response.text, "lxml")
        for link in soup.findAll('title'):
            code = link.contents[0].split('(')[1].split(')')[0]
            newCoin['name'] = link.contents[0].split('\t')[1].split('(')[0].strip()
            newCoin['code'] = code
        coins[code] = newCoin

printShitCOinsDict(coins)
