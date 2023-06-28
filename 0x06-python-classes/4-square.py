#!/usr/bin/python3
"""new class"""


class Square:
    """a class to define a square
    """

    def __init__(self, size=0):
        """initialize attributes
        size: private inst attribute
        """
        self.size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, size):
            """a method to change size private attribute
            args:
                size (int): size
            """
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        """a method to return the area"""
        return self.__size ** 2
