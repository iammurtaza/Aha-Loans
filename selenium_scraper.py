import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os
import pandas as pd

url="https://www.instafinancials.com/company/aaradhya-infraproperties-private-limited/U70109WB2012PTC172631"
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
content=driver.page_source
soup=BeautifulSoup(content,'lxml')
for i in range(30):
	table=soup.find_all('table')[i]
	print(i)
	print('\n')
	print(table)
	print('\n\n\n\n')

"""
soup=BeautifulSoup(content,'lxml')
tables=soup.find_all('table',class_='table table-striped no-ms table table-striped no-margins report-block')

for table in tables:
	rows=table.find_all('tr')
	for tr in rows:
		td=tr.find_all('td')
		row=[i.text for i in td]
		print(1)

"""