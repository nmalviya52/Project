
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd


# In[2]:

g=glob.glob("/home/naresh/Downloads/Project/Virus.Win/*");


# In[3]:

list1=set()


# In[4]:

for files in g:
    try:
        pe=pefile.PE(files)
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            list1.add(entry.dll.decode('ASCII'))
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
            list2.add(entry.dll.decode('ASCII'))
    except:
        pass


# In[9]:

len(list2)


# In[10]:

mergelist=list1.unionion(list2)


# In[13]:

len(mergelist)


# In[11]:

DLLcalls=pd.DataFrame(list(list2))


# In[14]:

DLLcalls.info()


# In[15]:

DLLcalls.to_csv("DLLcalls_list.csv")


# In[ ]:



