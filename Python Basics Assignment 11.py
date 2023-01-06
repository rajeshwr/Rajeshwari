#!/usr/bin/env python
# coding: utf-8

# ##Python Basics Assignment 11##

# 1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.

# In[ ]:


assert spam <= 0, 'Your spam is a negative integer!'


# 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

# In[ ]:


eggs = 'hello'
bacon = 'good bye'

# Raise an AssertError if they are not different.
assert eggs.lower() != bacon.lower(), 'eggs/bacon should not be the same!'


# 3. Create an assert statement that throws an AssertionError every time.

# In[ ]:


assert True, 'Always triggers an AssertionError.'


# 4. What are the two lines that must be present in your software in order to call logging.debug()?

# In[12]:


import logging 
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

# In[ ]:


import logging
logging.basicConfig(
    filename='programLog.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')


# 6. What are the five levels of logging?

# In[ ]:


DEBUG, INFO, WARNING, ERROR, and CRITICAL
# logging.debug() - variable's state and small details
# logging.info() - general events, confirm a program is working
# logging.warning() - potiental problem to work on in the future
# logging.error() - record an error that caused program to fail to do something
# logging.critical() - fatal error that has caused


# 7. What line of code would you add to your software to disable all logging messages?

# In[ ]:


logging.disable(logging.DEBUG)
logging.disable(logging.CRITICAL)


# 8. Why is using logging messages better than using print() to display the same message?

# You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.

# 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

# Step - one line execution at a time
# Over - excecute the next line of code, but if it is a program, it will
# complete the entire function call.
# execute the lines of code unti it returns from the current function.
# (out is useful when you stepped into a function call).

# 10. After you click Continue, when will the debugger stop ?

# Continue execution, only stop when a breakpoint is encountered. Set the next line that will be executed.

# 11. What is the concept of a breakpoint?

# Breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line
