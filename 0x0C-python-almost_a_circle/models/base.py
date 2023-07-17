#!/usr/bin/python3
"""
this is 'base' module

this module contains 1 class: Base

this class contains 5 methods: to_json_string, from_json_string, create,
                                save_to_file, load_from_file
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method to convert dict to json
        :return: json-string
        """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        method to convert json to dict
        :return: dictionary
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        a method to write json repr to file
        :param list_objs: list of json obj
        :return: file
        """
        file = cls.__name__ + ".json"
        my_list = []
        with open(file, 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                for i in list_objs:
                    my_list.append(cls.to_dictionary(i))
                file.write(cls.to_json_string(my_list))

    @classmethod
    def create(cls, **dictionary):
        """
        method to create obj ig
        :param dictionary: dict to create obj from
        :return: instance
        """
        if "Rectangle" == cls.__name__:
            dummy = cls(3, 3)
        if "Square" == cls.__name__:
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load lists from file
        :return: list of instances
        """
        file = cls.__name__ + '.json'
        my_list = []
        try:
            with open(file, 'r', encoding="utf-8") as file:
                inst = cls.from_json_string(file.read())
                for i in inst:
                    my_list.append(cls.create(**i))
        except:
            pass
        return my_list
