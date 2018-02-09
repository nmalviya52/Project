
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd


# In[2]:

data_dll=pd.read_csv("/home/naresh/Downloads/Project/Project/DLL_files_all_data.csv")


# In[3]:

data_function=pd.read_csv("/home/naresh/Downloads/Project/Project/functioncalls_alldata.csv")


# In[4]:

data_peheader=pd.read_csv("/home/naresh/Downloads/Project/Project/pe_header_allfiles.csv")


# In[5]:

data_dll.head()


# In[6]:

data_function.head()


# In[7]:

data_peheader.head()


# In[8]:

data_dll=data_dll.drop('Unnamed: 0',axis=1)


# In[9]:

data_function=data_function.drop('Unnamed: 0',axis=1)


# In[10]:

data_peheader=data_peheader.drop('Unnamed: 0',axis=1)


# In[11]:

new_df=pd.merge(data_dll,data_peheader,on='FileName')


# In[12]:

new_df.head()


# In[13]:

new_df.info()


# In[14]:

new_df=new_df.drop('Malicious_y',axis=1)


# In[15]:

new_df=new_df.rename(columns={'Malicious_x':'Malicious'})


# In[16]:

new_df.head()


# In[17]:

new_df2=pd.merge(new_df,data_function,on='FileName')


# In[18]:

new_df2.head()


# In[19]:

new_df2=new_df2.drop('Malicious_y',axis=1)


# In[20]:

new_df2=new_df2.rename(columns={'Malicious_x':'Malicious'})


# In[21]:

new_df2.head()


# In[22]:

new_df2.to_csv("all_data_final.csv")


# In[ ]:



