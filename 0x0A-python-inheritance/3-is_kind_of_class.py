#!/usr/bin/python3
"""
this is '3-is_kind_of_class' module

this module contains 1 function: is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    a fun to check if object is class of a certain class
    :param obj: object to be checked
    :param a_class: the given class
    :return: True if yes
    """
    if isinstance(obj, a_class):
        return True
    return False
