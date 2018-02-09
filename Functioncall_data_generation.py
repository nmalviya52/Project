
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd


# In[3]:

function= pd.read_csv("/home/naresh/Downloads/Project/Project/functioncall_list.csv")


# In[4]:

function.head()


# In[5]:

function=function.drop(['Unnamed: 0'],axis=1)


# In[6]:

function.info()


# In[7]:

function.columns=["functions"]


# In[8]:

datalist=function['functions'].tolist()


# In[9]:

len(datalist)


# In[10]:

datalist=['FileName']+['Malicious']+datalist


# In[11]:

len(datalist)


# In[12]:

function=pd.DataFrame(0,index=[0],columns=datalist)


# In[15]:

function['FileName']=function.FileName.astype(object)


# In[16]:

function.head()


# In[17]:

function=function.drop(function.index[[0]])


# In[18]:

g=glob.glob("/home/naresh/Downloads/Project/Virus.Win/*");


# In[19]:

for files in g:
    try:
        pe=pefile.PE(files)
        toadd=pd.DataFrame(0,index=[0],columns=datalist)
        toadd['FileName']=toadd.FileName.astype(object)
        toadd.set_value(0,'FileName',files)
        toadd.set_value(0,'Malicious',1)
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            for imp in entry.imports:
                if imp.name.decode('ASCII') in toadd.columns:
                    toadd.set_value(0,imp.name.decode('ASCII'),1)    
        function=function.append(toadd)
    except:
        pass


# In[20]:

function.info()


# In[21]:

function.head()


# In[22]:

g=glob.glob("/home/naresh/Downloads/Project/Benign/*");


# In[23]:

for files in g:
    try:
        pe=pefile.PE(files)
        toadd=pd.DataFrame(0,index=[0],columns=datalist)
        toadd['FileName']=toadd.FileName.astype(object)
        toadd.set_value(0,'FileName',files)
        toadd.set_value(0,'Malicious',0)
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            for imp in entry.imports:
                if imp.name.decode('ASCII') in toadd.columns:
                    toadd.set_value(0,imp.name.decode('ASCII'),1)    
        function=function.append(toadd)
    except:
        pass


# In[24]:

function.info()


# In[25]:

function.to_csv("functioncalls_alldata.csv")


# In[ ]:



