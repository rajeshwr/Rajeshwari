#!/usr/bin/env python
# coding: utf-8

# 1. Create a list called years_list, starting with the year of your birth, and each year thereafter until
# the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list =
# [1980, 1981, 1982, 1983, 1984, 1985].

# In[2]:


years_list = [1983, 1984, 1985,1986,1987,1988]


# 2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.

# In[3]:


years_list[2]


# 3. In the years list, which year were you the oldest?

# In[5]:


years_list[5] or years_list[-1]


# 4. Make a list called things with these three strings as elements: "mozzarella","cinderella","salmonella"
# 

# In[8]:


things = ["mozzarella","cinderella","salmonella"]
things


# 5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?

# In[9]:


#This capitalizes the word, but doesn’t change it in the list:
things_cap = things.copy()
things_cap[1].capitalize()


# In[10]:


things_cap


# 6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."

# In[11]:


surprise = ['Groucho', 'Chico', 'Harpo']
surprise


# 7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.

# In[12]:


surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1].capitalize()


# 8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.

# In[13]:


e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
e2f


# 9. Write the French word for walrus in your three-word dictionary e2f.

# In[14]:


e2f['walrus']


# 10. Make a French-to-English dictionary called f2e from e2f. Use the items method.

# In[15]:


f2e = {}
for english, french in e2f.items():
 f2e[french] = english
f2e


# 11. Print the English version of the French word chien using f2e.

# In[16]:


f2e['chien']


# 12. Make and print a set of English words from the keys in e2f.

# In[17]:


set(e2f.keys())


# 13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

# In[18]:


life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],'octopi': {},'emus': {}},'plants': {},'other': {}}
life


# 14. Print the top-level keys of life.

# In[21]:


print(life.keys())


# 15. Print the keys for life['animals'].

# In[20]:


print(life['animals'].keys())


# 16. Print the values for life['animals']['cats']

# In[22]:


print(life['animals']['cats'])


# In[ ]:




