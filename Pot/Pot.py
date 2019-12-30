#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys #imported the sys library to exit the program when need be
n = int(input())
if n < 1 or n >10:  #included my constraints
    sys.exit()
addlist = [] #created a list 
while n != 0:
    p = int(input())
    if p < 10 or p > 9999:  #included my constraints
        sys.exit()
    s = p%10 #took the modulo of p that will give me the last digit of the int and assigned a variable
    p=str(p) #made the int input into a string in order to take the last digit off
    p=p[:-1] #Took of the last digit from the string 
    p=int(p) #Made the string into an integer again
    p=p**s #Squared the int p 
    addlist.append(p) # Appended it to a list 
    n -= 1
r = sum(addlist) #Added all of the content on the list
print(r)


# In[ ]:




