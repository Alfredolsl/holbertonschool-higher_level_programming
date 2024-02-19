#!/usr/bin/python3
"""Defines a unittest for Class Rectangle."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_Instantiation(unittest.TestCase):
    """Unittests for testing Rectangle instantiation."""

    def test_rectangle_is_base(self):
        rect1 = Rectangle(5, 6)
        self.assertIsInstance(rect1, Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_three_arg(self):
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(4, 5, 6)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_four_arg(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_five_arg(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        self.assertEqual(98, rect1.id)

    def test_greater_than_5_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 98, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4, 98).__width

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4, 98).__height

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4, 98).__x

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4, 98).__y

    def test_width_getter(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        self.assertEqual(1, rect1.width)

    def test_height_getter(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        self.assertEqual(2, rect1.height)

    def test_x_getter(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        self.assertEqual(3, rect1.x)

    def test_y_getter(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        self.assertEqual(4, rect1.y)

    def test_width_setter(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        rect1.width = 10
        self.assertEqual(10, rect1.width)

    def test_height_setter(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        rect1.height = 10
        self.assertEqual(10, rect1.height)

    def test_x_setter(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        rect1.x = 10
        self.assertEqual(10, rect1.x)

    def test_y_setter(self):
        rect1 = Rectangle(1, 2, 3, 4, 98)
        rect1.y = 10
        self.assertEqual(10, rect1.y)


class Test_Rectangle_Width(unittest.TestCase):
    """
    Unittests for testing Rectangle width attribute
    when initialized.
    """

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hallo", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.14, 2)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)



















