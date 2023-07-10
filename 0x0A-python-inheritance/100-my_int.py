#!/usr/bin/python3
"""
this is '100-my_int' module

this module contains 1 class: MyInt
"""

class MyInt(int):
    """
    this is a class to convert stuff
    """
    def __eq__(self, other):
        """
        a method to convert equal
        :param other: parameter
        :return: the opposite
        """
        return not super().__eq__(other)
    
    def __ne__(self, other):
        """
        a method to convert not equal
        :param other: parameter
        :return: the opposite
        """
        return super().__eq__(other)
