
# coding: utf-8

# In[23]:


import re,os,json


# In[24]:


val='{"token":"EAAWI8wxzZBC4BAOpC9mKuJm4SxPkKEYqRpJ249WUeEkJUD9Whhtiq8c8EvAxzwEL6vyRT39X5VpsPuPRjexSzmZCb7dRGWtACxE7Curq6u5ZCd8Fp3v6uQkfjDzhp8dE9bblGsPMUJ6cBDKvZB5er6LYLn9en5IlBhrxZCYTW2AZDZD","refreshToken":null,"expiresIn":5178523,"id":"1730828933650713","nickname":null,"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","avatar":"https:\/\/graph.facebook.com\/v2.10\/1730828933650713\/picture?type=normal","user":{"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","gender":"male","verified":true,"link":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEdhek1nY0syLVlJZA0FVRjB0T0pwUHZAKRmVtR29yWTlhSUtLRWpJZAWpWTlFBOTVvMWYzTUU0amE0T3RCUlpzQlVfNjRZAY3MzTm5yT1RPcUh1TldjVzJWaXdqOHZASZAHkxWl9Hc0tsU3BHOFNxWHZAvRncZD\/","id":"1730828933650713"},"avatar_original":"https:\/\/graph.facebook.com\/v2.10\/1730828933650713\/picture?width=1920","profileUrl":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEdhek1nY0syLVlJZA0FVRjB0T0pwUHZAKRmVtR29yWTlhSUtLRWpJZAWpWTlFBOTVvMWYzTUU0amE0T3RCUlpzQlVfNjRZAY3MzTm5yT1RPcUh1TldjVzJWaXdqOHZASZAHkxWl9Hc0tsU3BHOFNxWHZAvRncZD\/"}'


# In[25]:


value=json.loads(val,strict=False)


# In[26]:


totalScore=0


# In[27]:


try:
    value=json.loads(val,strict=False)
    email=value['email']
    try:
        firstName=value['name'].split(" ")[0]
        containsfirst=re.compile(firstName.lower())
        if(containsfirst.search(email)):totalScore+=25
    except:
        pass
    try:
        lastName=value['name'].split(" ")[-1]
        containslast=re.compile(lastName.lower())
        if(containslast.search(email)):totalScore+=25
    except:
        pass
except:
    pass
        


# In[52]:


try:
    verify=value['user']['verified']
    if(verify):totalScore+=30
    else:pass
except:
    pass


# In[53]:




# In[50]:





# In[51]:

#total score=80

