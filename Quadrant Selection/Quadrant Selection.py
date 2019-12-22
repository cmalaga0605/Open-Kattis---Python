#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys #imported the sys library to exit the program when need be
x = int(input()) #declared variable to take in x coordinate
if x <-1000 or x >1000 or x ==0:
    sys.exit()
y = int(input()) #declared variable to take in y coordinate
if y<-1000 or y>1000 or y ==0: 
    sys.edit()
if x >=0 and y >=0: #quadrant 1
    print("1")
elif x<0 and y>=0:#quadrant 2
    print("2")
elif x>=0 and y<0:#quadrant 4
    print("4")
else: #quadrant 3
    print("3")


# In[ ]:




