#!/usr/bin/python3
"""
this is '3-inherits_from' module

this module contains 1 function: inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    a fun to check if object is inherited from of a certain class
    :param obj: object to be checked
    :param a_class: the given class
    :return: True if yes
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
