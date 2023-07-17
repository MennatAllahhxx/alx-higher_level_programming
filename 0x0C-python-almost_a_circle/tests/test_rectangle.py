#!/usr/bin/python3
"""
this is 'test_rectangle' module

unittest for 'rectangle' module
"""
import inspect
import io
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base
import pep8


class TestRectangle(unittest.TestCase):
    """
    a class to test Rectangle class and its methods
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
        cls.methods = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_class_doctest(self):
        """
        test to check doctest of class
        :return: nth
        """
        self.assertTrue(len(Rectangle.__doc__) > 1)

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
        test for pep8 of 'rectangle' module
        :return: nth
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files('models/rectangle')
        self.assertEqual(result.total_errors, 15, "PEP8 errors")

    def test_task2(self):
        """
        test for task 2
        :return: nth
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_task3(self):
        """
        test for task 3
        :return: nth
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_task4(self):
        """
        test for task 4
        :return: nth
        """
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_task5(self):
        """
        test for task 5
        :return: nth
        """
        r1 = Rectangle(4, 6)
        with io.StringIO() as buff, redirect_stdout(buff):
            r1.display()
            actual_op = buff.getvalue()
            expected_op = "####\n####\n####\n####\n####\n####\n"
            self.assertEqual(actual_op, expected_op)
        r1 = Rectangle(2, 2)
        with io.StringIO() as buff, redirect_stdout(buff):
            r1.display()
            actual_op = buff.getvalue()
            expected_op = "##\n##\n"
            self.assertEqual(actual_op, expected_op)

    def test_task6(self):
        """
        test for task 6
        :return: nth
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_task7(self):
        """
        test for task 7
        :return: nth
        """
        r1 = Rectangle(2, 3, 2, 2)
        with io.StringIO() as buff, redirect_stdout(buff):
            r1.display()
            actual_op = buff.getvalue()
            expected_op = "\n\n  ##\n  ##\n  ##\n"
            self.assertEqual(actual_op, expected_op)
        r1 = Rectangle(3, 2, 1, 0)
        with io.StringIO() as buff, redirect_stdout(buff):
            r1.display()
            actual_op = buff.getvalue()
            expected_op = " ###\n ###\n"
            self.assertEqual(actual_op, expected_op)

    def test_task8(self):
        """
        test for task 8
        :return: nth
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_task9(self):
        """
        test for task 9
        :return: nth
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_task13(self):
        """
        test for task 13
        :return: nth
        """
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary,
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
