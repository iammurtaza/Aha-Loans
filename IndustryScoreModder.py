
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[4]:


df=pd.read_csv('industrycount.csv')


# In[5]:


df.head()


# In[10]:


df.isnull().count(axis=1)


# In[13]:


df.count(axis=1)


# In[14]:


df.isnull().count(axis=1)


# In[15]:


df.isnull().any()


# In[18]:


null_col=df.columns[df.isnull().any()]


# In[19]:


null_col


# In[21]:


df.columns[null_col]


# In[22]:


df.columns


# In[25]:


df.Score


# In[26]:


df.Score.fillna(40,inplace=True)


# In[27]:


df.Score


# In[28]:


df.head(100)


# In[33]:


df.iloc[[2,4,3]]


# In[64]:



df.loc[[75,93]]['Score'].replace(40,50,inplace=True)


# In[61]:


df.loc[75]


# In[39]:


df.head(100)


# In[49]:


df.loc[:,'Score']


# In[51]:


df.loc['Venture Capital & Private Equity']


# In[52]:


pd.options.mode.chained_assignment = None  # default='warn'


# In[68]:


df.loc[df['Score']==70]['Industry']


# In[69]:


df.to_csv('industryscore.csv',sep='\t')


# In[71]:


df.loc[df['Industry'].str.lower().str.replace('s/+',"")=='retail']


# In[74]:


df.loc[df['Industry'].str.lower()=="human resources"]

