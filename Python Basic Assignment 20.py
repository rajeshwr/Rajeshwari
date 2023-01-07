#!/usr/bin/env python
# coding: utf-8

# 1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.

# In[1]:


test1 = 'This is a test of the emergency text system'
len(test1)


# In[2]:


with open('test.txt', 'wt') as outfile:
    outfile.write(test1)


# In[3]:


outfile.close()


# 2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?

# In[4]:


with open('test.txt', 'rt') as infile:
    test2 = infile.read()
len(test2)


# In[5]:


test1 == test2


# 3. Create a CSV file called books.csv by using these lines:
# 
# title,author,year
# 
# The Weirdstone of Brisingamen,Alan Garner,1960
# 
# Perdido Street Station,China Miéville,2000
# 
# Thud!,Terry Pratchett,2005
# 
# The Spellman Files,Lisa Lutz,2007
# 
# Small Gods,Terry Pratchett,1992

# In[6]:


text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books.csv', 'wt') as outfile:
    outfile.write(text)


# 4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).

# In[7]:


import sqlite3
db = sqlite3.connect('books.db')
curs = db.cursor()
curs.execute('''create table book (title text, author text, year int)''')


# In[8]:


db.commit()


# 5. Read books.csv and insert its data into the book table.

# In[9]:


import csv
import sqlite3
ins_str = 'insert into book values(?, ?, ?)'
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))


# In[10]:


db.commit()


# 6. Select and print the title column from the book table in alphabetical order.  

# In[11]:


sql = 'select title from book order by title asc'
for row in db.execute(sql):
    print(row)


# In[12]:


#to print the title value without that tuple stuff (parentheses and comma):
for row in db.execute(sql):
    print(row[0])


# 7. From the book table, select and print all columns in the order of publication.

# In[13]:


for row in db.execute('select * from book order by year'):
    print(row)


# In[14]:


#To print all the fields in each row, just separate with a comma and space:

for row in db.execute('select * from book order by year'):
    print(*row, sep=', ')


# 8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.

# In[16]:


import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'select title from book order by title asc'
rows = conn.execute(sql)
for row in rows:
    print(row)


# In[21]:


pip install redis


# 9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.

# In[ ]:


import redis
conn = redis.Redis()
conn.delete('test')


# In[ ]:


conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})


# In[ ]:


conn.hgetall('test')


# 10. Increment the count field of test and print it.

# In[ ]:


conn.hincrby('test', 'count', 3)


# In[ ]:


conn.hget('test', 'count')

