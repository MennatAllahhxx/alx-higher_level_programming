#!/usr/bin/python3
"""
this is '1-student' module

this module contains 1 class: Student

Student contains 2 methods: to_json, reload_from_json
"""


class Student:
    """
    a new class for student
    """

    def __init__(self, first_name, last_name, age):
        """
        initializing values
        :param first_name: student's first name
        :param last_name: student's last name
        :param age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        a method to return dict description
        :param attrs: list of attributes
        :return: dict description
        """
        if attrs is None and not isinstance(attrs, list):
            return self.__dict__

        my_list = {}
        for attr in attrs:
            if hasattr(self, attr):
                my_list[attr] = getattr(self, attr)
        return my_list

    def reload_from_json(self, json):
        """
        a method to replace attr
        :param json:a dict
        :return: nth probably
        """
        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
