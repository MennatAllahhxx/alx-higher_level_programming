#!/usr/bin/python3
"""
this is '7-add_item' module
"""


def class_to_json(obj):
    """
    a fun to return dict description
    :param obj: object
    :return: dict description
    """
    return obj.__dict__
