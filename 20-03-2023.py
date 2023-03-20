#!/usr/bin/env python
# coding: utf-8

# In[2]:


# OOPs
class Mycls:
    x=5
print(Mycls)
print(Mycls.x)


# In[5]:


class Myclass:
    x=5
p=Myclass()
print(p.x)
print(Myclass.x)


# In[7]:


class Mycls:
    x=5
    def __init__(self):
        print("Hello pardhu")
p=Mycls()
# whenever we create an object it will be executed


# In[12]:


class Mycls1:
    x=5
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Constrctor")
p=Mycls1("Pardhu",24)
print(p.a)


# In[18]:


# __str__ method reads objects data
class Mycls:
    a=10
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        return f"{self.a},{self.b}"
p=Mycls(10,"pavan",7)
print(p)
# whenever we call the object it will be executed without calling of str method


# In[24]:


# Methods 
class pavan:
    a=100
    def __init__(self,name,g,a):
        self.name=name
        self.g=g
        self.a=a
    def __str__(self):
        return f" The name:{self.name}"
    def pav(self):
        print("Gender :",self.g)
        print("Age: ",self.a)
a1=pavan("Pavan","M",24)
print(a1)
a1.pav()


# In[3]:


a=int(input("enter a value"))
if a>18:
    print(a,"is greter than 18")


# In[5]:


a=int(input("Enter your age"))
if a>=18:
    print("You are eligible for voting")
else:
    print("Not eligible")


# In[7]:


a=int(input("enter a number"))
if a>0:
    print("positive")
elif a==0:
    print("Zero")
else:
    print("negative")


# In[8]:


# Even or odd
a=int(input("Enter a number"))
if a%2==0:
    print("Even number")
else:
    print("Odd number")


# In[11]:


# largest of three numbers
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("a is greater")
elif b>c and b>a:
    print("b is greater")
else:
    print("C is greater")


# In[14]:


a="Pothala pardhu"
if a.endswith("pardhu"):
    print("yes")
else:
    print("No")


# In[15]:


# 1. Write a Python function named as "sum" with two parameters as a and b and pass the value as 10, 20 with 1 function call. 
def sum(a,b):
    return a+b
sum(10,20)


# In[16]:


# 2. Write a Python function named as "sum" with two parameters as a and b and pass the value as 10 with 1 function call. 
def sum(a,b):
    return a+b
sum(10)


# In[20]:


# 3. Write a Python function named as "greetings" with three parameters as id, name and age as 21 and with 1 function call as id equal to 20 and name equal to John.greetings(id,name,age=21):

def greetings(name,id,age=21):
    print("ID:",id)
    print("NAME:",name)
    print("AGE:",age)
greetings("pardhu",201)


# In[27]:


# 4. Write a Python function named as "greetings" with three parameters as id, name and age as 21 and with 1 function call as id equal to 20 and name equal to John, age equal to 25. 
def greetings(id,name,age=20):
    print(id,name,age)
greetings(21,"John")


# In[28]:


# Write a Python statements a=[1,2,3] b=(1,2,3) c={'id':1,'name':'Vikram'} find its type.
a=[1,2,3]
a=(1,2,3)
c={"id":1,"name":"Vikram"}
print(type(a),type(b),type(c))


# In[29]:


# Write a Python statement gets the employee name and eid inputs at runtime and print it. 
def fun(name,eid):
    print("Employee name",name)
    print("Employee id",eid)
fun("pardhu",121)
    


# In[31]:


# 7. Write a Python loop print the numbers from 1 to 10. 
def fun(a):
    for i in range(1,a+1):
        print(i)
fun(10)


# In[33]:


# 8. Write a Python loop print the numbers as start=5, end=9 and step=1. 
def fun(a,b):
    for i in range(a,b+1):
        print(i,end=" ")
        
fun(5,9)


# In[34]:


# 9. Write a Python loop print the list of numbers from 1 to 10 in the list format. 
def fun(a):
    b=[]
    for i in range(1,a+1):
        b.append(i)
    print(b)
fun(10)


# In[39]:


# 10. Write a Python enumerate function and print the colors namely as red, green and blue.
def fun():
    a=["red","green","blue"]
    c=enumerate(a)
    print(list(c))
fun()


# In[ ]:




