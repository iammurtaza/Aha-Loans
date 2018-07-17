
# coding: utf-8

# In[92]:


import re,json,sys



# In[129]:




def main():
    try:
        val='{"token":"ya29.GlvhBWHY6agRXvwCisbrYd7VJFJOIgFQ4iV8QJdL6eRq121ka4iXunFHE9AbCUDpdYztO4oqgdUUxc4zCQ5WodW8cVinTEsclao7RZ-KD-WPwhUEGF9MPrJkM9Wh","refreshToken":null,"expiresIn":3599,"id":"102390027928031912530","nickname":null,"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","avatar":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg?sz=50","user":{"kind":"plus#person","etag":"\"RKS4-q7QGL10FxltAebpjqjKQR0\/jH860EIRoiwI9_WsKudkq9Ao-YA\"","emails":[{"value":"sunnyyasser@gmail.com","type":"account"}],"objectType":"person","id":"102390027928031912530","displayName":"Sunny Yasser","name":{"familyName":"Yasser","givenName":"Sunny"},"url":"https:\/\/plus.google.com\/102390027928031912530","image":{"url":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg?sz=50","isDefault":false},"isPlusUser":true,"language":"en","circledByCount":0,"verified":false},"avatar_original":"https:\/\/lh4.googleusercontent.com\/-4ompB7TQ2gU\/AAAAAAAAAAI\/AAAAAAAAABQ\/3KHG61tRkec\/photo.jpg"}'
        val=val.replace('\\"','').replace('""','"')
        value=json.loads(val,strict=False)
        print(calcScore(value))
    except:
        pass

    
def calcScore(value):
    total_score=0
      
    
    try:
        if(value['user']['verified']):
            total_score+=30
        else:pass
    except:
        pass
    
    
    try:
        if(value['user']['isPlusUser']):
            total_score+=10
        else:pass
      
    except:
        pass
    
    
    try:
        num_o_conn=value['user']['circledByCount']
        if(num_o_conn>50):total_score+=50
        else:total_score+=int(num_o_conn)*1.5
        
        
    except:
        pass
    


    try:
        firstName=value['name'].split()[0].lower()
        lastName=value['name'].split()[-1].lower()
        email=value['email'].lower()
    except:
        pass
    else:
        containsFirst=re.compile(firstName)
        containsLast=re.compile(lastName)
        if(containsFirst.search(email)):total_score+=15
        if(containsLast.search(email)):total_score+=15    
   

    return(total_score)




if __name__=='__main__':
    main()





