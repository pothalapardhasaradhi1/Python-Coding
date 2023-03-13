#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python List Excercises
# 1. Python program to interchange first and last element in a list
def fun(a):
    a[0],a[-1]=a[-1],a[0]
    return a
fun([1,2,3,4,5])


# In[3]:


# Python3 program to swap elements
def fun1(a):
    p,q=1,3
    a[p],a[q]=a[q],a[p]
    
    return a
fun1([1,2,3,4,5,6,7])
#we have changed 1 and 3 rd index locations


# In[5]:


# python program to  find length of list
def fun3(a):
    i=0
    for j in a:
        i=i+1
    print("Length of the list is",i)
fun3([4,6,7,8,99,99])


# In[6]:


# MInimum of two numbers
def fun4(a,b):
    if b<a:
        print(b," is minimum")
    else:
        print(a," is minimum")
fun4(10,45)
    


# In[8]:


# Check if element exists in list in Python
def fun6(a):
    b=int(input("Enter a  number"))
    if b in a:
        print(b, " is present in a")
    else:
        print(b," is not present in a")
fun6([1,2,3,4,5,6,7,7])
        


# In[9]:


# clear a list in Python
def fun7(a):
    a.clear()
    return a
fun7([2,3,4])


# In[10]:


def fun8(a):
    del a
    return a
fun8([1,5])


# In[11]:


# Reversing a List in Python
def fun9(a):
    b=a[::-1]
    return b
fun9([1,2,3,4])


# In[19]:


def fun10(a):
    a.reverse()
    return a
fun10([1,2,3,45,45])


# In[10]:


def fun11(a):
    b=sorted(a,reverse=True)
    return b
        
    
fun11([1,2,3,4,5])     


# In[13]:


# Python | Program to print duplicates from a list of integers
def fun12(a):
    u=[]
    d=[]
    for i in a:
        if i not in u:
            u.append(i)
        elif i not in d:
            d.append(i)
    print(d)
fun12([1,2,3,9,4,5,6,7,8,8,8,9,0,0])


# In[16]:


# Python | Remove empty tuples from a list
def fun(a):
    for i in a:
        if(len(i)==0):
            a.remove(i)
    return a
fun([(),(1,2),(5,7,9)])


# In[23]:


# Python Program to remove even numbers in a given list
a=[1,2,5,99,1000,2345,66,78,90]
def fun(a):
    for i in a:
        if i%2==0:
            a.remove(i)
    return a
fun(a)


# In[24]:


# Remove numbers in particular index position in agiven list
def fun(a):
    del a[1:4]
    return a
a=[1,2,3,4,5,65,67,8,88]
fun(a)


# In[33]:


# Python program to count positive and negative numbers in a list
def fun(a):
    n=0
    p=0
    for i in a:
        if i>0:
            p=p+1
        else:
            n=n+1
    return "positive",p,"Negative",n
a=[1,2,3,4,5,6,6,-3,-4,-1]          
fun(a)           


# In[51]:


# Python program to print all negative numbers in a range
def fun(a,b):
    d=[]
    for i in range(a,b):
        d.append(i)
        
        
        
        print(i,end=" ")
    print("\n",d)
fun(-10,-3)


# In[57]:


# Python program to print positive Numbers in given range
def fun(a,b):
    for i in range(a,b):
        if i>0:
            print(i,end=" ")
fun(-3,9)


# In[68]:


# python program to count even and odd numbers in a list
def fun(a):
    e=0
    o=0
    for i in a:
        if i%2==0:
            e=e+1
        else:
            o=o+1
    print("Even numbers count",e)
    print("Odd numbers count",o)
    print(len(a))
fun([1,2,3,4,5,6,7,8,9,66,44,33,22,23,44,9])    


# In[76]:


# Python program to find second largest number in a list
def fun(a):
    a.sort()
    return a[-2]
fun([1,2,3,4,5,6,7,844,33,22,11,222,77,0,1,2,5])


# In[79]:


a=[1,2,3,4,5,5]
b=set(a)
c=list(b)
print(c[-2])


# In[80]:


# Python program to find largest number in a list
def fun(a):
    print(max(a))
fun([1,2,3,4,56])


# In[81]:


def fun(a):
    a.sort()
    print(a[-1])
fun([2,7,8,98,77])


# In[84]:


# Python | Multiply all numbers in the list
def fun(a):
    res=1
    for i in a:
        res=res*i
    return res
fun([1,2,3,4,5])


# In[86]:


# Python program to sum of all numbers in the list
def fun(a):
    res=0
    for i in a:
        res=res+i
    return res
fun([1,2,3,4,5])


# In[88]:


# Find sum andaverage of List in Python
def fun(a):
    a=int(input("Enter the number of elements you want"))
    b=[]
    for  i in range(a):
        i=int(input("Enter the number you want to add"))
        b.append(i)
    d=a
    sum=0
    for i in b:
        sum=sum+i
    print("Sum is ",sum)
    print("Avg",sum/d)
fun(a)       


# In[89]:


# Count the number of occurances in the given list
def fun(a):
    b=a.count(7)
    print(b)
fun([7,7,7])


# In[90]:


# Copy
a=[1,2,3]
b=a
print(b)


# In[91]:


a=[1,4,9,0,77]
b=a.copy()
print(b)


# In[97]:


a=[1,2,"pavan",True,"Pavan"]
print(len(a))
print(type(a))
print(a)
print(a[2])
print(a[:3])


# In[99]:


a=[1,2,3,4,5]
if 21 in a:
    print("Yes it is avialble")
else:
    print("It is not available")


# In[100]:


# Change the value
a=[1,2,3,4]
a[0]=100
print(a)


# In[103]:


a=[1,2,3,4,5,6,7]
a[0:4:3]=100,200
print(a)


# In[104]:


# adding element into list
a=[1,2]
a.append("pardhu")
print(a)


# In[105]:


# insert method
a=[1,2,3,4,6,8]
a.insert(1,"sarada")
print(a)


# In[108]:


# extend method
a=[1,2,3]
a.extend([2,4,9,1000])
print(a)


# In[109]:


# pop
a=[1,2,3,4,5,6]
print(a.pop())


# In[114]:


a=[1,2,3,4]
a.pop()
print(a)


# In[115]:


a=[1,2,3,4]
a.pop(1)
print(a)


# In[116]:


# remove
a=[1,2,3,4]
a.remove(4)
print(a)


# In[117]:


# clear method
a=[1,2,3]
a.clear()
print(a)


# In[118]:


# del
a=[1,2,34]
del a
print(a)


# In[119]:


print(d)


# In[120]:


a=[100,56,8,0,55]
a.sort()
print(a)


# In[124]:


a=[1,2,3,4,5,56,567,3,42,1,9]
a.reverse()
print(a)


# In[126]:


a=[1,2,3,4,5,100,10,200,20]
b=sorted(a,reverse=True)
print(b)


# In[127]:


# copying a list
a=[1,2,3]
b=a
print(b)


# In[128]:


a=[1,2,3]
b=a.copy()
print(b)


# In[129]:


# Joining of a lists
a=[1,23]
b=[4,99]
c=a+b
print(c)


# In[ ]:




