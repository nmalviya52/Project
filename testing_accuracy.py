
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


# In[2]:

train_df = pd.read_csv("/home/naresh/Downloads/Project/Project/reduced_data_selectedFeatures.csv")


# In[3]:

test_df=pd.read_csv("/home/naresh/Downloads/Project/Project/data_testing.csv")


# In[4]:

featureset=pd.read_csv("/home/naresh/Downloads/Project/Project/ReducedFeatureslist.csv")


# In[5]:

test_df.head()


# In[6]:

train_df.head()


# In[7]:

X=train_df.values[:,2:]


# In[8]:

Y=train_df.values[:,1]


# In[10]:

Y = Y.ravel()
Y = np.array(Y).astype(int)


# In[11]:

clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = None, max_depth=9)
clf_gini.fit(X, Y)


# In[12]:

test_df['OPTIONAL_HEADER.BaseOfData']=test_df['OPTIONAL_HEADER.BaseOfData'].fillna(train_df['OPTIONAL_HEADER.BaseOfData'].median())


# In[13]:

featureset


# In[14]:

featurelist=featureset.values[:,0]


# In[17]:

featurelist=featurelist.tolist()


# In[18]:

featurelist=['FileName']+['Malicious']+featurelist


# In[21]:

test_df=test_df[featurelist]


# In[22]:

test_df.head()


# In[23]:

X_test = test_df.values[:, 2:]


# In[24]:

y_pred_test = clf_gini.predict(X_test)


# In[25]:

print("Accuracy is ", accuracy_score(test_df['Malicious'],y_pred_test)*100)


# In[ ]:



