#!/usr/bin/env python
# coding: utf-8

# 1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.

# In[ ]:


import zoo
zoo.hours()


# 2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[ ]:


import zoo as menagerie
menagerie.hours()


# 3. Using the interpreter, explicitly import and call the hours() function from zoo.

# In[ ]:


from zoo import hours
hours()


# 4. Import the hours() function as info and call it.

# In[ ]:


from zoo import hours as info
info()


# 5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

# In[3]:


plain_dict = {'a': 1, 'b': 2, 'c': 3}
plain_dict


# 6. Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

# In[4]:


from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy


# 7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

# In[5]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']


# In[ ]:




