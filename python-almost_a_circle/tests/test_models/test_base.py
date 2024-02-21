#!/usr/bin/python3
"""Defines unit tests for base.py ."""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests to test instantiation of Base Class."""

    def test_no_args(self):
        """Test if __nb_objects assigns id correctly.
        if no id is specified, it defaults to None."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        b1 = Base(98)
        self.assertEqual(98, b1.id)

    def test_None_as_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_str_id(self):
        b1 = Base("Best")
        self.assertEqual("Best", b1.id)

    def test_float_id(self):
        b1 = Base(9.8)
        self.assertEqual(9.8, b1.id)

    def test_tuple_id(self):
        b1 = Base((1, 2))
        self.assertEqual((1, 2), b1.id)

    def test_list_id(self):
        b1 = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b1.id)

    def test_dict_id(self):
        b1 = Base({"a": 1, "b": 2})
        self.assertEqual({"a": 1, "b": 2}, b1.id)

    def test_set_id(self):
        b1 = Base({1, 2, 3})
        self.assertEqual({1, 2, 3}, b1.id) 

    def test_frozenset_id(self):
        b1 = Base(frozenset({1, 2, 3}))
        self.assertEqual(frozenset({1, 2, 3}), b1.id)

    def test_range_id(self):
        b1 = Base(range(3))
        self.assertEqual(range(3), b1.id) 
    
    def test_bool_id(self):
        b1 = Base(True)
        self.assertEqual(True, b1.id)

    def test_inf_id(self):
        b1 = Base(float('inf'))
        self.assertEqual(float('inf'), b1.id)

    def test_NaN_id(self):
        b1 = Base(float('nan'))
        self.assertNotEqual(float('nan'), b1.id) 

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(98)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_nb_instance_private(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            print(b1.__nb_instances)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of
    class Base."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) != 0)


    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) != 0)


    def test_save_to_file_two_squares(self):
        s1 = Rectangle(10, 7, 2, 8, 5)
        s2 = Rectangle(1, 2, 3, 4, 5)
        Square.save_to_file([s1, s2])
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_file_to_base(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_file_and_overwrite(self):
        s = Square(10, 7, 2, 7)
        Square.save_to_file([s])
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_None_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([1], 2)

class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method in
    class Base."""


    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_to_file_one_square(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_to_file_two_squares(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_to_file_to_base(self):
        s = Square(1, 2, 3, 4)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) != 0)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
