#!/usr/bin/python3
"""new class"""


class Square:
    """a class to define a square
    """

    def __init__(self, size=0):
        """initialize attributes
        size: private inst attribute
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
