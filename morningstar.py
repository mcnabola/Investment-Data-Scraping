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


g = pd.DataFrame(l, columns=["2011-12","2012-12","2013-12","2014-12","2015-12","2016-12","2017-12","2018-12","2019-12", "2020-12","TTM"])
#pop the last row *indicates calender year end data information
g = g.drop([15]).drop(columns=["2020-12"])#drops a row rows/=col


col_names_list = ["Revenue USD Mil", "Gross Margin %","Operating Income USD Mil", "Operating Margin %", 
                "Net Income USD Mil", "Earnings Per Share USD", "Dividends USD", "Payout Ratio %", 
                "Shares Mil", "Book Value Per Share USD", "Operating Cash Flow USD Mil", 
                "Cap Spending USD Mil", "Free Cash Flow USD Mil", "Free Cash Flow Per Share USD", 
                "Working Capital USD Mil"]
g = g.transpose()           # swap rows with columns so that the columns can have names

print("Key Ratios Financial Data")

# rename the columns from plain indexes (0, 1, 2, 3...14) to column names
g = g.rename(columns = {i : col_names_list[i] for i in range(len(col_names_list))})
print(g.transpose())

# Remove the commas from numbers > 1000 and remove null values
g = g.replace("—", "", regex=True).replace(",", "", regex=True)

print()


# Select and display the data for the last 5 years from the FCF and FCF per share columns
print("Last 6 years for FCF")
print(g.tail(6)[["Free Cash Flow USD Mil", "Free Cash Flow Per Share USD"]])    # Note that our data isn't modified here


# Calculate the mean/average for the data above
last_5_fcf = pd.to_numeric(g.tail(5)["Free Cash Flow USD Mil"]).mean()
print()
print("Average 5 year FCF:\t\t\t\t      "+ str(last_5_fcf))


# Check how many cells in the column are empty
no_empt_cells = (g["Free Cash Flow Per Share USD"].values == '').sum()
# Take older values to have all 5 numbers for the average
# Cast g values as numbers, load values from the last rows and calculate the mean
last_5_per_share = pd.to_numeric(g.tail(5+no_empt_cells)["Free Cash Flow Per Share USD"]).mean()
print("Average 5 year FCF per share:\t\t\t       "+ str(last_5_per_share))   # cast mean as string/text
print()



# Use head(5) for the first 5 years
first_5_fcf = pd.to_numeric(g.head(5)["Free Cash Flow USD Mil"]).mean()
print("First 5 years average:\t\t\t\t      " + str(first_5_fcf))
print("Last 5 / First 5 years FCF:\t\t\t" + f"{(last_5_fcf / first_5_fcf): 0.9f}") # show 9 floating point digits



#book_val_chn = 0
#print("Book value change per year:\t\t\t\t")

earn_5_avg = (pd.to_numeric(g.tail(6)["Dividends USD"].drop(["TTM"])).mean())
print("Earnings 5 year average:\t\t\t       " + f"{earn_5_avg: 0.2f}")

payout_ratio_7_avg = pd.to_numeric(g.tail(7)["Payout Ratio %"]).mean()
print("7 year average payout ratio %:\t\t\t    " + f"{payout_ratio_7_avg: 0.4f}")

