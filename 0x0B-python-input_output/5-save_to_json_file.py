#!/usr/bin/python3
"""
this is '5-save_to_json_file' module

this module contains 1 function: save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a fun to write obj to text file
    :param my_obj: object to be written
    :param filename: file to be written to
    :return: nth probably
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
