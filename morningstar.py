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

url = "https://financials.morningstar.com/finan/financials/getFinancePart.html?=&callback=jsonp1613684163698&t=0P0000034A&region=usa&culture=en-US&cur=&order=asc&_=1613684163765"
r= requests.get(url)
data=r.text
#print(data)
soup=BeautifulSoup(data)
print(soup.prettify())
