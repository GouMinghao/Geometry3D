# -*- coding: utf-8 -*-
import math
import unittest
from shape3d import *
v0 = Vector(1,1,2)
v1 = Vector(2,2,4)
v1_ = Vector(2,2,5)
v2 = Vector(0.5,0.5,1)
v3 = Vector(-0.1,-0.1,-0.2)
class aux_calc_Test(unittest.TestCase):
    def test_aux_calc_projection_length(self):
        self.assertAlmostEqual(get_projection_length(v1,v0),v1.length())
        self.assertAlmostEqual(get_projection_length(v2,v0),v2.length())

    def test_aux_calc_relative_projection_length(self):
        self.assertAlmostEqual(get_relative_projection_length(v1,v0),2)
        self.assertAlmostEqual(get_relative_projection_length(v2,v0),0.5)
        self.assertAlmostEqual(get_relative_projection_length(v3,v0),-0.1)
    
    def test_aux_calc_segment_from_point_list(self):
        a = Point(0,0,0)
        b = Point(1,1,1)
        c = Point(0.5,0.5,0.5)
        d = Point(-0.5,-0.5,-0.5)
        e = Point(1.1,1.1,1.1)
        self.assertEqual(get_segment_from_point_list([a,b,c,d,e]),Segment(d,e))
        self.assertEqual(get_segment_from_point_list([a,b]),Segment(b,a))