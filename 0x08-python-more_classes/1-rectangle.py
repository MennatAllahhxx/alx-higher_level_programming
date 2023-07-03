#!/usr/bin/python3
"""
New class
"""


class Rectangle:
    """
    a class to define a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        initialize parameters of a rectangle
        :param width: width of rect (int)
        :param height: height of rect (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """
        a method to change private width attribute
        :param self: Rectangle (class)
        :param width: width (int)
        :return: changed width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """
        a method to change private height attribute
        :param self: Rectangle (class)
        :param height: height (int)
        :return: changed height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
