#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Conditions: based on conditions only it will display block of code
# We have following conditions statements
# 1.if
# 2.if else
# 3.if...elif ladder
print("if condition is true then only execute the block of code")


# In[2]:


# IF condition
a=int(input("Enter your age"))
if a>=18:
    print("You are eligible for voting")


# In[7]:


a=10
b=23
if a>b:
    print(str(a)+" is greter than "+str(b))


# In[8]:


# elif keyword will be executed if the previous condition was not true
a=10
b=10
if a>b:
    print("a is greter than b")
elif a==b:
    print("a and b are equal")
# we can have multiple elif cases one program


# In[17]:


a=int(input("Enter the number"))
if a>=0 and a<=9:
    print("one's value")
elif a>=10 and a<=99:
    print("ten's value")
elif a>=100 and a<=999:
    print("hundreds value")
else:
    print("Invalid data")
# else is default case means if not satisfied every condition in program it will be executed else case 


# In[18]:


a=10
b=20
c=30
if a>b or c>b:
    print("if any one of the condition is true then executed")


# In[19]:


# Not operator
a=10
b=2
if not a<b:
    print("if the condition false then only executed not operator")


# In[23]:


# one condition inside another condition we can call it as nested condition
a=int(input("Enter a value"))
b=int(input("enter b value"))
c=int(input("Enter c value"))
if a>b:
    if a>c:
        print(str(a)+" is greter")
if b>a:
    if b>c:
        print(str(b)+" is greter")
else:
    print(str(c)+" is greater")


# In[25]:


# Pass statement is used to avoid errors
# to write empty loops as well as empty conditions
a=10
b=4
if a>b:
    pass


# In[29]:


#Switch case:it also same as if elif ladder
def switch(lang):
    if lang=="javascript":
        print("You are become a web developer")
    elif lang=="python":
        print("you are become a python developer")
    elif lang=="java":
        print("You are become a java developer")
    else:
        print("Invalid role")
switch("java")


# In[39]:


# Write a switch case program to check if a letter is a vowel
def switch(ab):
    if ab=="a" or ab=="A":
        print(ab+" is vowel")
    elif ab=="e" or ab=="E":
        print(ab+" is vowel")
    elif ab=="i" or ab=="I":
        print(ab+" is vowel")
    elif ab=="o" or ab=="O":
        print(ab+" is vowel")
    elif ab=="u" or ab=="U":
        print(ab+" is vowel")
    else:
        print(ab+" is Not a vowel")
switch("i")


# In[43]:


def operations(letter):
    switch={
        'a':"it is an vowel",
        'e':"it is an vowel",
        'i':"it is an vowel",
        'o':"it is an vowel",
        'u':"it is an vowel",
    }
    return switch.get(letter,"it is not an vowel")
operations("a1")


# In[47]:


def check(mail):
    if mail.endswith("@gmail.com"):
        print("valid")
    else:
        print("Invalid")
check("ac@gmail.com")


# In[49]:


check("@cvaGmail.com")


# In[53]:


# Write a function to print the price of the following in the menu
# on giving the input as either of the numbers from 1 to 5.
def menu():
    a=input("Enter your name")
    print("hello",a,"Welcome to Food court")
    print("""Choose the food based on index numbers
          1.Chicken Biryani Rs 300/-
          2.Mutton Biryani Rs 350/-
          3.Chapathy Rs 50/-
          4.Dosa Rs 30/-
          5.Curd Rice Rs 100/-""")
    b=int(input("Choose your food based index number"))
    if b==1:
        print("You have choose Chicken biryani")
    elif b==2:
        print("You have choose Mutton biryani")
    elif b==3:
        print("ypu have choose chapathy")
    elif b==4:
        print("You have choose dosa")
    elif b==5:
        print("you have choose curd rice")
    else:
        print("Invalid data")
    print("Thank you for choosing"+a)
menu()


# In[ ]:




