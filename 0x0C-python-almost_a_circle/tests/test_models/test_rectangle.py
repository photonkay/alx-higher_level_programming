#!/usr/bin/python3

"""Unittest module for models/rectangle.py"""


import unittest
import mock
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test functions for Rectangle class"""

    def test_attributes(self):
        """Test the getter and setter for the attributes"""
        rectangle = Rectangle(4, 5, 1, 2, 10)

        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 10)

        rectangle.width = 7
        rectangle.height = 8
        rectangle.x = 3
        rectangle.y = 4

        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_width_height_validation(self):
        """Tests that an error is raised for invalid width or height"""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-1, 5)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(2, 0)

        with self.assertRaises(TypeError):
            rectangle = Rectangle("a", 3)

        with self.assertRaises(TypeError):
            rectangle = Rectangle(4, "b")

    def test_x_y_validation(self):
        """Tests for invalid x or y inputs"""
        rectangle = Rectangle(4, 5)

        with self.assertRaises(ValueError):
            rectangle.x = -1

        with self.assertRaises(ValueError):
            rectangle.y = -2

        with self.assertRaises(TypeError):
            rectangle.x = "char"

        with self.assertRaises(TypeError):
            rectangle.y = "string"

    def test_area(self):
        rectangle = Rectangle(3, 2)

        self.assertEqual(rectangle.area(), 6)

    def test_display(self):
        """Tests the display method"""
        rectangle = Rectangle(2, 2, 1, 0)
        expected = " ##\n ##\n"
        with mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_str(self):
        """Tests the specified output string representation"""
        rectangle = Rectangle(2, 3, 1, 2, 10)
        expected_output = "[Rectangle] (10) 1/2 - 2/3\n"
        with mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print(rectangle)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def setUp(self):
        """Set up a clean instance of Rectangle for each test."""
        self.rectangle = Rectangle(2, 3, id=1)

    def test_update(self):
        """Test the update method."""
        rectangle = self.rectangle
        self.assertEqual(str(rectangle), "[Rectangle] (1) 0/0 - 2/3")

        rectangle.update(10, 5, 7, 1, 2)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 1/2 - 5/7")

        rectangle.update(id=1, width=2, height=3, x=0, y=0)

        rectangle.update(id=5, width=3, height=7, x=1, y=6)
        self.assertEqual(str(rectangle), "[Rectangle] (5) 1/6 - 3/7")

        rectangle.update(id=1, width=2, height=3, x=0, y=0)

        rectangle.update(id=10, width=5, height=7, x=1, y=2)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 1/2 - 5/7")

        rectangle.update(id=1, width=2, height=3, x=0, y=0)

        rectangle.update()
        self.assertEqual(str(rectangle), "[Rectangle] (1) 0/0 - 2/3")

        rectangle.update(id=1, width=2, height=3, x=0, y=0)

        rectangle.update(id=15, width=4, height=6, x=2, y=3)
        self.assertEqual(str(rectangle), "[Rectangle] (15) 2/3 - 4/6")

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        rectangle = Rectangle(4, 5, 1, 2, 10)
        dictionary_representation = {
            'id': 10,
            'width': 4,
            'height': 5,
            'x': 1,
            'y': 2
        }
        self.assertEqual(rectangle.to_dictionary(), dictionary_representation)


if __name__ == '__main__':
    unittest.main()
