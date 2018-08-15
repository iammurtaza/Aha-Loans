
# coding: utf-8

# In[23]:


import re,os,json


# In[24]:


val='{"token":"EAAWI8wxzZBC4BAGGJ0WsGgeZB1NZB7qpxTHN22RH4u7fgkDizYsCVuM4vzRwTqy0P4dRpA8h7IUunifZAKQZAMPNfdAzTFGXZCghZAbODOtkpLJNEYhH8VmSRW4WPIkma0nfhDDlsZBusCWDvFVI4fR5x8QWn0fNRfnbzm33p6ozFAZDZD","refreshToken":null,"expiresIn":5183998,"id":"1628721273866352","nickname":null,"name":"Akbar Ali","email":"akbarrizvi2000@yahoo.co.in","avatar":"https:\/\/graph.facebook.com\/v2.10\/1628721273866352\/picture?type=normal","user":{"name":"Akbar Ali","email":"akbarrizvi2000@yahoo.co.in","gender":"male","verified":true,"link":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEU0MEVpZAjNnclVROExCcUpJNUk4V2JIOFRXSlBRTXUtbVljUnZAxUFpHNG5kX3VUOC1ReTVIT3BhTi10Y045VWJCemtlMjNWMFlfUnFQQzdMb3FyMWdKdWRNVFZAPM2tUaU5qMmZAVMEFISktlOEFfOHcZD\/","id":"1628721273866352"},"avatar_original":"https:\/\/graph.facebook.com\/v2.10\/1628721273866352\/picture?width=1920","profileUrl":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEU0MEVpZAjNnclVROExCcUpJNUk4V2JIOFRXSlBRTXUtbVljUnZAxUFpHNG5kX3VUOC1ReTVIT3BhTi10Y045VWJCemtlMjNWMFlfUnFQQzdMb3FyMWdKdWRNVFZAPM2tUaU5qMmZAVMEFISktlOEFfOHcZD\/"}'


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
print(totalScore)



# In[50]:





# In[51]:

#total score=80

