#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Functions are nothing but a block of code which can be write once execute any number of times
# Code resusability
# Segmentaion
# def is a keyword to define a function in python



# Creating a Function
def function():
    print("Hello world")
function()


# In[4]:


# Passing arguments to function
# arguments is nothing but a input to the function
def fun(name):
    print("hello ",name)
fun("Ashish")


# In[5]:


# Number of Arguments
def fun1(a,b):
    print(a+b)
fun1(10,40)


# In[6]:


# Arbitrary Arguments, *args
# variable number of arguments
# if we dont have any idea to pass number arguments to the functions means we can use *args
def fun(*a):
    print(a[0])
    print(a[5])
fun("p","q","r","s","t","u","v")


# In[7]:


# Keyword Arguments
# we can pass keys to the function input and get value
def fun(a,b,c):
    print(b)
fun(a="pavan",b="nagarju",c="ashish")


# In[8]:


# Keyword arguments
# if we dont have any idea to pass number keys to functions
# we can go for kwargs
def fun(**kwags):
    print(kwags["lname"])
fun(fanme="pothala",lname="pardhu")


# In[10]:


def fun3(**num):
    print(num["even"])
fun3(even=2,odd=1,zero=0)


# In[13]:


# Default Parameter Value
def fun(a=10):
    print("The value of a",a)
fun()  


# In[14]:


def fun(a,b=25):
    print(a+b)
fun(10,5)


# In[15]:


fun(10)


# In[16]:


# Passing a List as an Argument
def fun(a):
    for i in a:
        print(i)
a=[1,2,3,4,4,5]
fun(a)


# In[17]:


# Return statement
def fun(a):
    return a*5
fun(7)


# In[20]:


def fun1(a):
    return "the value of a is",a
fun1(6)


# In[21]:


# pass statement is used to avoid getting errors
# to write empty functions
def fun(p):
    pass
fun("a")


# In[26]:


# REcursive function:
# a function that can be called by itself we can call it as recursive
def fib(n):
    if n<0:
        return "NA"
    elif n==0:
        return 1
    else:
        return n*fib(n-1)


# In[27]:


fib(5)


# In[ ]:




