import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from bs4 import BeautifulSoup
import re
import os

url='https://www.instafinancials.com/company/white-lion-entertainment-private-limited/U74120MH2011PTC223737'        

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
source=driver.page_source
soup=BeautifulSoup(source,'lxml')
table=soup.table
table_rows=table.find_all('tr')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)


url='https://www.instafinancials.com/company/white-lion-entertainment-private-limited/U74120MH2011PTC223737'        
driver.get(url)
source=driver.page_source
soup=BeautifulSoup(source,'lxml')
table=soup.table
table_rows=table.find_all('tr')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)