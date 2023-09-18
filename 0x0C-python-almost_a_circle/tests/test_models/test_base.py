#!/usr/bin/python3


"""
Summary: This module contains the unit tests for the Base class
Author: Alemi Herbert <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Perform a bunch of tests on the Base class
    """

    def test_no_arg(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_no_arg_multiple(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base().id, 4)

    def test_id_none(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base(None).id, 1)
        self.assertEqual(Base(None).id, 2)

    def test_id_unique(self):
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base(12).id, 12)

    def test_id_after_unique(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 3)

    def test_id_public(self):
        b = Base()
        b.id = 12
        self.assertEqual(b.id, 12)

    def test_nb_objects_private(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)

    def test_id_string(self):
        self.assertEqual(Base("hello").id, "hello")

    def test_id_float(self):
        self.assertEqual(Base(12.5).id, 12.5)

    def test_id_list(self):
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_id_tuple(self):
        self.assertEqual(Base((1, 2, 3)).id, (1, 2, 3))

    def test_id_dict(self):
        self.assertEqual(Base({"a": 1, "b": 2}).id, {"a": 1, "b": 2})

    def test_id_range(self):
        self.assertEqual(Base(range(10)).id, range(10))

    def test_id_frozenset(self):
        self.assertEqual(Base(frozenset({1, 2, 3})).id, frozenset({1, 2, 3}))

    def test_id_bool(self):
        self.assertEqual(Base(True).id, True)
        self.assertEqual(Base(False).id, False)

    def test_id_set(self):
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})

    def test_id_bytes(self):
        self.assertEqual(Base(b"hello").id, b"hello")

    def test_id_bytearray(self):
        self.assertEqual(Base(bytearray(b"hello")).id, bytearray(b"hello"))

    def test_id_inf(self):
        self.assertEqual(Base(float("inf")).id, float("inf"))

    def test_id_nan(self):
        self.assertNotEqual(Base(float("nan")).id, float("nan"))

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
