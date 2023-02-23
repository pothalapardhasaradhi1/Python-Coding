#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Array is nothing a collection of elements which is having same data type
# denoted by square braces[]
# array elements are indexed
# positive index starts from 0
# negative index starts from  -1
a=[1,2,3,4,5,6,7,8,0,2,2]
print(len(a))
print(type(a))


# In[7]:


# Append: adding element into the last position
a=[1,2,34,4]
a.append(8)
print(a)
    


# In[9]:


# clear: remove all the elee,ents in a list or araray
a=[1,2,34,4]
a.clear()
print(a)


# In[10]:


a=[1,2,34,4]
del a


# In[11]:


print(a)


# In[14]:


a=[1,2,34,4]
a.extend([9,0])
a
# if we want add more than one element


# In[17]:


a=[1,1,1,3,4,6]
b=a.count(5)
print(b)


# In[21]:


a=[1,2,3,4,5,6,0]
print(a.index(5))


# In[25]:


# insert
a=[1,2,3]
a.insert(0,100)
print(a)


# In[26]:


# sort():to arrange in the form asending order
a=[1,2,399,0,78,7]
a.sort()
print(a)


# In[31]:


a=[1,2,399,0,78,7]
a.reverse()
print(a)


# In[32]:


a=[1,2,399,0,78,7]
a.remove(1)
a


# In[34]:


a=[1,2,399,0,78,7]
a.pop()
a


# In[35]:


a=[1,2,399,0,78,7]
a.pop(1)
a


# In[36]:


a=[1,2,399,0,78,7]
b=a.copy()
print(b)


# In[37]:


a=[1,2,399,0,78,7]
b=a
print(b)


# In[38]:


# Lambda function is as small ananmous function
# a function without name we can call it as ananoumous
# lambda is keyword to define lambda function
# syntax lambda arguments: expression
x=lambda a:a+10
print(x(5))


# In[40]:


x= lambda a,b:a//b
print(x(20,5))


# In[41]:


# Class is a blue print for creating an object
# the physical existance of a cllass we can call it as object
# The class is a keyword to define a class
class myClass:
    a=10;
    pass


# In[42]:


p1=myClass()


# In[43]:


p1.a


# In[51]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=Person("pardhu",23)
print(obj.name)
# self is a default first argument for all instant methods


# In[ ]:




