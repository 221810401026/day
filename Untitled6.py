#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1) [1,4,5,6,9] - 14569
def convert(s):
    x=0
    for i in range(len(s)):
        x=x*10+s[i]
    return x
s=[1,4,5,6,9]
convert(s)

