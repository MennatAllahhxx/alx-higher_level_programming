#!/usr/bin/python3
"""
this is '8-rectangle' module

this module contains 2 classes: BaseGeometry, Rectangle

BaseGeometry contains 2 methods: area(self),
integer_validator(self, name, value)
"""


class BaseGeometry:
    """
    this is a class to do some geometry
    """

    def area(self):
        """
        a method to calculate the area
        :return: area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        a method to validate integer
        :param name: name of object
        :param value: its value
        :return: nth probably
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    this is a class for rectangle
    """

    def __init__(self, width, height):
        """
        initialize rectangle
        :param width: width of rectangle
        :param height: height of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
