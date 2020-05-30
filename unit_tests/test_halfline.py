# -*- coding: utf-8 -*-
import math
import unittest
from Geometry3D import *
import Geometry3D

class HalfLineTest(unittest.TestCase):
    def test_halfline_in_line(self):
        self.assertTrue(
            HalfLine(origin(),Point(1,0,0)) in x_axis()
        )

    def test_halfline_in_plane(self):
        self.assertTrue(
            HalfLine(origin(),Point(1,0,0)) in xy_plane()
        )
        self.assertTrue(
            HalfLine(origin(),Point(1,0,0)) in xz_plane()
        )
        self.assertFalse(
            HalfLine(origin(),Point(1,0,0)) in yz_plane()
        )
    
    def test_halfline_contains_point(self):
        self.assertTrue(
            origin() in HalfLine(origin(),Point(1,0,0))
        )
        self.assertTrue(
            Point(100,0,0) in HalfLine(origin(),Point(1,0,0))
        )
        self.assertTrue(
            Point(-get_eps() / 100,0,0) in HalfLine(origin(),Point(1,0,0))
        )
        self.assertFalse(
            Point(-1,0,0) in HalfLine(origin(),Point(1,0,0))
        )
        self.assertFalse(
            Point(1,1,1) in HalfLine(origin(),Point(1,0,0))
        )
    
    def test_halfline_contains_segment(self):
        self.assertTrue(
            Segment(origin(),Point(1,0,0)) in HalfLine(origin(),Point(1,0,0))
        )
        self.assertTrue(
            Segment(origin(),Point(2,0,0)) in HalfLine(origin(),Point(1,0,0))
        )
        self.assertFalse(
            Segment(Point(-1,0,0),Point(1,0,0)) in HalfLine(origin(),Point(1,0,0))
        )
        self.assertFalse(
            Segment(Point(1,0,0),Point(1,1,1)) in HalfLine(origin(),Point(1,0,0))
        )
        self.assertTrue(
            Segment(Point(1,0,0),Point(2,0,0)) in HalfLine(origin(),Point(1,0,0))
        )

    def test_halfline_contains_halfline(self):
        h1 = HalfLine(origin(),Point(1,0,0))
        h2 = HalfLine(Point(1,0,0),Point(2,0,0))
        h3 = HalfLine(origin(),Point(1,0,0))
        h4 = HalfLine(origin(),Point(-1,0,0))
        h5 = HalfLine(Point(1,0,0),Point(2,1,0))
        h6 = HalfLine(Point(1,0,0),Vector(-1,0,0))
        self.assertTrue(h2 in h1)
        self.assertTrue(h3 in h1)
        self.assertFalse(h4 in h1)
        self.assertFalse(h5 in h1)
        self.assertFalse(h6 in h1)

    def test_halfline_segment_hash(self):
        s = set()
        s.add(
            HalfLine(origin(),Point(1,0,0))
        )
        s.add(
            HalfLine(origin(),2 * x_unit_vector())
        )
        self.assertEqual(len(s),1)
    
    def test_halfline_equal(self):
        self.assertTrue(HalfLine(origin(),Point(1,0,0)),HalfLine(Point(0,0,0),Vector(3,0,0)))

    def test_halfline_move(self):
        self.assertEqual(
            HalfLine(origin(),Point(2,3,1)).move(Vector(1,2,3)),
            HalfLine(Point(1,2,3),Vector(2,3,1))
        )

