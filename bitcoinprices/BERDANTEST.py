
from cryptos import *
import requests
from matplotlib import *
from numpy import * 
from bs4 import BeautifulSoup

URL = 'https://coinmarketcap.com/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')


priceofbitcoininus = soup.find(href="/currencies/bitcoin/markets/").get_text() 

#<a href="/currencies/bitcoin/markets/" class="cmc-link">$8,786.19</a>


print("Price of Bitcoin Right now in $US is %s"%(priceofbitcoininus))
#====================================================================


priceofetheriuminus = soup.find(href="/currencies/ethereum/markets/").get_text()

print("Price of Etherium Right now in $US is %s"%(priceofetheriuminus))
#<a href="/currencies/ethereum/markets/" class="cmc-link">$216.83</a>


#===============================================================

priceoflitecoininus = soup.find(href="/currencies/litecoin/markets/").get_text()
print("Price of LiteCoin Right now in $US is %s"%(priceoflitecoininus))


