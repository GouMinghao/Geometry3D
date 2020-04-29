# -*- coding: utf-8 -*-
import math
import unittest
from Geometry3D import *
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

    def test_aux_calc_get_segment_convexpolyhedron_intersection_point_set(self):
        cph = Parallelepiped(origin(),x_unit_vector(),y_unit_vector(),z_unit_vector())
        s1 = Segment(origin(),Point(-1,-1,-1))
        inter_set1 = get_segment_convexpolyhedron_intersection_point_set(s1,cph)
        self.assertEqual(len(inter_set1),1)
        self.assertTrue(origin() in inter_set1)
        s2 = Segment(Point(0.5,0.5,-0.5),Point(0.5,0.5,1.5))
        inter_set2 = get_segment_convexpolyhedron_intersection_point_set(s2,cph)
        self.assertEqual(len(inter_set2),2)
        self.assertTrue(Point(0.5,0.5,0) in inter_set2)
        self.assertTrue(Point(0.5,0.5,1) in inter_set2)
        s3 = Segment(Point(0,-1,0),Point(1,1,0))
        inter_set3 = get_segment_convexpolyhedron_intersection_point_set(s3,cph)
        self.assertEqual(len(inter_set3),2)
        self.assertTrue(Point(0.5,0,0) in inter_set3)
        self.assertTrue(Point(1,1,0) in inter_set3)
        s4 = Segment(Point(0,-1,0),Point(1,-1,0))
        inter_set4 = get_segment_convexpolyhedron_intersection_point_set(s4,cph)
        self.assertEqual(len(inter_set4),0)
        
        