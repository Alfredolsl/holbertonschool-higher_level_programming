#!/usr/bin/python3
"""Defines unit tests for base.py ."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


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
