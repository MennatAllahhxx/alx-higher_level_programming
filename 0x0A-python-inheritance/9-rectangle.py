#!/usr/bin/python3
"""
this is '9-rectangle' module

this module contains 1 class: Rectangle

importing BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

    def area(self):
        """
        method to calculate area
        :return: area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        method to return certain string
        :return:
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
