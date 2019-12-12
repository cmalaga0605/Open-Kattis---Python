#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys #imported sys to exit program if I need to 
contestants,problems =[int(number)for number in input().split()] #took two inputs 
if contestants <1: #set constraint 1 
    sys.exit()
elif problems>1000: #set constraint 2
    sys.exit()
else:
    count = 1 #set the count at one 
    while contestants>=count:  #looped to repeat the same operation 
        input() #accepted an input 
        count+=1  #incremented each time 
    
    print(problems) #printed the count of problems solved i.e carrots needed


# In[ ]:




