#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sys #imported the sys library to exit the program when need be
n = int(input()) #took in the number of battles our hero played
if n > 100 or n <1: #assigned constraints
    sys.exit()
count = 0   
while n !=0: #used a while loop to loop through the battles
    k=str(input()) #took in the battle
    if 'C'not in k and 'D'not in k and 'O'not in k or len(k)>1000 or len(k)<1: #assigned constraints
        sys.exit()
    s = 'CD'
    for i in k: #used a for loop to go through the input
        if s not in k: # if CD not in k then we added 1 to the count
            count+=1
            break  #if we added 1 we went to the next input
    n-=1
print(count)
    


# In[ ]:




