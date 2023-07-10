#!/usr/bin/python3
"""
this is '10-square' module

this module contains 1 class: Square

importing Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    this is a class for square
    """

    def __init__(self, size):
        """
        initialize rectangle
        :param size: size of square
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        method to calculate area
        :return: area
        """
        return self.__size ** 2
