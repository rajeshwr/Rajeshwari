#!/usr/bin/env python
# coding: utf-8

# 1. What does RGBA stand for?

# RGBA(Red-Green-Blue-Alpha)

# 2. From the Pillow module, how do you get the RGBA value of any images?

# Pillow offers the ImageColor.getcolor() function so we don’t have to memorize RGBA values for the colors you want to use. This function takes a color name string as its first argument, and the string 'RGBA' as its second argument, and it returns an RGBA tuple.
# White (255, 255, 255, 255), Red (255, 0, 0, 255), Green (0, 128, 0, 255), Blue (0, 0, 255, 255)

# 4. Use your image and load in notebook then, How can you find out the width and height of an Image object?

# The first approach is by using the PIL(Pillow) library and the second approach is by using the Open-CV library
# PIL.Image.open() is used to open the image and then .width and .height
# An alternate way to get height and width is using .size property

# In[ ]:


pip install opencv-python
# import required module
import cv2
  
# get image
filepath = "raji.jpg"
image = cv2.imread(filepath)
#print(image.shape)
  
# get width and height
height, width = image.shape[:2]
  
# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)
********************************************************************************************************************************
pip install pillow
# import required module
from PIL import Image
  
# get image
filepath = "raji.png"
img = Image.open(filepath)
  
# get width and height
width,height = img.size
  
# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)
********************************************************************************************************************************
# import required module
from PIL import Image
  
# get image
filepath = "raji.png"
img = Image.open(filepath)
  
# get width and height
width = img.width
height = img.height
  
# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)


# 5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?

# The Python Imaging Library (PIL) provides general image handling and lots of useful basic image operations like resizing, cropping, rotating, color conversion. And with help of Numpy array we can manipulate the image

# 6. After making changes to an Image object, how could you save it as an image file?

# To save images, we can use the PIL. save() function. This function is used to export an image to an external file. But to use this function, first, we should have an object which contains an image.

# 7. What module contains Pillow’s shape-drawing code?

# ImageDraw provides a variety of methods to, as its name suggests, draw on images. With the help of this module, we can draw lines, circles, rectangles and, even write and format text on an image.

# 8. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?

# The ImageDraw module provides simple 2D graphics for Image objects. You can use this module to create new images, annotate or retouch existing images, and to generate graphics on the fly for web use.
