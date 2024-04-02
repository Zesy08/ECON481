#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = np.array([1, 2, 5, -2, -4, 5])
cond = x > 0
x[~cond] = x[~cond] * -1
x


# In[ ]:




