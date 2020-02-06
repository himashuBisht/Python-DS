#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math
tt=pd.read_csv("train.csv")


# In[6]:


tt.head(10)


# print("Passengers--"+str(len(tt)))

# ## Analysing

# In[11]:


sns.countplot(x="Survived",data=tt)


# In[12]:


sns.countplot(x="Survived", hue="Sex",data=tt)


# In[14]:


tt["Age"].plot.hist()


# In[20]:


sns.countplot(x="SibSp", data=tt)


# ## Data Wrangling
# 

# In[22]:


tt.isnull()


# In[23]:


tt.isnull().sum()


# In[24]:


sns.heatmap(tt.isnull(),yticklabels=False)


# In[25]:


sns.heatmap(tt.isnull(),yticklabels=False,cmap="viridis")


# In[26]:


sns.boxplot(x="Pclass",y="Age", data= tt)


# In[28]:


tt.drop("Cabin", axis=1,inplace=True)


# In[29]:


tt.head(1)


# In[31]:


tt.dropna(inplace=True)


# In[36]:


sns.heatmap(tt.isnull(), yticklabels=False,cbar=False)


# In[39]:


tt.isnull().sum()


# In[43]:


pd.get_dummies(tt["Sex"])


# In[51]:


sex=pd.get_dummies(tt["Sex"],drop_first=True)


# In[46]:


embark=pd.get_dummies(tt["Embarked"])
embark.head()


# In[47]:


embark=pd.get_dummies(tt["Embarked"],drop_first=True)
embark.head()


# In[49]:


pcl=pd.get_dummies(tt["Pclass"],drop_first=True)
pcl.head(3)


# In[53]:


tt=pd.concat([tt,sex,embark,pcl],axis=1)
tt.head(1)


# In[55]:


tt.drop(['Name','Sex','Ticket','Embarked','PassengerId'],axis=1,inplace=True)


# In[56]:


tt.head(1)


# In[57]:


tt.drop('Pclass',axis=1,inplace=True)


# In[58]:


tt.head(0)


# ## Train Data Sets

# In[64]:


X=tt.drop("Survived",axis=1)
Y=tt["Survived"]


# In[62]:


from sklearn.model_selection import train_test_split


# In[66]:


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)


# In[67]:


from sklearn.linear_model import LogisticRegression


# In[69]:


logmodel=LogisticRegression()


# In[70]:


logmodel.fit(X_train, y_train)


# In[71]:


predictions=logmodel.predict(X_test)


# In[73]:


from sklearn.metrics import classification_report


# In[75]:


classification_report(y_test,predictions)


# In[76]:


from sklearn.metrics import confusion_matrix


# In[77]:


confusion_matrix(y_test,predictions)


# In[79]:


from sklearn.metrics import accuracy_score


# In[80]:


accuracy_score(y_test, predictions)


# In[ ]:




