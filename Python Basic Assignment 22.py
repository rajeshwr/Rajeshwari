#!/usr/bin/env python
# coding: utf-8

# 1. What is the result of the code, and explain?
# 
# X = 'iNeuron'
# 
# def func():
# 
# print(X)
# 
# func()

# In[1]:


#The line, func() Call the function we defined which prints the value of X

X = 'iNeuron'
def func():
    print (X)


# In[2]:


func()


# 2. What is the result of the code, and explain?
# 
# X = 'iNeuron'
# 
# def func():
# 
# X = 'NI!'
# 
# func()
# 
# print(X)

# In[4]:


# The line, func() Call the function we defined, with "NI" as the value of X inside the funtion, but doesn't prints it, as there is no print statement inside the function.
#The line, print(X), prints the value of X, which is "iNeuron", which is outside func().

X = 'iNeuron'
def func():
    X = 'NI!'
func()


# In[5]:


print(X)


# 3. What does this code print, and why?
# 
# X = 'iNeuron'
# 
# def func():
# 
# X = 'NI'
# 
# print(X)
# 
# func()
# 
# print(X)

# In[6]:


#The line, func() Call the function we defined which prints the value of X, which is "NI" inside the funtion.

#The line, print(X), prints the value of X, which is "iNeuron", which is outside func().

X = 'iNeuron'
def func():
    X = 'NI!'
    print (X)
func()


# In[7]:


print(X)


# 4. What output does this code produce? Why?
# 
# X = 'iNeuron'
# 
# def func():
# 
# global X
# 
# X = 'NI'
# 
# func()
# 
# print(X)

# In[8]:


#The line, func() Call the function we defined, with "NI" as the value of X inside the funtion, but doesn't prints it, as there is no print statement inside the function, and we have used global keyword, which means, global keyword allows us to modify the variable, that is "X", outside of the current function.

#The line, print(X), prints the value of X, which is now "NI", as we used global keyword inside the function.

X = 'iNeuron'
def func():
    global X
    X = "NI"
func()


# In[9]:


print(X)


# 5. X = 'iNeuron'
# 
# def func():
# 
# X = 'NI'
# 
# def nested():
# 
# print(X)
# 
# nested()
# 
# func()
# 
# X

# In[10]:


X = 'iNeuron'
def func():
    X = "NI"
def nested():
    print(X)
nested()


# 6. def func():
# 
# X = 'NI'
# 
# def nested():
# 
# nonlocal X
# 
# X = 'Spam'
# 
# nested()
# 
# print(X)
# 
# func()

# In[17]:


# The nonlocal keyword is used to work with variables inside nested functions, 
#where the variable should not belong to the inner function.Use the keyword nonlocal to declare that the variable is not local.

def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()


# In[18]:


print(X)


# In[23]:


func()


# In[24]:


print(func())


# In[ ]:




