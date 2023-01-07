#!/usr/bin/env python
# coding: utf-8

# 1. Add the current date to the text file today.txt as a string.

# In[1]:


from datetime import date
now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    print(now_str, file=output)


# 2. Read the text file today.txt into the string today_string

# In[2]:


with open('today.txt', 'rt') as input:
    today_string = input.read()
    
today_string


# 3. Parse the date from today_string.

# In[3]:


from datetime import datetime
fmt = '%Y-%m-%d\n'
datetime.strptime(today_string, fmt)


# 4. List the files in your current directory

# In[4]:


import os
os.listdir('.')


# 5. Create a list of all of the files in your parent directory (minimum five files should be available)

# In[5]:


os.listdir('..')


# 6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.

# In[ ]:


get_ipython().system('python multi_process.py')


# 7. Create a date object of your day of birth.

# In[8]:


my_day = date(1983, 3, 15)
my_day


# 8. What day of the week was your day of birth?

# In[9]:


my_day.weekday()


# In[10]:


my_day.isoweekday()


# 9. When will you be (or when were you) 10,000 days old?

# In[11]:


from datetime import timedelta
ten_thousand = my_day + timedelta(days=10000)
ten_thousand


# In[ ]:




