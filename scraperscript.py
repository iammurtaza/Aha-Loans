import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import pandas


df=pandas.DataFrame(index=np.arange(0,12060),columns=['No.','Company','Region','Status'])
x=1

for i in range(9000,10169):
    url="https://www.zaubacorp.com/company-list/status-Active/age-D/p-"+str(i)+"-company.html"
    content=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(content,'lxml')
    table=soup.table
    table_rows=table.find_all('tr')
    for tr in table_rows:
        td=tr.find_all('td')
        row=[i.text for i in td]
        if(len(row) is not 0):
            df.loc[x]=row
            x+=1
            print(row,x)
		
print(df)



df.to_csv('index.csv',sep='\t',mode='a',encoding='utf-8',index=False)
    
