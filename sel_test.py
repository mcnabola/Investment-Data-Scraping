from lxml import html
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://financials.morningstar.com/ratios/r.html?t=AMD&region=USA&culture=en_US')
tree = html.fromstring(driver.page_source)
driver.quit()
rev = tree.cssselect('td[headers^=Y0]')[0].text
print(rev)
