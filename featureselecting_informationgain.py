
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif


# In[2]:

data=pd.read_csv("/home/naresh/Downloads/Project/Project/data_training.csv")


# In[3]:

data.head()


# In[15]:

X=data.values[:,2:]


# In[16]:

Y=data.values[:,1]


# In[17]:

Y = Y.ravel()
Y = np.array(Y).astype(int)


# In[18]:

X.shape


# In[19]:

Y.shape


# In[20]:

Y=Y.reshape(-1,1)


# In[21]:

Y.shape


# In[12]:

data.isnull().sum()


# In[13]:

data['OPTIONAL_HEADER.BaseOfData']=data['OPTIONAL_HEADER.BaseOfData'].fillna(data['OPTIONAL_HEADER.BaseOfData'].median())


# In[22]:

result=mutual_info_classif(X,Y,discrete_features=True)


# In[23]:

result


# In[24]:

len(result)


# In[25]:

feature=data.columns


# In[26]:

feature=feature[2:]


# In[27]:

len(feature)


# In[28]:

feature


# In[29]:

result_df = pd.DataFrame(
    {'Features':feature,
     'Informationgain':result
    })


# In[31]:

result_df.head()


# In[34]:

len(result_df[result_df['Informationgain']>0.05])


# In[35]:

reduced_feature=result_df[result_df['Informationgain']>0.05]


# In[36]:

result_df.to_csv("FeatureswithInformationGain.csv",index=False)


# In[37]:

reduced_feature.info()


# In[38]:

reduced_feature.head()


# In[39]:

featureslist=reduced_feature.values[:,0]


# In[40]:

featureslist


# In[41]:

featureslist_df=pd.DataFrame(featureslist)


# In[42]:

featureslist_df.head()


# In[43]:

featureslist_df.columns=['Features']


# In[45]:

featureslist_df.to_csv("ReducedFeatureslist.csv",index=False)


# In[49]:

features_list=featureslist.tolist()


# In[50]:

features_list


# In[51]:

features_list=['FileName']+['Malicious']+features_list


# In[52]:

features_list


# In[53]:

data_reduced_df=data[features_list]


# In[54]:

data_reduced_df.head()


# In[55]:

data_reduced_df.info()


# In[58]:

data_reduced_df.to_csv("reduced_data_selectedFeatures.csv",index=False)


# In[ ]:



