import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os
import pandas as pd

data=pd.read_csv('index.csv',usecols=['CIN','Name','City','Status'])
data.drop(['Status','City'],axis=1,inplace=True)

for i in range(332056):
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




        

