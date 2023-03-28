#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Numpy is  a python library used for working with arrays
import numpy
arr=numpy.array([1,2,3,4,5,6])
print(arr)
print(type(arr))


# In[4]:


import numpy as np
arr=np.array(["pavan","ashish","sanju"])
print(arr)
print(type(arr))


# In[5]:


import numpy as np
print(np.__version__)


# In[6]:


import numpy as np
arr=np.array(8)
print(arr)
# ) dimesion array


# In[7]:


# 1 dimesional array
import numpy as np
arr=np.array([1,2,3,"pava"])
print(arr)


# In[9]:


# 2 Dimesional array: it contains rows and columns
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(type(arr))


# In[12]:


# 3 dimesional array
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]]])
print(arr)


# In[17]:


# Check Number of Dimensions?
import numpy as np
arr=np.array(8)
print(arr.ndim)
arr=np.array([1,2])
print(arr.ndim)
arr=np.array([[1,3,4]])
print(arr.ndim)
arr=np.array([[[1,2,3],[6,98,0]]])
print(arr.ndim)


# In[18]:


# if you want set number of dimesions to particular array {ndmin}
import numpy as np
arr=np.array([1,2,3],ndmin=7)
print(arr.ndim)


# In[21]:


# Acces array elements
import numpy as np
arr=np.array([1,2,3,3,55,5])
print(arr[0])
print(arr[-1])
print(arr[0]+arr[-1])


# In[29]:


import numpy as np
arr=np.array([[1,2,3,4,5,6],[8,0,5,7,8,11]])
print(arr[0,0])
print(arr[0,-1])
print(arr[1,-1])
print(arr[1,1])
print(arr[1,0])
print(arr[1,9])


# In[35]:


import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]])
# Combination of 2d arrays we can call it as 3d array
print(arr.ndim)
print(arr[0,1,1])
print(arr[-1,-1,-1])
print(arr[0,0,0])
print(arr[1,1,0])


# In[47]:


# Slicing
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr)
print(type(arr))
print(arr[:1])
print(arr[1:5])
print(arr[:6])
print(arr[3:])
print(arr[::2])
print(arr[::-1])
print(arr[-5:-2])
# for negative indexing always right side is higher values


# In[63]:


import numpy as np
arr=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr[1,::-1])
print(arr[0,1:5])
print(arr[:,2])
print(arr[:,0])
print(arr[:1,0])
print(arr[:,-1])


# In[3]:


import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(type(arr))
print(arr.ndim)


# In[10]:


import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[77,88,55],[22,44,666]]])
print(arr.ndim)
print(type(arr))
print(arr[0:2])


# In[13]:


# NUMPY Data Types
import numpy as np
arr=np.array([1,2,3,5])
print(type(arr))
print(arr.ndim)
print(arr.dtype)


# In[15]:


import numpy as np
arr=np.array(["pavan","ashish","sanju","naga"])
print(arr.dtype)


# In[17]:


import numpy as np
arr=np.array(["pavan","ash"],dtype="S")
print(arr.dtype)


# In[18]:


import numpy as np
arr=np.array([3.6,7.8,9.45])
print(arr.dtype)


# In[19]:


# astype is used to convert data
import numpy as np
arr=np.array([1,2,3])
p=arr.astype(float)
print(p)
print(type(p))
print(p.dtype)


# In[28]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
a=arr.copy()
b=arr.view()
print(a)
print(b)
a[0]=100
print(a)
b[-1]=1009
print(b)
print(a.base)
print(b.base)


# In[29]:


import numpy as np
arr=np.array([1,2,3,4,55,55,4432,2,2,3,4,4])
x=arr.copy()
print(x.base)
# copy will not show data verses view will show data


# In[31]:


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(arr.shape)


# In[32]:


import numpy as np
arr=np.array([[1,2,3,4],[6,7,8,9]])
print(arr.shape)


# In[35]:


import numpy as np
arr=np.array([1,2,3],ndmin=5)
print(arr.shape)


# In[38]:


# REshaping arrays
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
p=arr.reshape(4,3)
print(p)
print(p.dtype)
# 1D to 2D


# In[42]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
p=arr.reshape(3,2,2)
print(p)
print(p.ndim)


# In[43]:


# Convert an 2d array into 1d array
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
p=arr.reshape(-1)
print(p)


# In[47]:


import numpy as np
arr=np.array([[[1,2,3],[4,5,8]],[[77,99,66],[666,333,662]]])
print(arr.reshape(-1))
print(arr.reshape(-5))


# In[51]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2,2)

print(newarr)


# In[53]:


import numpy as np
arr=np.array([1,2,3,3,545,66,7,87,8,766,65])
for i in arr:
    print(i,end=" ")


# In[54]:


for i in enumerate(arr):
    print(i)


# In[56]:


import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for i in arr:
    print(i,end=" ")


# In[58]:


for i in arr:
    for j in i:
        print(j,end=" ")


# In[64]:


import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[77,88,99],[333,666,8888]]])
print(arr.ndim)
for i in arr:
    print(i)
print("_______________________________")
print()
for i in arr:
    for j in i:
        print(j)
print("_____________________________________")


# In[66]:


for i in arr:
    for j in i:
        for p in j:
            print(p,end=" ")


# In[68]:


# if we have more dimesions then will got for nditer for iterations
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[22,1,11],[55,44,333]]])
for i in np.nditer(arr):
    print(i,end=" ")


# In[ ]:




