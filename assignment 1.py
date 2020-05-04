#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=list(range(2000,3201))
m=[]
for i in a:
    if i%7==0:
        if i%5!=0:
            m.append(i)
                


# In[3]:


print(m,end="")


# In[4]:


a=input("first name ")
b=input("second name ")
print(b,a)


# In[5]:


d=12
import math
p= math.pi
area=(d*p*d*d)/6
area


# In[6]:


a=list(map(int,input().split(',')))
print(a)


# In[7]:


for i in range(5):
    for j in range(i+1):
        print('*',end=" ")
    print()
for i in range(5):
    for j in range(4-i):
        print('*',end=" ")
    print()


# In[11]:


s=input("enter the str ")
l=len(s)
l
for i in range(l-1,-1,-1):
    print(s[i],end="")


# In[12]:


s="WE, THE PEOPLE OF INDIA,\n      having solemnly resolved to constitute India into a SOVEREIGN, !\n            SOCIALIST,SECULAR,DEMOCRATIC,REPUBLIC \n             and to secure to all its citizens"
print(s)


# In[ ]:




