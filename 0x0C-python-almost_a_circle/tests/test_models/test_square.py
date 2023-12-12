#!/usr/bin/python3

"""Unittest module for models.square"""

import unittest
import io
import mock
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""
    def test_attributes(self):
        """Test the attributes of the Square class"""
        square = Square(4, 2, 3, 1)

        self.assertEqual(square.size, 4)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

        square.size = 5
        square.x = 1
        square.y = 2

        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_size_x_y_validation(self):
        """Test that an error is raised for invalid inputs"""
        square = Square(4)

        with self.assertRaises(ValueError):
            square = Square(-1)

        with self.assertRaises(ValueError):
            square.x = -1

        with self.assertRaises(ValueError):
            square.y = -2

        with self.assertRaises(TypeError):
            square = Square("a")

        with self.assertRaises(TypeError):
            square.x = "char"

        with self.assertRaises(TypeError):
            square.y = "string"

    def test_area(self):
        """Test the area method"""
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_str(self):
        """Test the specified output string representation"""
        square = Square(4, 1, 2, 10)
        expected = "[Square] (10) 1/2 - 4\n"
        with mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print(square)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_update(self):
        """Test the update method."""
        square = Square(4, 2, 3, 1)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

        square.update(10, 5, 1, 2)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

        square.update(id=5, size=3, x=1, y=6)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 6)
        self.assertEqual(square.id, 5)

        square.update(id=15, size=4, x=2, y=3)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 15)

        square.update()
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 15)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square"""
        square = Square(4, 5, 1, 2)
        dictionary_representation = {
            'id': 2,
            'size': 4,
            'x': 5,
            'y': 1
        }


if __name__ == '__main__':
    unittest.main()
