#!/usr/bin/python3
"""
this is '9-student' module

this module contains 1 class: Student

Student contains 1 method: to_json
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

    def to_json(self):
        """
        a fun to return dict description
        :return: dict description
        """
        return self.__dict__
