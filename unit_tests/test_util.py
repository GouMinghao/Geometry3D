# -*- coding: utf-8 -*-
import unittest
import Geometry3D.utils.util as util

from decimal import Decimal as D
from fractions import Fraction as F


class UtilTest(unittest.TestCase):
    def test_unify_types_to_int(self):
        l = [1, 2, 3]
        self.assertEqual(util.unify_types(l), l)

    def test_unify_types_to_float(self):
        l = [1, 2.0, 3]
        self.assertEqual(util.unify_types(l), [1.0, 2.0, 3.0])

    def test_unify_types_to_decimal(self):
        l = [1, 2.0, D(3)]
        self.assertEqual(util.unify_types(l), [D(1), D(2), D(3)])

    def test_unify_types_to_fraction(self):
        l = [1, D(2), F(3)]
        self.assertEqual(util.unify_types(l), [F(1), F(2), F(3)])

    def test_unify_types_to_custom_type(self):
        class MyNumber(object):
            def __init__(self, x):
                if isinstance(x, MyNumber):
                    self.x = x.x
                else:
                    self.x = int(x)

        l = [1, F(2), MyNumber(3)]
        u = util.unify_types(l)
        for i in u:
            self.assertIsInstance(i, MyNumber)
        self.assertEqual([i.x for i in u], [1, 2, 3])
