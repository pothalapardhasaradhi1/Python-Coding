#!/usr/bin/env python
# coding: utf-8

# In[19]:


# ATM Machine Code
import datetime
username="pardhu"
password="Python@123"
c_name=input("Enter your username")
c_password=input("Enter your pasword")
if c_name==username and c_password==password:
    print("""
    1.Deposit
    2.Withdraw
    3.Ministatement
    4.Exit""")
    amount=50000 #default amount
    option=int(input("Select your option based on index number"))
    if option==1:
        dep=int(input("Enter the amount"))
        amount=amount+dep
        print("Total amount :",amount)
    elif option==2:
        with1=int(input("Enter the amount"))
        if amount>=with1:
            amount=amount-with1
            print("The available balance is :",amount)
        else:
            print("Please choose the amount below or equal available amount: ",amount)
    elif option==3:
        print("========ATM==========")
        print("Username:",username)
        print("Total amount",amount)
        print("Thanks for visiting")
        print("Current date and time: ",datetime.datetime.now())
        print("====================")
    elif option==4:
        print("Thanks for viting ",username)
else:
    print("Invalid data")


# In[23]:


# Dice roll simulator
import random
print("""1.Roll the dice 
2.exit""")
user=int(input("choose "))
if user==1:
    num=random.randint(1,6)
    print(num)
else:
    print("Exit")


# In[25]:


# Guess the number
import random
number=random.randint(1,10)
a=int(input("Number of chances you want"))
for i in range(a):
    user=int(input("Guess the number"))
    if user==number:
        print("You guess the correct number",number)
        
        print("and the",i+1,"chance")
        break


# In[27]:


# Random password generator
import random
a=int(input("Enter the password length"))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*"
print("".join(random.sample(s,a)))


# In[15]:


a="pavan kumar"
print("  ".join(a))


# In[9]:


# Write a dictionary named as “data1” with Id, Name, and Designation and add values as 1, John, 
# SC and print the length of the dictionary, type and print the data1. 
data1={"Id":1,"Name":"John","Designation":"SC"}
print(data1)
print(type(data1))
print(len(data1))


# In[10]:


# Print all the keys of the dictionary named as”data1”.
print(data1.keys())


# In[11]:


# Print all the values of the dictionary named as “data1”. 
print(data1.values())


# In[12]:


# Print the specific key named as “designation” for the dictionary “data1”. 
print(data1["Designation"])


# In[13]:


# Write a dictionary named as “data2” with Id, Name, 
# and Designation and add values as 2, Ajay, PC and update the key name as “Arjun”. 
data2={"Id":2,"Name":"Ajay","Designation":"PC"}
data2["Name"]="Arjun"
print(data2)


# In[14]:


# Clear all the values for the dictionary named as “data1” and print it
data1={"Id":1,"Name":"John","Designation":"SC"}
data1.clear()
print(data1)


# In[16]:


# Delete the dictionary named as”data2”. 
data2={"Id":2,"Name":"Ajay","Designation":"PC"}
del data2
print(data2)


# In[18]:


# Write a python code  to perform string manipulations and get the 3 input at runtime 

# And enter the value as “Welcome”, ”hello”, ”hello python” and convert the second
# input into uppercase and check whether is converted into uppercase or not. 
a=input()
b=input()
c=input()
d=b.upper()
if d.isupper():
    print("Converted into uppercase")
else:
    print("Not converted")


# In[29]:


# For the same string code print the length of the 
# third string and check whether the third string is digit or not. 
print(len(b))
print(c.isdigit())


# In[31]:


# For the same string code convert the first string into 
# swap case and check whether the first string is alphabet or not. 
a="hello"
print(a.swapcase())
print(a.isalpha())


# In[33]:


# For the same string code count the number of letter “l” for the second string value and replace “l” as “k”. 
a="hello python"
print(a.count("l"))
print(a.replace("l","R"))


# In[41]:


# For the same string code append the “#” before the third string use lstrip () 
# and capitalize the initial letters in each word. 
a=" pavan "
print(len(a))
p=a.lstrip()
print(len(p))
print(p.capitalize())
print(p.title())


# In[43]:


#  Given two sets namely as A={1,2,9,3,1,3,7,9,3,1,3,2,4,5,6} and B={5,8,4,3,7,8} and 
# perform set operations namely union, intersect,
# difference and symmetric_difference use set methods not operator symbols.
A={1,2,9,3,1,3,7,9,3,1,3,2,4,5,6}
B={5,8,4,3,7,8}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))


# In[ ]:




