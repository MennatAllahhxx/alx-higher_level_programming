#!/usr/bin/python3
"""
this is '7-add_item' module
"""
import json


def class_to_json(obj):
    """
    a fun to return dict description
    :param obj: object
    :return: dict description
    """
    return json.dumps(obj.__dict__)
