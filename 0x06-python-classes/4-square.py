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
    def size(self, ssize):
        """a method to change size private attribute
        args:
            ssize (int): size
        """
        if type(ssize) is not int:
            raise TypeError("size must be an integer")
        elif ssize < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = ssize

    def area(self):
        """a method to return the area"""
        return self.__size ** 2
