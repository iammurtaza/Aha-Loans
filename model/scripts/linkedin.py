
# coding: utf-8

# In[136]:


import json,pandas as pd,sys,datetime,re


# In[349]:


args='{"token":"AQVaPxJrvgYHltSSdeJGQl7jhU-FOf1QStpKgF0NjeWIHxHLRTKH9XHefvx3lvebHHft7RFiAQqqcuWlIpL-3_lX8Wtd-UBwPr799fcIKWUtynMmbHmWtgdQi5tFwmXu_WS5vfIkvj-TX50ZLmzp1ewn7mbJFuYPiFmM1HAgR_tHAEuZKmuM6Roi9SYZSs17YHY6STkOSSClKWb8wQ2D3mjOf45FYa273IcUentTZHKvFxVoZiATCqvdrgn2W8-B570fP4JVzMhh2qxgNSZV4UqEpzMvQdXa11nPvoz_kq0Y2xs1PaFpGxcKCn7c5OAufzYpvNe8XwHZEbOujcTqwZP3GQrQSw","refreshToken":null,"expiresIn":5183999,"id":"1iUqh2wTIA","nickname":null,"name":"Suneel Kumar Rajpoot","email":"suneelweb15@gmail.com","avatar":"https:\/\/media.licdn.com\/dms\/image\/C4D03AQHZTZnv_sKv6A\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=tUwxDAeQ0fCmFQbUgOuW7FYmNUVcROMH_280pPxWcM4","user":{"apiStandardProfileRequest":{"headers":{"_total":1,"values":[{"name":"x-li-auth-token","value":"name:UUqR"}]},"url":"https:\/\/api.linkedin.com\/v1\/people\/1iUqh2wTIA"},"currentShare":{"author":{"firstName":"Suneel Kumar","id":"1iUqh2wTIA","lastName":"Rajpoot"},"comment":"","id":"s6081331427444613120","source":{"serviceProvider":{"name":"FLAGSHIP"}},"timestamp":1449902397000,"visibility":{"code":"anyone"}},"emailAddress":"suneelweb15@gmail.com","firstName":"Suneel Kumar","formattedName":"Suneel Kumar Rajpoot","headline":"SR.PHP Developer, Laravel Expert, Full Stack PHP Developer, Opencart Developer, Amazon Web Services (AWS)","id":"1iUqh2wTIA","industry":"Information Technology and Services","lastName":"Rajpoot","location":{"country":{"code":"in"},"name":"Noida Area, India"},"numConnections":500,"numConnectionsCapped":true,"pictureUrl":"https:\/\/media.licdn.com\/dms\/image\/C4D03AQHZTZnv_sKv6A\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=tUwxDAeQ0fCmFQbUgOuW7FYmNUVcROMH_280pPxWcM4","pictureUrls":{"_total":1,"values":["https:\/\/media.licdn.com\/dms\/image\/C4D00AQEL0Yxaq7lGpA\/profile-originalphoto-shrink_900_1200\/0?e=1529661600&v=beta&t=iVwgnH2-8pCGMmBrsyGAllQxaRXeiGQan4ti3Z0NnBA"]},"positions":{"_total":3,"values":[{"company":{"id":15217245,"industry":"Financial Services","name":"Gullakh.com","size":"2-10","type":"Privately Held"},"id":1012766236,"isCurrent":true,"location":{"country":{"code":"in","name":"India"},"name":"Noida Area, India"},"startDate":{"month":5,"year":2017},"title":"Senior Software Engineer"},{"company":{"id":5038819,"industry":"Retail","name":"MyFlowerTree.com","size":"51-200","type":"Privately Held"},"id":705779842,"isCurrent":true,"location":{"country":{"code":"in","name":"India"},"name":"New Delhi Area, India"},"startDate":{"month":6,"year":2015},"title":"Senior Software Developer(PHP, Laravel, eCommerce)"},{"company":{"name":"Trust Payments Ltd"},"id":684919439,"isCurrent":true,"location":[],"startDate":{"month":6,"year":2015},"summary":"As a software Developer, I will support service specialists in performing problem determination and analysis on client systems Depending on the severity level of a problem, I will be required to work directly with clients through conference calls or on site visits and provide in sight and feedback regarding the client environment to the development organization and be responsible for existing and new product development.","title":"Senior Software Developer(laravel Framework)"}]},"publicProfileUrl":"https:\/\/www.linkedin.com\/in\/suneelrajpoot","siteStandardProfileRequest":{"url":"https:\/\/www.linkedin.com\/profile\/view?id=AAoAAAUvUs8Bxt2sJqHoqzokhQvfm16dmNgtSnE&authType=name&authToken=UUqR&trk=api*a5274615*s5592855*"},"summary":"Currently working as a Sr. Software Developer. My role function requires to develop code using programming specifications, high level design documents and implement the identified components based on client requirements. Its also ensure that the implemented components are unit tested and ready to beintegrated into the product. You will provide defect fixes identified by theverification team during the software development life cycle and be exposed to projects across different domains.\n\nAs a software Developer, I will support service specialists in performing problem determination and analysis on client systems Depending on the severity level of a problem, I will be required to work directly with clients through conference calls or on site visits and provide in sight and feedback regarding the client environment to the development organization and be responsible for existing and new product development.\n\nI have completed project on several platform \u2013 php, mysql, sql server 2005\/2008, oops, Joomla, Magneto, opencart, oscommerce, wordpress, DotNetNuke, virtue mart, phpfox, asp.net."},"avatar_original":"https:\/\/media.licdn.com\/dms\/image\/C4D00AQEL0Yxaq7lGpA\/profile-originalphoto-shrink_900_1200\/0?e=1529661600&v=beta&t=iVwgnH2-8pCGMmBrsyGAllQxaRXeiGQan4ti3Z0NnBA"}'


# In[350]:


args=args.replace('null','\"null\"') 
value=json.loads(args,strict=False)


# In[351]:


total_score=0


# In[352]:


industryScore=pd.read_csv('industryscore.csv')
companyList=pd.read_csv('comapnyList.csv')
locationList=pd.read_csv('locationList.csv')


locationList.set_index("Branch Name",inplace=True)
companyList.set_index("CATEGORY",inplace=True)
industryScore.set_index('Score',inplace=True)


# In[353]:


if(value['user']['location'] and value['user']['location']['name']):
    area=value['user']['location']['name'].split(',')[0].split(' ')[:-1]
    ccode=value['user']['location']['country']['code']
    location=" ".join(area).strip()
    try:
        idx=locationList.loc[locationList['City'].values == location]['Location type PL'][0]
        #print(total_score)
        if(idx=='Type A PL'):total_score+=100
        elif(idx=='Type B PL'):total_score+=50
        else:pass
    except:
        pass
print(total_score)
    


# In[370]:


if(value['user']['positions'] and value['user']['positions']['_total'] is not 0 ):
    pos=value['user']['positions']['values']
    start_month=0
    start_year=0
    company_name=0
    for item in pos:
        if(item['company']):
            company_name=item['company']['name']
        elif(item['startDate']):
            start_month=item['startDate']['month']
            start_year=item['startDate']['year']
        else:pass

try:
    now=datetime.datetime.now()
    years_passed=now.year-int(start_year)
    if(years_passed==0):pass
    elif(years_passed <=1):total_score+=10
    elif(years_passed>1 and years_passed<=2):total_score+=20
    elif(years_passed>2 and years_passed<=3):total_score+=30
    elif(years_passed>3 and years_passed<=5):total_score+=40

    else:total_score+=50

except:
    pass




try:
    idx=companyList.index[companyList['COMPANY NAME'].values == company_name][0]
    if(idx == 'A+'):total_score+=100
    elif(idx == 'C1000'):total_score+=80
    elif(idx == 'Cat A'):total_score+=60
    elif(idx == 'Cat B'):total_score+=40
    elif(idx == 'Cat G'):total_score+=20
    else:pass
    
except:
    pass
total_score


# In[355]:


if(value['user']['industry']):
    industry=value['user']['industry']
    try:
        idx=industryScore.index[industryScore['Industry']== industry][0]
        total_score+=idx
        
    except:pass
else:pass    
    
total_score    


# In[356]:


if (value['user']['headline']):
    
    try:
        headline=value['user']['headline'].lower()
        looking='looking'
        _for='for'
        job='job'
        contains_1=re.compile(looking.lower())
        contains_2=re.compile(_for.lower())
        contains_3=re.compile(job.lower())
        if(contains_1.search(headline) and contains_2.search(headline) and contains_3.search(headline) ):pass
        elif(contains_1.search(headline) and contains_3.search(headline)):pass
        elif(contains_1.search(headline) and contains_2.search(headline)):total_score+=30
        else:total_score+=50    
        
    except: 
        pass
total_score


# In[357]:


if(value['user']['numConnections']):
    if(value['user']['numConnectionsCapped']):
        total_score+=50
    else:
        total_score+=int (int(value['user']['numConnections'])/10)
total_score       


# In[358]:


if(value['name'] and value['email']):
    try:
        first_name=value['name'].split()[0]
        last_name=value['name'].split()[1]
        email=value['email']
        contains_f=re.compile(first_name.lower())
        contains_l=re.compile(last_name.lower())
        if(contains_f.search(email.lower()) and contains_l.search(email.lower()) ):total_score+=50
        elif(contains_f.search(email.lower()) or contains_l.search(email.lower())):total_score+=25
        else:pass    
    except:pass
total_score
last_name


# In[359]:


total_score

