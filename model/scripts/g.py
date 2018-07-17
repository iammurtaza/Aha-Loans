
# coding: utf-8

# In[1]:


import re,json,sys


# In[2]:


val='{"token":"ya29.GlvhBe0WPTWwBqG9t3SjuBXn6Z0Z0tBPqmnujA9MNa30RuoDKWUTDHF5mYNgga9V9Fuz3XRNSXGOHc806oQXBtFrCwxPrxo1F1Wy6guGanyxHMk-x8xLov7Tbf3_","refreshToken":null,"expiresIn":3600,"id":"112338217579525064145","nickname":null,"name":"Suneel Kumar","email":"suneel@ahaloans.com","avatar":"https:\/\/lh4.googleusercontent.com\/-BdxeRSG9gw0\/AAAAAAAAAAI\/AAAAAAAAAAA\/AB6qoq2ErBdZujv3moct09in7N7Q-F7-ow\/mo\/photo.jpg?sz=50","user":{"kind":"plus#person","etag":"\"RKS4-q7QGL10FxltAebpjqjKQR0\/KScNOyALFa_8fzjv8HI2ALe_5ag\"","emails":[{"value":"suneel@ahaloans.com","type":"account"}],"objectType":"person","id":"112338217579525064145","displayName":"Suneel Kumar","name":{"familyName":"Kumar","givenName":"Suneel"},"image":{"url":"https:\/\/lh4.googleusercontent.com\/-BdxeRSG9gw0\/AAAAAAAAAAI\/AAAAAAAAAAA\/AB6qoq2ErBdZujv3moct09in7N7Q-F7-ow\/mo\/photo.jpg?sz=50","isDefault":true},"isPlusUser":false,"language":"en","verified":false,"domain":"ahaloans.com"},"avatar_original":"https:\/\/lh4.googleusercontent.com\/-BdxeRSG9gw0\/AAAAAAAAAAI\/AAAAAAAAAAA\/AB6qoq2ErBdZujv3moct09in7N7Q-F7-ow\/mo\/photo.jpg"}'


# In[3]:


value=val.replace('\\"','').replace('""','"').replace("\'","")


# In[4]:


json.loads(value,strict=False)


# In[5]:


def main():
    try:
        
        val='{"token":"ya29.GlvhBWHY6agRXvwCisbrYd7VJFJOIgFQ4iV8QJdL6eRq121ka4iXunFHE9AbCUDpdYztO4oqgdUUxc4zCQ5WodW8cVinTEsclao7RZ-KD-WPwhUEGF9MPrJkM9Wh","refreshToken":null,"expiresIn":3599,"id":"102390027928031912530","nickname":null,"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","avatar":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg?sz=50","user":{"kind":"plus#person","etag":"\"RKS4-q7QGL10FxltAebpjqjKQR0\/jH860EIRoiwI9_WsKudkq9Ao-YA\"","emails":[{"value":"sunnyyasser@gmail.com","type":"account"}],"objectType":"person","id":"102390027928031912530","displayName":"Sunny Yasser","name":{"familyName":"Yasser","givenName":"Sunny"},"url":"https:\/\/plus.google.com\/102390027928031912530","image":{"url":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg?sz=50","isDefault":false},"isPlusUser":true,"language":"en","circledByCount":0,"verified":false},"avatar_original":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg"}'
        val=val.replace('\\"','').replace('""','"')
        value=json.loads(val,strict=False)
        print(calcScore(value))
    except:
        pass


# In[6]:


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
        if(value['user']['verified']):total_score+=40
        else:pass
    except:
        pass
    
    
    try:
        if(value['user']['isPlusUser']):total_score+=15
        else:pass
      
    except:
        pass
    
    
    try:
        num_o_conn=value['user']['circledByCount']
        total_score+=int(num_o_conn)*1.5
        
        
    except:
        pass
    
    
    return(total_score)


# In[7]:


if __name__=='__main__':
    main()


# In[11]:


