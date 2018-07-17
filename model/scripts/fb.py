
# coding: utf-8

# In[23]:


import re,os,json


# In[24]:


val='{"token":"ya29.GlvhBWHY6agRXvwCisbrYd7VJFJOIgFQ4iV8QJdL6eRq121ka4iXunFHE9AbCUDpdYztO4oqgdUUxc4zCQ5WodW8cVinTEsclao7RZ-KD-WPwhUEGF9MPrJkM9Wh","refreshToken":null,"expiresIn":3599,"id":"102390027928031912530","nickname":null,"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","avatar":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg?sz=50","user":{"kind":"plus#person","etag":"\"RKS4-q7QGL10FxltAebpjqjKQR0\/jH860EIRoiwI9_WsKudkq9Ao-YA\"","emails":[{"value":"sunnyyasser@gmail.com","type":"account"}],"objectType":"person","id":"102390027928031912530","displayName":"Sunny Yasser","name":{"familyName":"Yasser","givenName":"Sunny"},"url":"https:\/\/plus.google.com\/102390027928031912530","image":{"url":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg?sz=50","isDefault":false},"isPlusUser":true,"language":"en","circledByCount":0,"verified":false},"avatar_original":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg"}'


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

