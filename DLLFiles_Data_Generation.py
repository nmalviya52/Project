
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd


# In[2]:

function= pd.read_csv("/home/naresh/Downloads/Project/Project/DLLcalls_list.csv")


# In[3]:

function.head()


# In[4]:

function=function.drop(['Unnamed: 0'],axis=1)


# In[5]:

function.columns=["DLL"]


# In[6]:

function.head()


# In[7]:

datalist=function['DLL'].tolist()


# In[8]:

datalist=['FileName']+['Malicious']+datalist


# In[9]:

function=pd.DataFrame(0,index=[0],columns=datalist)


# In[10]:

function.head()


# In[11]:

function=function.drop(function.index[[0]])


# In[12]:

function.head()


# In[14]:

function['FileName']=function.FileName.astype(object)


# In[13]:

g=glob.glob("/home/naresh/Downloads/Project/Virus.Win/*");


# In[15]:

for files in g:
    try:
        pe=pefile.PE(files)
        toadd=pd.DataFrame(0,index=[0],columns=datalist)
        toadd['FileName']=toadd.FileName.astype(object)
        toadd.set_value(0,'FileName',files)
        toadd.set_value(0,'Malicious',1)
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            if entry.dll.decode('ASCII') in toadd.columns:
                toadd.set_value(0,entry.dll.decode('ASCII'),1)    
        function=function.append(toadd)
    except:
        pass


# In[16]:

function.head()


# In[17]:

function.info()


# In[18]:

g=glob.glob("/home/naresh/Downloads/Project/Benign/*");


# In[19]:

for files in g:
    try:
        pe=pefile.PE(files)
        toadd=pd.DataFrame(0,index=[0],columns=datalist)
        toadd['FileName']=toadd.FileName.astype(object)
        toadd.set_value(0,'FileName',files)
        toadd.set_value(0,'Malicious',0)
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            if entry.dll.decode('ASCII') in toadd.columns:
                toadd.set_value(0,entry.dll.decode('ASCII'),1)    
        function=function.append(toadd)
    except:
        pass


# In[20]:

function.info()


# In[21]:

function.head()


# In[22]:

function['Malicious'].value_counts()


# In[23]:

function.to_csv("DLL_files_all_data.csv")


# In[ ]:



