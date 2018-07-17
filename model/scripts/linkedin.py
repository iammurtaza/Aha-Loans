
# coding: utf-8

# In[136]:


import json,pandas as pd,sys,datetime,re


# In[349]:

def main():
    args='{"token":"AQVv53iAgSdGNzlVuFKBYHtTiNy08Tc_zRB4se0oUqt2YNKo9dyU9arc66fGQLA6uFELZY0pfs49izRDMn_jQZLmYqRhZxUy_hXrhwlt2M-G4-ed1nt3zgrXcVwwCXh6Lv2oqeBP_EmM1vWrx0HUWnA5UW7hTW5Q5OuOr2j7wOqGtTjG88rP_gGhOZGorNfSTBM11ZX9Qdel6UP_70SIctQBWUC-E1FYqjJTKekbUkfycauvFKD4BoZ9lAn3P1zsBcN7BRBR4OnQbYjvPzTpHhObr5jw6R5NKNrp46zG-4BPZ6Em4ULA2NAjThw75jjfBrF3N4ft7tVeP_CoaSbnA5XPa5MZ0A","refreshToken":null,"expiresIn":5183999,"id":"hd-yfhQVIy","nickname":null,"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","avatar":"https:\/\/media.licdn.com\/dms\/image\/C5103AQF05Rl4FuBsyg\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=IfXypj05SD0P9_YvF5ZOHz0wmzsFt7NrpEHnNgls9lw","user":{"apiStandardProfileRequest":{"headers":{"_total":1,"values":[{"name":"x-li-auth-token","value":"name:e9LX"}]},"url":"https:\/\/api.linkedin.com\/v1\/people\/hd-yfhQVIy"},"emailAddress":"sunnyyasser@gmail.com","firstName":"Sunny","formattedName":"Sunny Yasser","headline":"Data Science enthusiast","id":"hd-yfhQVIy","industry":"Computer Software","lastName":"Yasser","location":{"country":{"code":"in"},"name":"New Delhi Area, India"},"numConnections":168,"numConnectionsCapped":false,"pictureUrl":"https:\/\/media.licdn.com\/dms\/image\/C5103AQF05Rl4FuBsyg\/profile-displayphoto-shrink_100_100\/0?e=1534982400&v=beta&t=IfXypj05SD0P9_YvF5ZOHz0wmzsFt7NrpEHnNgls9lw","pictureUrls":{"_total":1,"values":["https:\/\/media.licdn.com\/dms\/image\/C4E04AQG6jYL-4DmARg\/profile-originalphoto-shrink_450_600\/0?e=1534982400&v=beta&t=DaYuHuVZSeM5P4mw5tM8jyCr8LgcpJTRPz9ja5JusY8"]},"positions":{"_total":1,"values":[{"company":{"name":"Aha! Loans , IIM Lucknow"},"id":1323599578,"isCurrent":true,"location":{"country":{"code":"in","name":"India"},"name":"Noida Area, India"},"startDate":{"month":5,"year":2018},"summary":"Involved in the development of a credit risk analysis model using the social footprint of a person.","title":"Data Scientist Intern"}]},"publicProfileUrl":"https:\/\/www.linkedin.com\/in\/sunny-yasser","siteStandardProfileRequest":{"url":"https:\/\/www.linkedin.com\/profile\/view?id=AAoAACNvdAMBJFiNOLYmOX7P6a96U2pUYxO_EKc&authType=name&authToken=e9LX&trk=api*a5274615*s5592855*"},"summary":"An inquisitive, self-taught machine learning enthusiast, I look forward to collaborating in the fields of  AI and data science.\nI have experience in the development and deployment of machine learning models, including RNNs and CNNs. Proficient in Python, Pandas, Numpy, Sklearn, Keras and Tensorflow. I have experience with statistical analysis too including ROC curves, chi-squared test, and am well versed in hyperparameter tuning and exploratory data analysis.\nI also have experience in Java and C++ programming, with knowledge of data structures and algorithms. \nLooking forward to connect with opportunities in the above fields."},"avatar_original":"https:\/\/media.licdn.com\/dms\/image\/C4E04AQG6jYL-4DmARg\/profile-originalphoto-shrink_450_600\/0?e=1534982400&v=beta&t=DaYuHuVZSeM5P4mw5tM8jyCr8LgcpJTRPz9ja5JusY8"}'


    # In[350]:


    args=args.replace('null','\"null\"') 
    value=json.loads(args,strict=False)


    # In[351]:


    industryScore=pd.read_csv('industryscore.csv')
    companyList=pd.read_csv('comapnyList.csv')
    locationList=pd.read_csv('locationList.csv')


    locationList.set_index("Branch Name",inplace=True)
    companyList.set_index("CATEGORY",inplace=True)
    industryScore.set_index('Score',inplace=True)

    print(link_score(value))

# In[353]:

def link_score(value):
    total_score=0
    if(value['user']['location'] and value['user']['location']['name']):
        area=value['user']['location']['name'].split(',')[0].split(' ')[:-1]
        ccode=value['user']['location']['country']['code']
        location=" ".join(area).strip()
        #print(locationList.loc[locationList['City'].values == location]['Location type PL'][0])
        try:
            idx=locationList.loc[locationList['City'].values == location]['Location type PL'][0]
            if(idx=='Type A PL'):total_score+=100
            elif(idx=='Type B PL'):total_score+=50
            else:pass
        except:
            pass
    

   # print(total_score)
        


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


    # In[355]:


    if(value['user']['industry']):
        industry=value['user']['industry']
        try:
            idx=industryScore.index[industryScore['Industry']== industry][0]
            total_score+=idx
            
        except:pass
    else:pass    
        
        


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



    # In[357]:


    if(value['user']['numConnections']):
        if(value['user']['numConnectionsCapped']):
            total_score+=50
        else:
            total_score+=int (int(value['user']['numConnections'])/10)


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


    return(total_score)

if __name__ == '__main__':
    industryScore=pd.read_csv('industryscore.csv')
    companyList=pd.read_csv('comapnyList.csv')
    locationList=pd.read_csv('locationList.csv')


    locationList.set_index("Branch Name",inplace=True)
    companyList.set_index("CATEGORY",inplace=True)
    industryScore.set_index('Score',inplace=True)
    main()