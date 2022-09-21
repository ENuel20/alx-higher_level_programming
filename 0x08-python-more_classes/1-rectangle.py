#!/usr/bin/python3
""" define a rectanle class"""

class Rectangle:
    """ definition of rectangle"""

    def __init__(self,width=0,height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The width of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the current width of the rectamgle."""
        return (self.__width)

    @width.setter
    def width(self,value):
        """ set the width of the rectangle """
        if not(isinstance(value,int)):
            return TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self,value):
        """ set the height of the rectangle """
        if not(isinstance(value,int)):
            return TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
