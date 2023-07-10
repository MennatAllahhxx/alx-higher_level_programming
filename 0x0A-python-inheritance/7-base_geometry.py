#!/usr/bin/python3
"""
this is '6-base_geometry' module

this module contains 1 class: BaseGeometry

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
            raise ValueError(f"{name}  must be greater than 0")
