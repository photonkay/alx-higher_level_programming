#!/usr/bin/python3

"""unittest module for models/base.py"""


import unittest
import json
import csv
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test functions for Base class"""

    def test_id_assignment(self):
        """Tests if id is assigned correctly"""
        obj = Base(50)
        self.assertEqual(obj.id, 50)

    def test_id_increment(self):
        """Tests that id is incremented correctly"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 3)
        self.assertEqual(obj2.id, 4)

    def test_to_dictionary(self):
        """Tests the base static method to_dictionary()"""
        list_of_dicts = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'},
            {'id': 3, 'name': 'Charlie'}
        ]
        expected_json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]'
        self.assertEqual(Base.to_json_string(list_of_dicts), expected_json_string)

        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), "[]")

        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file(self):
        """Test the save_to_file method."""
        rectangles = [Rectangle(4, 5, 1, 2, 10), Rectangle(3, 2, 0, 0, 5)]

        Rectangle.save_to_file(rectangles)

        with open('Rectangle.json', 'r') as file:
            file_content = json.load(file)

        expected_json_string = '[{"id": 10, "width": 4, "height": 5, "x": 1, "y": 2},' \
                               ' {"id": 5, "width": 3, "height": 2, "x": 0, "y": 0}]'
        expected_objects = json.loads(expected_json_string)

        self.assertEqual(file_content, expected_objects)

    def test_from_json_string(self):
        """Test the from_json_string method."""
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        expected_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

        empty_json_string = '[]'
        self.assertEqual(Base.from_json_string(empty_json_string), [])

        self.assertEqual(Base.from_json_string(None), [])

    def test_create_rectangle(self):
        """Test create method for Rectangle."""
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)

        self.assertIsInstance(rectangle_instance, Rectangle)
        self.assertEqual(rectangle_instance.id, 1)
        self.assertEqual(rectangle_instance.width, 5)
        self.assertEqual(rectangle_instance.height, 10)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)

    def test_create_square(self):
        """Test create method for Square."""
        square_dict = {'id': 2, 'size': 7, 'x': 1, 'y': 0}
        square_instance = Square.create(**square_dict)

        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 7)
        self.assertEqual(square_instance.x, 1)
        self.assertEqual(square_instance.y, 0)

    def test_create_invalid_class(self):
        """Test create method with an unsupported class."""
        with self.assertRaises(ValueError):
            Base.create()


    def setUp(self):
        """Create temporary JSON files for testing."""
        self.rectangle_json_file = "Rectangle.json"
        self.square_json_file = "Square.json"
        self.invalid_json_file = "Invalid.json"

        with open(self.rectangle_json_file, 'w') as file:
            file.write('[{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}]')

        with open(self.square_json_file, 'w') as file:
            file.write('[{"id": 2, "size": 7, "x": 1, "y": 0}]')

    def tearDown(self):
        """Clean up temporary files."""
        json_files = [
            self.rectangle_json_file,
            self.square_json_file,
            self.invalid_json_file
        ]

        for file in json_files:
            if os.path.exists(file):
                os.remove(file)

    def test_load_rectangle_from_file(self):
        """Test loading Rectangle instances from a file."""
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[0].width, 5)
        self.assertEqual(rectangles[0].height, 10)
        self.assertEqual(rectangles[0].x, 2)
        self.assertEqual(rectangles[0].y, 3)

    def test_load_square_from_file(self):
        """Test loading Square instances from a file."""
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].id, 2)
        self.assertEqual(squares[0].size, 7)
        self.assertEqual(squares[0].x, 1)
        self.assertEqual(squares[0].y, 0)

    def test_load_from_nonexistent_file(self):
        """Test loading from a nonexistent file."""
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_invalid_file(self):
        """Test loading from an invalid JSON file."""
        with open(self.invalid_json_file, 'w') as file:
            file.write('invalid_json_string')

        instances = Base.load_from_file()
        self.assertEqual(instances, [])
