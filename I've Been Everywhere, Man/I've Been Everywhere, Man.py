#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys #imported the sys library to exit the program when need be
testcases= int(input()) #declared a variable to recieve the testcases
if testcases >50:  #declared a constrant 
    sys.exit()
else:
    while testcases != 0:  #used a while loop to loop through to go through testcases
        hypo_trips =int(input()) #declared a variable to recieve number of trips (hypothetical)
        if (hypo_trips > 100): #declared a constrant
            sys.exit()
        else:
            triplist = [] #declared a list for the trips
            while hypo_trips != 0: #used a while loop to go through the trips
                triplist.append(str(input())) #appended each trip to the list
                hypo_trips-=1 #subtracted 1 everytime went through the loop so that the loop wouldnt go on forever
            x = set(triplist) #declared variable so that i can use the set function to get distinct strings in the list
            count=0
            for i in x: #used a for loop to go through the list and get a count
                count+=1
            testcases-=1
            print(count) 


# In[ ]:





# In[ ]:




