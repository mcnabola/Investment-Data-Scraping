import requests
from bs4 import BeautifulSoup 
import csv 
import pandas as pd

names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]

for i in range(0,10):
  CryptoCurrenciesUrl = "https://in.finance.yahoo.com/cryptocurrencies?offset="+str(i)+"&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=50"
  r= requests.get(CryptoCurrenciesUrl)
  data=r.text
  soup=BeautifulSoup(data)

  for listing in soup.find_all('tr', attrs={'class':'SimpleDataTableRow'}):
    for name in listing.find_all('td', attrs={'aria-label':'Name'}):
      names.append(name.text)
    for price in listing.find_all('td', attrs={'aria-label':'Price (intraday)'}):
      prices.append(price.find('span').text)
    for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
    for percentChange in listing.find_all('td', attrs={'aria-label':'% change'}):
      percentChanges.append(percentChange.text)
    for marketCap in listing.find_all('td', attrs={'aria-label':'Market cap'}):
      marketCaps.append(marketCap.text)
    for totalVolume in listing.find_all('td', attrs={'aria-label':'Total volume all currencies (24 hrs)'}):
      totalVolumes.append(totalVolume.text)
    for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Circulating supply'}):
      circulatingSupplys.append(circulatingSupply.text)

print(names)

pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})

names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]
 
CryptoCurrenciesUrl = "https://in.finance.yahoo.com/currencies"
r= requests.get(CryptoCurrenciesUrl)
data=r.text
soup=BeautifulSoup(data)
 
counter = 40
for i in range(40, 404, 14):
   for listing in soup.find_all('tr', attrs={'data-reactid':i}):
      for name in listing.find_all('td', attrs={'data-reactid':i+3}):
         names.append(name.text)
      for price in listing.find_all('td', attrs={'data-reactid':i+4}):
         prices.append(price.text)
      for change in listing.find_all('td', attrs={'data-reactid':i+5}):
         changes.append(change.text)
      for percentChange in listing.find_all('td', attrs={'data-reactid':i+7}):
         percentChanges.append(percentChange.text)
pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})


