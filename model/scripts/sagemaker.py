
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt


# In[8]:


print(2)


# In[9]:


df = pd.read_csv('custs.csv',low_memory=False)


# In[10]:


df.describe()


# In[11]:


df.drop('phone1',axis=1,inplace=True)


# In[12]:


df.head(10)


# In[13]:


df.describe()


# In[14]:


df.drop('email',axis=1,inplace=True)


# In[15]:


df.head(10)


# In[16]:


df.drop(['piplDataSource','phone2','DOB','first_name','last_name','address','city','fullContactSource'],axis=1,inplace=True)


# In[17]:


df.head(10)


# In[18]:


sum(pd.isnull(df['Occupation']))


# In[19]:


df.drop(['country','Occupation'],axis=1,inplace=True)


# In[20]:


df.head(10)


# In[21]:


df.describe()


# In[22]:


df.drop('pincode',axis=1,inplace=True)


# In[23]:


df.isnull().values.sum()


# In[24]:


df.count()


# In[25]:


df.isnull().count(axis=0)


# In[26]:


df.isnull().sum(axis=0)


# In[27]:


df.isnull().sum(axis=1)


# In[28]:


df.shape


# In[29]:


df = df[pd.notnull(df['creditScore'])]


# In[30]:


df.isnull().sum(axis=0)


# In[31]:


df.count(axis=0)


# In[32]:


df.describe()


# In[33]:


sum(pd.isnull(df['creditScore']))


# In[34]:


print(sum(pd.isnull(df.type)))


# In[35]:


df.head()


# In[36]:


df.shape


# In[37]:


df.ndim


# In[38]:


df.to_csv('editedCSV.csv', sep='\t', encoding='utf-8')


# In[39]:


df.drop('id',axis=1,inplace=True)


# In[40]:


df.head(10)


# In[41]:


df.tail(10)


# In[42]:


pd.distinct(df['type'])


# In[43]:


df.type.unique()


# In[44]:


sum(pd.isnull(df['type']))


# In[45]:


import numpy as np


# In[46]:


import matplotlib.pyplot as plt


# In[47]:


df.isnull().sum(axis=0)


# In[48]:


(df.type == 'Owns,Primary').sum()


# In[49]:


df.head()


# In[50]:


values=['Primary', 'Rents,Primary', 'Owns,Primary','Permanent',
       'Office', 'Owns,Permanent', 'Owns', 'Owns,Office',
       'Rents,Permanent', 'Rents,Office', 'Rents']
for item in values:
    print((df['type']==item).sum())


# In[51]:


df.isnull().sum(axis=0)


# In[52]:


df.drop(['RecentAccount','RecentAccountType','RecentAccountDate','OldestAccount','OldestAccountType','OldestAccountDate'],axis=1,inplace=True)


# In[53]:


df.isnull().sum(axis=0)


# In[54]:


df.head(5)


# In[55]:


df.describe()


# In[56]:


df.shape


# In[57]:


df.to_csv('editedCSV_v2.csv', sep='\t', encoding='utf-8')


# In[58]:


type_mapping={'Primary':0,
              'Rents,Primary':1,
              'Owns,Primary':2,
              'Permanent':3,
              'Office':4,
              'Owns,Permanent':5,
              'Owns':6,
              'Owns,Office':7,
              'Rents,Permanent':8, 
              'Rents,Office':9,
              'Rents':10}


# In[59]:


def typemap(x):
    if(x is not np.nan):
        df['typeMap']=type_mapping(x)
    


# In[60]:


df['type_map'] = df.type.map({'Primary':0,
              'Rents,Primary':1,
              'Owns,Primary':2,
              'Permanent':3,
              'Office':4,
              'Owns,Permanent':5,
              'Owns':6,
              'Owns,Office':7,
              'Rents,Permanent':8, 
              'Rents,Office':9,
              'Rents':10})


# In[61]:


df.drop('type',axis=1,inplace=True)


# In[62]:


df.head(10)


# In[63]:


df.shape


# In[64]:


df.describe()


# In[65]:


df.isnull().sum(axis=0)


# In[66]:


df.to_csv('editedCSV_v3.csv', sep='\t', encoding='utf-8')


# In[67]:


numeric = pd.read_csv('dataNumeric.csv')


# In[68]:


numeric.head(10)


# In[69]:


numeric.describe()


# In[70]:


numeric.isnull().sum(axis=0)


# In[71]:


numeric.shape


# In[72]:


numeric['TotalCreditLimit'].count().sum(axis=0)


# In[73]:


import matplotlib.pyplot as plt


# In[74]:


import seaborn as sns


# In[76]:


import sklearn


# In[78]:


import tensorflow as tf


# In[79]:


print(numeric)


# In[113]:


x=numeric.iloc[:,4].values
x.shape


# In[114]:


y=numeric.iloc[:,0].values
y.shape


# In[115]:


get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlabel('No. of Accounts')
ax.set_ylabel('Credit Score')
ax.set_xlim([x.min(axis=0),50])
ax.set_ylim([250,y.max(axis=0)])
ax.scatter(x,y,s=1)
plt.show()


# In[83]:


numeric['NoOfAccounts'].max()


# In[86]:


numeric[['creditScore','Age','Gender']][numeric.NoOfAccounts==numeric.NoOfAccounts.max()]


# In[87]:


numeric.NoOfAccounts.max()


# In[88]:


numeric[numeric.NoOfAccounts==numeric.NoOfAccounts.max()]


# In[96]:


x=numeric.iloc[8495]  


# In[97]:


x


# In[100]:


numeric.drop(numeric.index[[8495]])


# In[116]:


x=numeric.iloc[8495]


# In[117]:


x

numeric.drop(numeric.index[8495],iplace=True)
# In[118]:


numeric.drop(numeric.index[8495],inplace=True)


# In[119]:


numeric.shape


# In[122]:


q = numeric["Age"].quantile(0.99)


# In[123]:


q


# In[126]:


df=numeric.copy(deep=True)


# In[131]:


q=numeric.all().quantile(0.99)


# In[132]:


q


# In[129]:


q=numeric.all


# In[130]:


q.drop()


# In[136]:


q=np.mean(df.Age)


# In[137]:


q


# In[138]:


std=np.std(df.Age)


# In[139]:


std


# In[149]:


df[np.logical_and(df.Age<55, df.Age>19)]


# In[150]:


std=np.std(df)


# In[151]:


std


# In[152]:


from scipy.stats import mstats
winsor=mstats.winsorize(df,limits=[df.quantile(0.05),df.quantile(0.95)])

