#!/usr/bin/env python
# coding: utf-8

# 1. What advantages do Excel spreadsheets have over CSV spreadsheets?

# CSV is generally faster and less complicated when compared to Excel. Text editors cannot edit files saved in Excel format, and also, Excel file can be password protected. Files saved in CSV format can be edited by text editors, and also CSV file cannot be password protected.

# 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

# call open() and pass it 'w' to open a file in write mode. This will create the object you can then pass to csv. writer() to create a Writer object
# The csv module's reader and writer objects read and write sequences. Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes

# 3. What modes do File objects for reader and writer objects need to be opened in?

# In order to open a file for reading or writing purposes, we must use the built-in open() function.
# ‘r’	Open a file for reading. (default)
# ‘w’	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.

# 4. What method takes a list argument and writes it to a CSV file?

# The csv.writer writerow method takes an iterable as an argument. The result set has to be a list (rows) of lists (columns).

# 5. What do the keyword arguments delimiter and line terminator do?

# The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline.

# 6. What function takes a string of JSON data and returns a Python data structure?

# loads() method return Python data structure of JSON string or data

# 7. What function takes a Python data structure and returns a string of JSON data?

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method
