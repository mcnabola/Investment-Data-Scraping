import requests
from bs4 import BeautifulSoup 
import csv 
import pandas as pd

#kellogs - Nyse
url = "https://financials.morningstar.com/finan/financials/getFinancePart.html?=&callback=jsonp1613684163698&t=0P0000034A&region=usa&culture=en-US&cur=&order=asc&_=1613684163765"

#visa - nasdaq
#https://financials.morningstar.com/finan/financials/getFinancePart.html?=&callback=jsonp1613686472031&t=0P0000CPCP&region=usa&culture=en-US&cur=&order=asc&_=1613686472128



r= requests.get(url)
data=r.text
#print(data)
soup=BeautifulSoup(data, 'lxml') #add lxml to avoid the error
#print(soup.prettify())- prints a nice formatted html code

table = soup.find('table')
table_rows = table.find_all('tr')

l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td if tr.text.strip()]
    #row = [tr.text for tr in td]
    if row:
        l.append(row)

g = pd.DataFrame(l, columns=["2010-12","2011-12","2012-12","2013-12","2014-12","2015-12","2016-12","2017-12","2018-12","2019-12","TTM"])
#pop the last row *indicates calender year end data information
g = g.drop([15])#drops a row rows/=col
print(g)

