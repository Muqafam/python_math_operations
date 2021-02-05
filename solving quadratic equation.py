#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
import numpy as np
warnings.filterwarnings('ignore')
a=12
b=24
c=10

d = (-b-np.sqrt((b**2) - (4*a*c)))/(2*a)
e = (-b+np.sqrt((b**2) - (4*a*c)))/(2*a)
print(d)
print(e)


# In[ ]:




