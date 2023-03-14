#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to find size of tuple
a=(1,2,3,4)
print(a)
print(type(a))


# In[5]:


a=(1,2,3)
print(a.__sizeof__(),"Bytes")
# To find total number of bytes in a tuple


# In[8]:


# Python – Maximum and Minimum K elements in Tuple
a=(1,2,3,4,5,6,7,8,9,10)
k=2
b=list(a)
b.sort()
c=[b[0],b[1]]
d=[b[-2],b[-1]]
e=c+d
a=tuple(e)
print(a)


# In[32]:


# Python program to create a list of tuples from given list having number and its cube in each tuple
a=[1,2,3]
for i in a:
    j=i**3
    b=[]
    b.extend((i,j))
    c=tuple(b)
    d=[]
    d.append(c)
    print(d)


# In[37]:


a=[1,2,3,4]
b=[(i**3,i)for i in a]
print(b)


# In[39]:


a=[1,2,3,4,5,6]
b=[(i,i*i*i)for i in a]
print(b)
# list comprehension


# In[41]:


# Python – Adding Tuple to List and vice – versa
a=[1,2,3]
b=(4,5)
c=a+list(b)
print(c)


# In[44]:


a=(1,2)
b=[9,98]
print(a+tuple(b))


# In[52]:


# Python Program for cube sum of first n natural numbers
def fun(a):
    sum=0
    for i in range(1,a+1):
        sum=sum+i*i*i
    print(sum)
fun(10)


# In[53]:


# Python Program for square  sum of first n natural numbers
def fun1(a):
    sum=0
    for i in range(1,a+1):
        sum=sum+i*i
    print(sum)
fun1(3)  


# In[55]:


# Program to print ASCII Value of a character
def fun2(a):
    print(ord(a))
fun2('a')
# ord function is used to ascii value of a characte


# In[57]:


def fun(a):
    return chr(a)
fun(65)


# In[58]:


# Python program to add two numbers
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=a+b
print(c)


# In[59]:


# Python program to print maximum of two numbers
def fun(a,b):
    if a>b:
        print(a," is greter")
    else:
        print(b," is greter")
fun(1,7)


# In[61]:


# python program for factorial of a number
def funa(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact)
funa(5)


# In[62]:


# Python program for simple interest
def fun():
    p=int(input("Enter the principle amount"))
    t=int(input("Enter the tenure in months"))
    r=int(input("Enter the rate of interest"))
    si=(p*t*r)/100
    print(si)
fun()


# In[ ]:




