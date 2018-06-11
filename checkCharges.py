import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait


data=pd.read_csv('index.csv',usecols=['CIN','Name','City','Status'])
data.drop(['Status','City'],axis=1,inplace=True)


driver=webdriver.Chrome()
driver.set_network_conditions(
    offline=False,
    latency=5,  # additional latency (ms)
    download_throughput=50 * 1024,  # maximal throughput
    upload_throughput=50 * 1024)  # maximal throughput


for i in range(2,3356):
	name=data.Name.iloc[i]
	name=str(name).lower()
	cin=data.CIN.iloc[i]
	words=name.split()
	urlname=""
	for word in words:
		urlname=urlname+word+"-"
	urlname=urlname[:-1]	

	url='https://www.instafinancials.com/company/'+urlname+'/'+str(cin)	
	print(url)
	
	driver.implicitly_wait(10)
	time.sleep(9)
	driver.get(url)
	
	"""
	content=driver.page_source
	soup=BeautifulSoup(content,'lxml')
	tableIndices=[14,0,7]

	table=soup.find_all('table')[14]
	
	print(i)
	print('\n')
	print(table)
	print('\n\n\n\n')
	rows=table.find_all('tr')
	
	rows=table.find_all('tr')

	for tr in rows:
		td=tr.find_all('td')
		row=[i.text for i in td]
		print(row)



"""

        
