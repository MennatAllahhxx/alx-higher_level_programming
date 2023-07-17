#!/usr/bin/python3
"""
this is 'rectangle' module

this module contains 1 class: Rectangle

Base class is imported
"""
from models.base import Base


class Rectangle(Base):
    """
    a new class for rectangles
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize object
        :param width: width of rect
        :param height: height or rect
        :param x: x-axis position
        :param y: y-axis position
        :param id: id of the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """
        a method to change private width attribute
        :param width: given width
        :return: changed width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """
        a method to change private height attribute
        :param height: given height
        :return: changed height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """
        a method to change private x attribute
        :param x: given x
        :return: changed x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """
        a method to change private y attribute
        :param y: given y
        :return: changed y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        a method to calculate the area
        :return: area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        to display the rectangle
        :return: prints the rectangle
        """
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        a method to repr string
        :return: representation
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
