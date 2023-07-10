#!/usr/bin/python3
"""
this is '2-is_same_class' module

this module contains 1 function: is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    a fun to check if object is class of a certain class
    :param obj: object to be checked
    :param a_class: the given class
    :return: True if yes
    """
    if type(obj) == a_class:
        return True
    return False
