#!/usr/bin/python3
"""
this is 'test_square' module

unittest for 'square' module
"""
import inspect
import unittest
import io
from io import StringIO
from contextlib import redirect_stdout
from models.square import Square
from models.base import Base
import pep8


class TestSquare(unittest.TestCase):
    """
    a class to test Square class and its methods
    """

    @classmethod
    def setUp(self):
        Base._Base__nb_objects = 0

    @classmethod
    def get_methods(cls):
        """
        a method to get the methods in the class
        :return: nth
        """
        cls.methods = inspect.getmembers(Square, inspect.isfunction)

    def test_class_doctest(self):
        """
        test to check doctest of class
        :return: nth
        """
        self.assertTrue(len(Square.__doc__) > 1)

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
        test for pep8 of 'square' module
        :return: nth
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors")

    def test_task10(self):
        """
        test for task 10
        :return: nth
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        with io.StringIO() as buff, redirect_stdout(buff):
            s1.display()
            actual_op = buff.getvalue()
            expected_op = "#####\n#####\n#####\n#####\n#####\n"
            self.assertEqual(actual_op, expected_op)
        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        with io.StringIO() as buff, redirect_stdout(buff):
            s2.display()
            actual_op = buff.getvalue()
            expected_op = "  ##\n  ##\n"
            self.assertEqual(actual_op, expected_op)
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        with io.StringIO() as buff, redirect_stdout(buff):
            s3.display()
            actual_op = buff.getvalue()
            expected_op = "\n\n\n ###\n ###\n ###\n"
            self.assertEqual(actual_op, expected_op)

    def test_task11(self):
        """
        test for task 11
        :return: nth
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_task12(self):
        """
        test for task 12
        :return: nth
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_task14(self):
        """
        test for task 14
        :return: nth
        """
        s1 = Square(10, 2, 1)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary,
                         {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        self.assertEqual(str(s2), "[Square] (2) 1/0 - 1")
        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
