#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pandas is python library mainly used for data analysis
# pandas library mainly works with the tabular data
# we have 3 types data strctures
# Series:1 d(single column data)
# dataframe 2d(roes and column)
# panel 3d
import pandas
# check whether the library installed or not


# In[2]:


import keras


# In[4]:


print(pandas.__version__)
# Check version of pandas


# In[7]:


# collection of data in the form of tabular form we can call it as datasets
# free data sets avaialable in kaggle.com
# Creating a dataframe
# dats set may in the form two forms execl or csv
import pandas as pd
d=pd.read_csv("student.csv")
# LOad the data
df=pd.DataFrame(d)
print(df)
# same foe execel aso
# pd.read_excel("s.xlsx")


# In[8]:


di={"Name":["pavan","ashish","Pardhu","Sanju"],"Roll_Number":[101,102,103,104],"Percentage":[90,77,90.6,66]}
df=pd.DataFrame(di)
print(df)
# Key name will be act as column name


# In[9]:


# using list of tuples to create dataframe
ti=[("abc",101,90),("cfg",102,78),("dfgh",103,90)]
df=pd.DataFrame(ti)
print(df)


# In[10]:


import pandas as pd
d=[("pspk",1,50),("Rc",2,40),("Rebal",3,60)]
df=pd.DataFrame(d)
print(df)


# In[13]:


# INDEXING SLICING
import pandas as pd
d=pd.read_csv("student.csv")
df=pd.DataFrame(d)
print(df.head())


# In[14]:


print(df.head(2))


# In[15]:


print(df.tail())


# In[16]:


print(df.tail(10))


# In[18]:


print(df.tail(1))


# In[19]:


df.head(0)


# In[20]:


df.describe()


# In[22]:


df.shape


# In[23]:


df[0:10:1]


# In[24]:


df[0:10:2]


# In[26]:


df["Roll_No"]


# In[27]:


df[["Roll_No","Telugu"]]


# In[28]:


df[["Telugu","English","Maths"]]


# In[32]:


df["Telugu"][:5]


# In[33]:


df["English"][0:15:3]


# In[35]:


df[["Telugu","English","Maths"]][:2]


# In[38]:


df["Telugu"]+df["English"]


# In[39]:


for i in df.iterrows():
    print(i)


# In[40]:


# if you want to get data invidually with headers we can go for iterrows
for i in df:
    print(i)


# In[41]:


for i in df.iterrows():
    print(i)
# tuple of data invidually will get it


# In[44]:


# LOC (Stop index also included)
import pandas as pd
d=pd.read_csv("student.csv")
df=pd.DataFrame(d)
df.loc[0:10]


# In[48]:


df.loc[:][:3]


# In[49]:


df.loc[0]


# In[50]:


df.loc[10]


# In[51]:


df[10]


# In[52]:


df.loc[21]


# In[53]:


df.loc[19,"Telugu"]


# In[55]:


df.loc[19,["Telugu","English"]]


# In[56]:


df.loc[0:5]


# In[64]:


df.loc[0:6:2,"Telugu"]


# In[68]:


df.loc[0:6,"Telugu":"Maths"]


# In[69]:


df.loc[9,"Roll_No":"Maths"]


# In[71]:


# ILOC: excluded index value
# Column name refer to the number onluy
import pandas as pd
d=pd.read_csv("student.csv")
df=pd.DataFrame(d)
df.iloc[0:6]


# In[72]:


df.iloc[::3]


# In[75]:


df.iloc[:,2:6]


# In[77]:


df.iloc[:]


# In[80]:


df.iloc[1:3,[2,4]]


# In[81]:


df.iloc[2:4,1:4]


# In[82]:


# Sorting Dataframe
df


# In[83]:


df.sort_values("Maths")


# In[84]:


df.sort_values("Maths",ascending=False)


# In[86]:


df.sort_values(["Name_Of_Student","Maths"])
# most priority belongs to first parameter itself


# In[87]:


# Manipulating datframe
df["Total"]=0


# In[88]:


df


# In[89]:


df["Total"]=df["Telugu"]+df["English"]+df["Maths"]+df["Science"]+df["Social"]
df
# Adding column


# In[90]:


# Removing a column
df["Perc"]="Pass/fail"
df


# In[92]:


print(df.drop(columns="Perc"))


# In[93]:


df


# In[94]:


df.drop(columns="Perc",inplace=True)
df


# In[96]:


# inplace is true then all changes apply to the data frame
df.drop(columns=["Telugu","English"])
df


# In[98]:


# REmoving duplicates
# Duplicated() is used to check it contains duplicates or not
df.duplicated()


# In[99]:


import pandas as pd
df=pd.read_csv("student1.csv")
df1=pd.DataFrame(df)
df1


# In[100]:


df1.duplicated()


# In[101]:


df1.drop_duplicates()


# In[102]:


df1


# In[103]:


df1.drop_duplicates(inplace=True)
df1


# In[104]:


df1


# In[105]:


# Handling the missing data
import pandas as pd
d=pd.read_csv("student2.csv")
df=pd.DataFrame(d)
df


# In[106]:


df.dropna()


# In[107]:


df


# In[108]:


df.fillna(80)
# by default fill data by 80


# In[114]:


df["Name_Of_Student"].fillna("pavan",inplace=True)


# In[115]:


df


# In[116]:


df.dropna(inplace=True)


# In[117]:


df


# In[118]:


# permently do operation means we have to go through
# inplace =True
df


# In[120]:


# data filtering and conditional change 1:14
import pandas as pd
d=pd.read_csv("student.csv")
df=pd.DataFrame(d)
df.loc[df["Maths"]>70]
# simple condition


# In[123]:


# if you can use 2 simple conditions we can acll it as compuund condition
df.loc[(df["Maths"]>60)& (df["Maths"]<80)]


# In[124]:


df.loc[df["Name_Of_Student"].str.contains("n")]


# In[127]:


df.loc[df["Name_Of_Student"].str.startswith("P")]


# In[128]:


df.loc[df["Name_Of_Student"].str.endswith("n")]


# In[131]:


df.to_excel("p.xlsx")


# In[133]:


df.to_csv("p.csv",index=False)


# In[136]:


import sys
import numpy as np
import pandas as pd
print(sys.version)
print(np.__version__)
print(pd.__version__)


# In[138]:


d=pd.Series(np.random.randn(5))
d


# In[ ]:




