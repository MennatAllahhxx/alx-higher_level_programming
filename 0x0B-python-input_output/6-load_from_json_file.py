#!/usr/bin/python3
"""
this is '6-load_from_json_file' module

this module contains 1 function: load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    a fun to create obj from json-file
    :param filename: file to converted
    :return: object
    """
    with open(filename, encoding="utf-8") as file:
        json.loads(file.read())
