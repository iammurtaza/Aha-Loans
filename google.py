
# coding: utf-8

# In[92]:


import re,json,sys,fuckit


# In[129]:


val='{"token":"ya29.GlvhBa4OkOcwM88bFGjpURKcnTz_rotWh-E_vcfwUBFjxH3LB98pbfjhIrU93b29jzLVXd2q1S50_0VEB63ikAJMy9m2U-1NQ4B2EHS8oex2yqNFAunY8r0wcaSx","refreshToken":null,"expiresIn":3600,"id":"101048662100544358927","nickname":null,"name":"Murtaza Hasan","email":"murtazaygenius@gmail.com","avatar":"https:\/\/lh3.googleusercontent.com\/-f-0iPgx913U\/AAAAAAAAAAI\/AAAAAAAAiu0\/EVHFonNZgdc\/photo.jpg?sz=50","user":{"kind":"plus#person","etag":"\"RKS4-q7QGL10FxltAebpjqjKQR0\/yx3dVB7XKtwptMf3qkRPK_Xp3KY\"","gender":"male","emails":[{"value":"murtazaygenius@gmail.com","type":"account"}],"urls":[{"value":"http:\/\/www.youtube.com\/user\/MhZnSO4","type":"otherProfile","label":"Murtaza Hasan"},{"value":"http:\/\/www.facebook.com\/mhznso4","type":"other","label":"mhznso4"}],"objectType":"person","id":"101048662100544358927","displayName":"Murtaza Hasan","name":{"familyName":"Hasan","givenName":"Murtaza"},"tagline":" \u03c0 ain\'t rational, kid! ","braggingRights":"Sports + Studies = All Rounder = Me !","aboutMe":"Different thinking .. different views .. what you see is what you won&#39;t get .. cause i am both introvert and outshining guy .. i haven&#39;t been able to figure out myself ! DON&#39;T KNOW ABOUT THE WORLD","relationshipStatus":"single","url":"https:\/\/plus.google.com\/+MurtazaHasanZaidi","image":{"url":"https:\/\/lh3.googleusercontent.com\/-f-0iPgx913U\/AAAAAAAAAAI\/AAAAAAAAiu0\/EVHFonNZgdc\/photo.jpg?sz=50","isDefault":false},"organizations":[{"name":"Bal Bharati School","type":"school","primary":false},{"name":"Bal Bharati Public School","type":"school","primary":false}],"placesLived":[{"value":"India"}],"isPlusUser":true,"language":"en_GB","circledByCount":0,"verified":false,"cover":{"layout":"banner","coverPhoto":{"url":"https:\/\/lh3.googleusercontent.com\/3mXQUfB9XOMjufr0wv6dyjrzeeqPJQu5PzU2dRdY3-V7WNROjFIapHwXfGFs49fGVREPaEAPjdpsJw=s630-fcrop64=1,00000000ffffffff","height":528,"width":940},"coverInfo":{"topImageOffset":0,"leftImageOffset":0}}},"avatar_original":"https:\/\/lh3.googleusercontent.com\/-f-0iPgx913U\/AAAAAAAAAAI\/AAAAAAAAiu0\/EVHFonNZgdc\/photo.jpg"}'


# In[130]:


value=val.replace('\\"','').replace('""','"').replace("\'","")


# In[131]:


json.loads(value,strict=False)


# In[132]:


def main():
    try:
        
        val='{"token":"ya29.Gl3hBbA3WDTjQrj4AxFm3UHqYMfF2mgpRHJ5oh7myM1lYiRyhym5dvJwxL1T6sfNjcGDeELJ1OyEyt0M-9TQgki9dN73eSAEwnZJ2HFAd86AsE6OhaDH9oHeJTTAu_Q","refreshToken":null,"expiresIn":3599,"id":"117137725249225792257","nickname":null,"name":"Akbar Ali","email":"akbarali0702@gmail.com","avatar":"https:\/\/lh6.googleusercontent.com\/-7qHRJbecjtk\/AAAAAAAAAAI\/AAAAAAAAAEc\/ywaoD1Y_Lus\/photo.jpg?sz=50","user":{"kind":"plus#person","etag":"\"RKS4-q7QGL10FxltAebpjqjKQR0\/0XNvPDppxL7u4w-RzRYioOpuLkY\"","gender":"male","emails":[{"value":"akbarali0702@gmail.com","type":"account"}],"objectType":"person","id":"117137725249225792257","displayName":"Akbar Ali","name":{"familyName":"Ali","givenName":"Akbar"},"url":"https:\/\/plus.google.com\/117137725249225792257","image":{"url":"https:\/\/lh6.googleusercontent.com\/-7qHRJbecjtk\/AAAAAAAAAAI\/AAAAAAAAAEc\/ywaoD1Y_Lus\/photo.jpg?sz=50","isDefault":false},"isPlusUser":true,"language":"en_GB","circledByCount":13,"verified":false},"avatar_original":"https:\/\/lh6.googleusercontent.com\/-7qHRJbecjtk\/AAAAAAAAAAI\/AAAAAAAAAEc\/ywaoD1Y_Lus\/photo.jpg"}'    
        val=val.replace('\\"','').replace('""','"')
        value=json.loads(val,strict=False)
        print(calcScore(value))
    except:
        pass


# In[133]:


def calcScore(value):
    total_score=0
    try:
        firstName=value['name'].split()[0]
        lastname=value['name'].split()[-1]
        email=value['email']
        contains_first_name=re.compile(firstName.lower())
        contains_last_name=re.compile(lastName.lower())
        if(contains_first_name.search(email)):total_score+=2.5
        if(contains_last_name.search(email)):total_score+=2.5
    except:
        pass
    
    
    try:
        if(value['user']['verified']):total_score+=30
        else:pass
    except:
        pass
    
    
    try:
        if(value['user']['isPlusUser']):total_score+=10
        else:pass
      
    except:
        pass
    
    
    try:
        num_o_conn=value['user']['circledByCount']
        total_score+=int(num_o_conn)*1.5
        
        
    except:
        pass
    
    
    return(total_score)


# In[134]:


if __name__=='__main__':
    main()


# In[63]:


import numpy as np
val='{"token":"ya29.Gl3hBbA3WDTjQrj4AxFm3UHqYMfF2mgpRHJ5oh7myM1lYiRyhym5dvJwxL1T6sfNjcGDeELJ1OyEyt0M-9TQgki9dN73eSAEwnZJ2HFAd86AsE6OhaDH9oHeJTTAu_Q","refreshToken":null,"expiresIn":3599,"id":"117137725249225792257","nickname":null,"name":"Akbar Ali","email":"akbarali0702@gmail.com","avatar":"https:\/\/lh6.googleusercontent.com\/-7qHRJbecjtk\/AAAAAAAAAAI\/AAAAAAAAAEc\/ywaoD1Y_Lus\/photo.jpg?sz=50","user":{"kind":"plus#person","etag":"\"RKS4-q7QGL10FxltAebpjqjKQR0\/0XNvPDppxL7u4w-RzRYioOpuLkY\"","gender":"male","emails":[{"value":"akbarali0702@gmail.com","type":"account"}],"objectType":"person","id":"117137725249225792257","displayName":"Akbar Ali","name":{"familyName":"Ali","givenName":"Akbar"},"url":"https:\/\/plus.google.com\/117137725249225792257","image":{"url":"https:\/\/lh6.googleusercontent.com\/-7qHRJbecjtk\/AAAAAAAAAAI\/AAAAAAAAAEc\/ywaoD1Y_Lus\/photo.jpg?sz=50","isDefault":false},"isPlusUser":true,"language":"en_GB","circledByCount":13,"verified":false},"avatar_original":"https:\/\/lh6.googleusercontent.com\/-7qHRJbecjtk\/AAAAAAAAAAI\/AAAAAAAAAEc\/ywaoD1Y_Lus\/photo.jpg"}'    
val=val.replace('\\"','').replace('""','"')
value=json.loads(val,strict=False)
teVal=value['user']['verified']


# In[67]:




