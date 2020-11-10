#!/usr/bin/env python
# coding: utf-8

# # PYTHON TASK

# Import necessary libraries

# In[1]:


import random
import math
import string
import timeit


# ## 1. Generate 6 digit OTP

# In[2]:


def genOTP():
    OTP = ''
    for i in range(6):
        OTP += str(random.randint(0,9))
    return OTP


# In[3]:


'''Total time taken by the function to create 6 digit OTP in a loop that runs 1000000 times'''

code1='''
def genOTP():
    OTP = ''
    for i in range(6):
        OTP += str(random.randint(0,9))
    return OTP
'''

print("Time taken in sec:",timeit.timeit(stmt= code1))


# ## 2. Generate random 5 character password with a combination of alphabets 
# ##### (lower and upper case combination )

# In[4]:


def get_random_string():
    letters=string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(5))
    return result_str


# In[5]:


'''Total time taken by the function to create 5 character password in a loop that runs 1000000 times'''

code2='''
def get_random_string():
    letters=string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(5))
    return result_str
'''

print("Total time (in sec):",timeit.timeit(stmt=code2))


# ## 3. Generate 10 character password 
# #### ( atleast a digit, a special character, 2 uppercase characters)

# In[6]:


def pass_gen():
    password_char=string.ascii_letters+string.digits+string.punctuation
    passwrd = ''.join(random.choice(password_char[26:52]) for i in range(2))+''.join(random.choice(password_char[52:62]))+''.join(random.choice(password_char[62:94]))+''.join(random.choice(password_char) for i in range(6))
    pass_list= random.sample(passwrd,len(passwrd))
    pass_word=''.join(pass_list)
    return pass_word


# In[7]:


'''Total time taken by the function to create 10 character password in a loop that runs 1000000 times'''

code3='''
def pass_gen():
    password_char=string.ascii_letters+string.digits+string.punctuation
    passwrd = ''.join(random.choice(password_char[26:52]) for i in range(2))+''.join(random.choice(password_char[52:62]))+''.join(random.choice(password_char[62:94]))+''.join(random.choice(password_char) for i in range(6))
    pass_list= random.sample(passwrd,len(passwrd))
    pass_word=''.join(pass_list)
    return pass_word
'''

print("Total time taken (in sec): ",timeit.timeit(stmt=code3))


# In[ ]:




