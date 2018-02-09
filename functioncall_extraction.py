
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd


# In[2]:

malicious=glob.glob("/home/naresh/Downloads/Project/Virus.Win/*");


# In[3]:

list1=set()


# In[4]:

for files in malicious:
    try:
        pe=pefile.PE(files)
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            for imp in entry.imports:
                list1.add(imp.name.decode('ASCII'))
    except:
        pass


# In[5]:

len(list1)


# In[6]:

benign=glob.glob("/home/naresh/Downloads/Project/Benign/*");


# In[7]:

list2=set()


# In[8]:

for files in benign:
    try:
        pe=pefile.PE(files)
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            for imp in entry.imports:
                list2.add(imp.name.decode('ASCII'))
    except:
        pass


# In[9]:

len(list2)


# In[10]:

len(list1.intersection(list2))


# In[11]:

combine=list1.union(list2)


# In[12]:

len(combine)


# In[13]:

functioncalls=pd.DataFrame(list(combine))


# In[14]:

functioncalls.head()


# In[15]:

functioncalls.info()


# In[16]:

functioncalls.to_csv("functioncall_list.csv")


# In[ ]:



