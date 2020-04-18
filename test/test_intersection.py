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

class LineIntersectionTest(unittest.TestCase):
    def test_line_line(self):
        l1 = x_axis()
        l2 = Line(Point(1,0,0),Point(2,0,0))
        l3 = z_axis()
        l4 = Line(Point(1,2,0),Point(2,3,0))
        self.assertEqual(intersection(l1,l2),l1)
        self.assertEqual(intersection(l1,l3),origin())
        self.assertTrue(intersection(l3,l4) is None)
    
    def test_line_plane(self):
        l1 = x_axis()
        p1 = xy_plane()
        l2 = z_axis()
        l3 = Line(Point(2,3,2),Point(3,5,2))
        self.assertEqual(intersection(l1,p1),l1)
        self.assertEqual(intersection(p1,l2),origin())
        self.assertTrue(intersection(p1,l3) is None)
    
    def test_line_segment(self):
        l1 = x_axis()
        s1 = Segment(origin(),Point(1,0,0))
        l2 = z_axis()
        s2 = Segment(Point(-0.5,0,0),Point(0.5,0,0))
        s3 = Segment(Point(0.43,0.2224,-0.34),Point(0.23,0.234,0.241))
        s4 = Segment(Point(0.21,1321,1),Point(-0.24,-93,1))
        self.assertEqual(intersection(l1,s1),s1)
        self.assertEqual(intersection(l2,s1),origin())
        self.assertEqual(intersection(s2,l2),origin())
        self.assertTrue(intersection(s3,l2) is None)
        self.assertTrue(intersection(s4,l2) is None)

    def test_line_convexpolygen(self):
        cpg = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
        l1 = x_axis()
        l2 = Line(Point(1,1,0),Point(0,0,0))
        l3 = Line(Point(1,1,0),Point(0.5,0,0))
        l4 = Line(Point(0.5,0,0),Point(1,0.5,0))
        l5 = Line(Point(1,0,0),Point(2,1,0))
        l6 = Line(Point(0.5,0.5,0),Point(0.6,0.6,2))
        l7 = Line(origin(),Point(1,1,1))
        l8 = Line(Point(0,0,1), Point(1,1,1))
        l9 = Line(Point(0,0,0.5),Point(1,1,1))
        self.assertEqual(intersection(cpg,l1),Segment(origin(),Point(1,0,0)))
        self.assertEqual(intersection(cpg,l2),Segment(origin(),Point(1,1,0)))
        self.assertEqual(intersection(cpg,l3),Segment(Point(0.5,0,0),Point(1,1,0)))
        self.assertEqual(intersection(cpg,l4),Segment(Point(0.5,0,0),Point(1,0.5,0)))
        self.assertEqual(intersection(cpg,l5),Point(1,0,0))
        self.assertEqual(intersection(cpg,l6),Point(0.5,0.5,0))
        self.assertEqual(intersection(cpg,l7),Point(0,0,0))
        self.assertTrue(intersection(cpg,l8) is None)
        self.assertTrue(intersection(cpg,l9) is None)
        
