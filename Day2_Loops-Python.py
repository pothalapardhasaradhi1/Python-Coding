#!/usr/bin/env python
# coding: utf-8

# In[1]:


# loops: are used to run block of code for a certain number of times
# we have two types
# 1.for loop
# 2.while loop
# While loop:it is used to execute the block ofof statement until the condition false
i=int(input("Enter the number"))
while i<10:
    print(i)
    i=i+1
    


# In[1]:


# Break statement is used to break the loop when the condition true
i=1
while i<10:
    print(i)
    if i==5:
        break
    i=i+1
        


# 

# In[4]:


a=int(input("Enter a number"))
while a<20:
    print(a)
    if a==18:
        break
    a=a+1


# In[5]:


# Continue statement is used to stop the current iteration and continue with the next
a=10
while a>20:
    if a==15:
        continue
    a=a+1
    print(a)


# In[6]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[8]:


# While with else block
# once the condition is false, it will be executed
i=1
while i<10:
    print(i)
    i=i+1
else:
    print("the value of i is greater than 9")


# In[9]:


# For loop
a=[1,2,3,4,5,6,7,8]
for i in a:
    print(i)


# In[10]:


for i in "pardhu":
    print(i)


# In[11]:


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in a:
    print(i)
    if i==10:
        break


# In[12]:


# Skip the value in for loop
a=['a','b','c','d','e']
for i in a:
    if i=='c':
        continue
    print(i)


# In[13]:


for i in range(10):
    print(i)


# In[14]:


for i in range(1,3):
    print(i)


# In[15]:


for i in range(1,20,2):
    print(i)


# In[16]:


# for with else block
for i in range(10):
    print(i)
else:
    print("Once the condition has done then else will be executed")


# In[18]:


# Pass statement is used to write empty loops
# used to getting avoid error
for i in range(10):
    pass
    


# In[ ]:




