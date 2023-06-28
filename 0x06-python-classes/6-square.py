#!/usr/bin/python3
"""new class"""


class Square:
    """a class to define a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initialize attributes
        size: private inst attribute
        position: private inst attribute
        """
        self.size = size
        self.position = position

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
        if ssize < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = ssize

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pposition):
        """a method to change position private attribute
        args:
            pposition (int): size
        """
        if (type(pposition) != tuple or len(pposition) != 2
                or type(pposition[0]) is not int or
                type(pposition[1]) is not int or
                pposition[0] < 0 or pposition[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = pposition

    def area(self):
        """a method to return the area"""
        return self.__size ** 2

    def my_print(self):
        """a method to print to stdout"""
        import sys
        if self.size == 0:
            print("", file=sys.stdout)
        else:
            print("\n" * self.position[1], file=sys.stdout, end="")
            for i in range(self.size):
                print(" " * self.position[0], file=sys.stdout, end="")
                for j in range(self.size):
                    print("#", file=sys.stdout, end="")
                print("", file=sys.stdout)
