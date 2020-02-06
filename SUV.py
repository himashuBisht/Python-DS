


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math
sv=pd.read_csv("Social_Network_Ads.csv")


# In[5]:


sv.head(1)


# In[20]:


X=sv.iloc[:,[2,3]].values
y=sv.iloc[:,4].values

#iloc is index of pandas dataframe used for integer based indexing(Selection by index)


# In[16]:


X[1:10]


# In[18]:


from sklearn.model_selection import train_test_split


# In[21]:


X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.33, random_state=42)


# In[22]:


from sklearn.preprocessing import StandardScaler


# In[26]:


sc=StandardScaler()  # to transform large data in small data to train
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)


# In[28]:


from sklearn.linear_model import LogisticRegression
classic=LogisticRegression(random_state=0)
classic.fit(X_train,y_train)


# In[32]:


y_pred=classic.predict(X_test)


# In[34]:


from sklearn.metrics import accuracy_score


# In[35]:


accuracy_score(y_test,y_pred)


# In[ ]:




