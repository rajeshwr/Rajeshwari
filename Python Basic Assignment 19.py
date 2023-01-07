#!/usr/bin/env python
# coding: utf-8

# 1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?

# In[1]:


class Thing:
    pass
print(Thing)


# In[2]:


example = Thing()
print(example)


# 2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.

# In[3]:


class Thing2:
    letters = 'abc'
print(Thing2.letters)


# 3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?

# In[4]:


class Thing3:
    def __init__(self):
        self.letters = 'xyz'


# #The variable letters belongs to any objects made from Thing3, not the Thing3 class itself:

# In[5]:


print(Thing3.letters)


# In[6]:


something = Thing3()
print(something.letters)


# 4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1

# In[7]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
hydrogen = Element('Hydrogen', 'H', 1)


# 5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.

# In[12]:


#Starting with the dictionary:
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}


# In[13]:


#Creating object called hydrogen from class Element using el_dict
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])


# In[8]:


hydrogen.name


# In[14]:


#We can also initialize the object directly from the dictionary, because its key names match the arguments to "init"
hydrogen = Element(**el_dict)
hydrogen.name


# 6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.

# In[15]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))
hydrogen = Element(**el_dict)
hydrogen.dump()


# 7. Call print(hydrogen). In the definition of Element, change the name of method dump to str, create a new hydrogen object, and call print(hydrogen) again.

# In[16]:


print(hydrogen)


# In[17]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))

hydrogen = Element(**el_dict)
print(hydrogen)


# 8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.

# In[18]:


class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property    
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
hydrogen = Element('Hydrogen', 'H', 1)


# In[19]:


hydrogen.name


# In[20]:


hydrogen.symbol


# In[21]:


hydrogen.number


# 9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.

# In[22]:


class Bear:
    def eats(self):
        return 'berries'
    
class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'
    
b = Bear()
r = Rabbit()
o = Octothorpe()


# In[23]:


print(b.eats())


# In[24]:


print(r.eats())


# In[25]:


print(o.eats())


# 10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.

# In[26]:


class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'
    
class SmartPhone:
    def does(self):
        return 'ring'
    
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
        
    def does(self):
        return '''I have many attachments:
        My laser, to %s.
        My claw, to %s.
        My smartphone, to %s.''' % (self.laser.does(),self.claw.does(),self.smartphone.does() )


# In[27]:


robbie = Robot()


# In[28]:


print( robbie.does())


# In[ ]:




