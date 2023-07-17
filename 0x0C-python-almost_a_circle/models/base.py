#!/usr/bin/python3
"""
this is 'base' module

this module contains 1 class: Base
"""


class Base:
    """
    this is the base class of all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing the class
        :param id: id to be checked
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
