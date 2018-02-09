
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd


# In[2]:

data=pd.read_csv("/home/naresh/Downloads/Project/Project/all_data_final.csv")


# In[3]:

data.info()


# In[4]:

data.head()


# In[5]:

data=data.drop("Unnamed: 0",axis=1)


# In[6]:

df = pd.DataFrame(np.random.randn(4489, 2))
msk = np.random.rand(len(df)) < 0.7


# In[7]:

train = data[msk]
test = data[~msk]


# In[8]:

train_df=pd.DataFrame(train)


# In[9]:

test_df=pd.DataFrame(test)


# In[10]:

train_df['Malicious'].value_counts()


# In[11]:

test_df['Malicious'].value_counts()


# In[12]:

train_df.to_csv("data_training.csv",index=False)


# In[13]:

test_df.to_csv("data_testing.csv",index=False)


# In[ ]:



