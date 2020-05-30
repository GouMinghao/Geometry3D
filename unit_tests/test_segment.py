# -*- coding: utf-8 -*-
import math
import unittest
from Geometry3D import *
import Geometry3D

class SegmentTest(unittest.TestCase):
    def test_segment_length(self):
        self.assertAlmostEqual(
            Segment(origin(),Point(0,0,1)).length(),
            1
        )
        self.assertAlmostEqual(
            Segment(origin(),Point(1,1,1)).length(),
            math.sqrt(3)
        )

    def test_segment_in_line(self):
        self.assertTrue(
            Segment(origin(),Point(1,0,0)) in x_axis()
        )

    def test_segment_in_plane(self):
        self.assertTrue(
            Segment(origin(),Point(1,0,0)) in xy_plane()
        )
        self.assertTrue(
            Segment(origin(),Point(1,0,0)) in xz_plane()
        )
        self.assertFalse(
            Segment(origin(),Point(1,0,0)) in yz_plane()
        )

    def test_segment_segment_hash(self):
        s = set()
        s.add(
            Segment(origin(),Point(1,0,0))
        )
        s.add(
            Segment(Point(1,0,0),origin())
        )
        self.assertEqual(len(s),1)
    
    def test_segment_move(self):
        self.assertEqual(
            Segment(origin(),Point(2,3,1)).move(Vector(1,2,3)),
            Segment(Point(1,2,3),Vector(2,3,1))
        )
