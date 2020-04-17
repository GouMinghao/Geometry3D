# -*- coding: utf-8 -*-
import math
import unittest
from shape3d import *
import shape3d

class PointIntersectionTest(unittest.TestCase):
    def test_point_point(self):
        self.assertEqual(intersection(origin(),Point(0,0,0)),origin())
        self.assertEqual(intersection(Point(0,0,0),origin()),origin())
        self.assertTrue(intersection(origin(),Point(1,1,0)) is None)
    
    def test_point_line(self):
        self.assertTrue(intersection(x_axis(),origin()) == origin())
        self.assertTrue(intersection(origin(),x_axis()) == origin())
        self.assertTrue(intersection(Point(1,0,3),y_axis()) is None)
    
    def test_point_plane(self):
        self.assertEqual(intersection(Point(1,2,0),xy_plane()),Point(1,2,0))
        self.assertEqual(intersection(xy_plane(),Point(1,2,0)),Point(1,2,0))
        self.assertTrue(intersection(xy_plane(),Point(0,0,0.1)) is None)

    def test_point_segment(self):
        self.assertEqual(intersection(origin(),Segment(Point(-1,0,0),Point(1,0,0))),origin())
        self.assertEqual(intersection(Segment(Point(-1,0,0),Point(1,0,0)),origin()),origin())
        self.assertEqual(intersection(Segment(Point(0,0,0),Point(1,0,0)),origin()),origin())
        self.assertEqual(intersection(Segment(Point(-1,-1,-1),Point(1,1,1)),origin()),origin())
        self.assertTrue(intersection(Segment(Point(-1,-1,-1),Point(1,1,1)),Point(0,0,0.1)) is None)

    def test_point_convexpolygen(self):
        cpg = Parallelogram(origin(),Vector(1,0,1),Vector(0,1,1))
        self.assertEqual(intersection(origin(),cpg),origin())
        self.assertEqual(intersection(Point(1,0,1),cpg),Point(1,0,1))
        self.assertEqual(intersection(Point(0.5,0,0.5),cpg),Point(0.5,0,0.5))
        self.assertEqual(intersection(cpg,Point(0.5,0.5,1)),Point(0.5,0.5,1))
        self.assertTrue(intersection(cpg,Point(0.5,0.5,1.02)) is None)

    def test_point_convexpolyhedron(self):
        cph = Parallelepiped(origin(),Vector(1,0,0),Vector(0,1,0),Vector(0,0,2))
        self.assertEqual(intersection(cph,origin()),origin())
        self.assertEqual(intersection(Point(0.5,0,0),cph),Point(0.5,0,0))
        self.assertEqual(intersection(cph,Point(0.5,0.5,0)),Point(0.5,0.5,0))
        self.assertEqual(intersection(Point(0.5,0.5,1),cph),origin().move(Vector(0.5,0.5,1)))
        self.assertTrue(intersection(cph,Point(-0.1,0.5,0.5)) is None)