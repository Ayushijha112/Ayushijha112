#!/usr/bin/env python
# coding: utf-8

# 
# # factorial program
# 

# In[2]:



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("enter the number"))# for python3.x
print(factorial(n))


# # Average of 10 numbers
# 

# In[3]:


sum=0
for i in range(10):
    n=int(input("enter the number"))
    sum=+n
average = sum/10
print("Average of given number are :",average)


# # Fibonacci series
# 

# In[5]:


num=int(input("enter the number: "))
n1=0
n2=1
print("fibonacci series: ",n1, n2, end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")


# In[ ]:




