#!/usr/bin/env python
# coding: utf-8
# In[3]:
import pandas as pd
import numpy as np
# In[9]:
z = pd.DataFrame({'x':[1,2,3,4,5], 'y':[6,8,np.nan,9,10],'a':["a","b","c",np.nan,"e"],'b':["f",'g','h','j','k']})
# In[10]:
z
# In[11]:
z1 = z.fillna("vide")
# In[12]:
z1
# In[13]:
z2 = z['a'].fillna(0)
# In[14]:
z2
# In[19]:
z
# In[20]:
z['a']=z['a'].fillna(0)
# In[21]:
z
# In[ ]:
