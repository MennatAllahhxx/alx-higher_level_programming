#!/usr/bin/python3
"""
this is '8-rectangle' module

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
