#!/usr/bin/python3
"""
this is 'test_base' module

unittest for 'base' module
"""
import inspect
import unittest
from json import JSONDecodeError
from models.base import Base
from models.rectangle import Rectangle
import pep8


class TestBase(unittest.TestCase):
    """
    a class to test Base class and its methods
    """

    @classmethod
    def setUp(self):
        """
        set up class everytime
        :return: nth
        """
        Base._Base__nb_objects = 0

    @classmethod
    def get_methods(cls):
        """
        a method to get the methods in the class
        :return: nth
        """
        cls.methods = inspect.getmembers(Base, inspect.isfunction)

    def test_class_doctest(self):
        """
        test to check doctest of class
        :return: nth
        """
        self.assertTrue(len(Base.__doc__) > 1)

    def test_methods_doctest(self):
        """
        test to check doctest of methods
        :return: nth
        """
        self.get_methods()
        for method in self.methods:
            self.assertTrue(len(method[1].__doc__) > 1)

    def test_class_pep8(self):
        """
        test for pep8 of 'base' module
        :return: nth
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/Base.py'])
        self.assertEqual(result.total_errors, 1, "PEP8 errors")

    def test_task1(self):
        """
        test for task 1
        :return: nth
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_task1_extra(self):
        """
        test for task 1 extra
        :return: nth
        """
        with self.assertRaises(TypeError):
            b1 = Base(7, 5)

    def test_task15(self):
        """
        test for task 15
        :return: nth
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(dictionary),
                         "{'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}")
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(str(json_dictionary),
                         '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]')
        self.assertEqual(type(json_dictionary), str)

    def test_task15_extra(self):
        """
        test for task 15 extra
        :return: nth
        """
        json_dictionary = Base.to_json_string([])
        self.assertEqual(str(json_dictionary), '[]')
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(type(json_dictionary), str)
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 1)

    def test_task16(self):
        """
        test for task 16
        :return: nth
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(str(file.read()),
                             '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, \
{"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]')

    def test_task16_extra(self):
        """
        test for task 16 extra
        :return: nth
        """
        with self.assertRaises(TypeError):
            Base.save_to_file()
        with self.assertRaises(TypeError):
            Base.save_to_file(1, 1)

    def test_task17(self):
        """
        test for task 17
        :return: nth
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(str(f"[{type(list_input)}] {list_input}"),
                         "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, \
{'id': 7, 'width': 1, 'height': 7}]")
        self.assertEqual(str(f"[{type(json_list_input)}] {json_list_input}"),
                         "[<class 'str'>] [{\"id\": 89, \"width\": 10, \"height\": 4}, \
{\"id\": 7, \"width\": 1, \"height\": 7}]")
        self.assertEqual(str(f"[{type(list_output)}] {list_output}"),
                         "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, \
{'id': 7, 'width': 1, 'height': 7}]")

    def test_task17_extra(self):
        """
        test for task 17 extra
        :return: nth
        """
        json_dictionary = Base.from_json_string("[]")
        self.assertEqual(json_dictionary, [])
        json_dictionary = Base.from_json_string(None)
        self.assertEqual(json_dictionary, [])
        with self.assertRaises(TypeError):
            Base.from_json_string(1, 1)

    def test_task18(self):
        """
        test for task 18
        :return: nth
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
