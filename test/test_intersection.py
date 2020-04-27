# -*- coding: utf-8 -*-
import math
import unittest
from shape3d import *
import shape3d
import copy

class PointIntersectionTest(unittest.TestCase):
    def test_intersection_point_point(self):
        self.assertEqual(intersection(origin(),Point(0,0,0)),origin())
        self.assertEqual(intersection(Point(0,0,0),origin()),origin())
        self.assertTrue(intersection(origin(),Point(1,1,0)) is None)
    
    def test_intersection_point_line(self):
        self.assertTrue(intersection(x_axis(),origin()) == origin())
        self.assertTrue(intersection(origin(),x_axis()) == origin())
        self.assertTrue(intersection(Point(1,0,3),y_axis()) is None)
    
    def test_intersection_point_plane(self):
        self.assertEqual(intersection(Point(1,2,0),xy_plane()),Point(1,2,0))
        self.assertEqual(intersection(xy_plane(),Point(1,2,0)),Point(1,2,0))
        self.assertTrue(intersection(xy_plane(),Point(0,0,0.1)) is None)

    def test_intersection_point_segment(self):
        self.assertEqual(intersection(origin(),Segment(Point(-1,0,0),Point(1,0,0))),origin())
        self.assertEqual(intersection(Segment(Point(-1,0,0),Point(1,0,0)),origin()),origin())
        self.assertEqual(intersection(Segment(Point(0,0,0),Point(1,0,0)),origin()),origin())
        self.assertEqual(intersection(Segment(Point(-1,-1,-1),Point(1,1,1)),origin()),origin())
        self.assertTrue(intersection(Segment(Point(-1,-1,-1),Point(1,1,1)),Point(0,0,0.1)) is None)

    def test_intersection_point_convexpolygen(self):
        cpg = Parallelogram(origin(),Vector(1,0,1),Vector(0,1,1))
        self.assertEqual(intersection(origin(),cpg),origin())
        self.assertEqual(intersection(Point(1,0,1),cpg),Point(1,0,1))
        self.assertEqual(intersection(Point(0.5,0,0.5),cpg),Point(0.5,0,0.5))
        self.assertEqual(intersection(cpg,Point(0.5,0.5,1)),Point(0.5,0.5,1))
        self.assertTrue(intersection(cpg,Point(0.5,0.5,1.02)) is None)

    def test_intersection_point_convexpolyhedron(self):
        cph = Parallelepiped(origin(),Vector(1,0,0),Vector(0,1,0),Vector(0,0,2))
        self.assertEqual(intersection(cph,origin()),origin())
        self.assertEqual(intersection(Point(0.5,0,0),cph),Point(0.5,0,0))
        self.assertEqual(intersection(cph,Point(0.5,0.5,0)),Point(0.5,0.5,0))
        self.assertEqual(intersection(Point(0.5,0.5,1),cph),origin().move(Vector(0.5,0.5,1)))
        self.assertTrue(intersection(cph,Point(-0.1,0.5,0.5)) is None)

class LineIntersectionTest(unittest.TestCase):
    def test_intersection_line_line(self):
        l1 = x_axis()
        l2 = Line(Point(1,0,0),Point(2,0,0))
        l3 = z_axis()
        l4 = Line(Point(1,2,0),Point(2,3,0))
        self.assertEqual(intersection(l1,l2),l1)
        self.assertEqual(intersection(l1,l3),origin())
        self.assertTrue(intersection(l3,l4) is None)
    
    def test_intersection_line_plane(self):
        l1 = x_axis()
        p1 = xy_plane()
        l2 = z_axis()
        l3 = Line(Point(2,3,2),Point(3,5,2))
        self.assertEqual(intersection(l1,p1),l1)
        self.assertEqual(intersection(p1,l2),origin())
        self.assertTrue(intersection(p1,l3) is None)
    
    def test_intersection_line_segment(self):
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

    def test_intersection_line_convexpolygen(self):
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
        
    def test_intersection_line_convexpolyhedron(self):
        cph = Parallelepiped(origin(),x_unit_vector(),y_unit_vector(),z_unit_vector())
        l1 = x_axis()
        l2 = Line(Point(1,1,0),Point(0,0,0))
        l3 = Line(Point(1,1,0),Point(0.5,0,0))
        l4 = Line(Point(0.5,0,0),Point(1,0.5,0))
        l5 = Line(Point(1,0,0),Point(2,1,0))
        l6 = Line(Point(0.5,0.5,0),Point(0.6,0.6,1))
        l7 = Line(origin(),Point(1,1,1))
        l8 = Line(Point(0,0,1), Point(1,1,1))
        l9 = Line(Point(0,0,0.5),Point(1,1,1))
        l10 = Line(Point(-1,-1,-1),Point(-2,-2,0))
        l11 = Line(Point(-1,0,0),Point(1,0,1))
        l12 = Line(Point(0,0,2),Point(2,2,0))
        l13 = Line(Point(1,-1,0),Point(0,1,2))
        l14 = Line(Point(0.5,0,0),Point(1,1,1))
        self.assertEqual(intersection(cph,l1),Segment(origin(),Point(1,0,0)))
        self.assertEqual(intersection(cph,l2),Segment(origin(),Point(1,1,0)))
        self.assertEqual(intersection(cph,l3),Segment(Point(0.5,0,0),Point(1,1,0)))
        self.assertEqual(intersection(cph,l4),Segment(Point(0.5,0,0),Point(1,0.5,0)))
        self.assertEqual(intersection(cph,l5),Point(1,0,0))
        self.assertEqual(intersection(cph,l6),Segment(Point(0.5,0.5,0),Point(0.6,0.6,1)))
        self.assertEqual(intersection(cph,l7),Segment(Point(0,0,0),Point(1,1,1)))
        self.assertEqual(intersection(cph,l8),Segment(Point(0,0,1),Point(1,1,1)))
        self.assertEqual(intersection(cph,l9),Segment(Point(0,0,0.5),Point(1,1,1)))
        self.assertTrue(intersection(cph,l10) is None)
        self.assertEqual(intersection(cph,l11),Segment(Point(0,0,0.5),Point(1,0,1)))
        self.assertEqual(intersection(cph,l12),Point(1,1,1))
        self.assertEqual(intersection(cph,l13),Point(0.5,0,1))
        self.assertEqual(intersection(cph,l14),Segment(Point(0.5,0,0),Point(1,1,1)))

class PlaneIntersectionTest(unittest.TestCase):
    def test_intersection_plane_plane(self):
        p1 = xy_plane()
        p2 = xy_plane()
        p3 = xz_plane()
        p4 = xy_plane().move(z_unit_vector())
        self.assertEqual(intersection(p1,p2),xy_plane())
        self.assertEqual(intersection(p1,p3),x_axis())
        self.assertTrue(intersection(p1,p4) is None)
    
    def test_intersection_plane_segment(self):
        p1 = xy_plane()
        s1 = Segment(Point(0,0,-1),Point(0,0,1))
        s2 = Segment(Point(-2,3,0),Point(2,34.3,0))
        s3 = Segment(Point(1,3,0.1),Point(2,34,0.1))
        self.assertEqual(intersection(p1,s1),origin())
        self.assertEqual(intersection(s2,p1),s2)
        self.assertTrue(intersection(s3,p1) is None)

    def test_intersection_plane_convexpolygen(self):
        p1 = xy_plane()
        cpg1 = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
        cpg2 = Parallelogram(origin(),x_unit_vector(),z_unit_vector())
        cpg3 = Parallelogram(origin(),Vector(0,1,1),Vector(0,-1,1))
        cpg4 = copy.deepcopy(cpg2).move(Vector(0,0,-0.5))
        cpg5 = Parallelogram(origin().move(z_unit_vector()),x_unit_vector(),y_unit_vector())
        self.assertEqual(intersection(p1,cpg1),cpg1)
        self.assertEqual(intersection(p1,cpg2),Segment(origin(),Point(1,0,0)))
        self.assertEqual(intersection(p1,cpg3),origin())
        self.assertEqual(intersection(p1,cpg4),Segment(origin(),Point(1,0,0)))
        self.assertTrue(intersection(p1,cpg5) is None)
    
    def test_intersection_plane_convexpolyhedron(self):
        cph = Parallelepiped(origin(),x_unit_vector(),y_unit_vector(),z_unit_vector())
        p1 = xy_plane()
        p2 = xy_plane().move(Vector(0,0,0.5))
        p3 = Plane(Point(1,1,1),Vector(1,1,1))
        p4 = Plane(origin(),Vector(-1,-1,0))
        p5 = Plane(Point(0.1,0.1,0.1),Vector(1,1,1))
        p6 = Plane(Point(-0.1,-0.1,-0.1),Vector(-1,-1,-1))
        p7 = xy_plane().move(-z_unit_vector())
        self.assertTrue(intersection(cph,p1).eq_without_narmal(Parallelogram(origin(),x_unit_vector(),y_unit_vector())))
        self.assertTrue(intersection(cph,p2).eq_without_narmal(Parallelogram(origin().move(0.5*z_unit_vector()),x_unit_vector(),y_unit_vector())))
        self.assertEqual(intersection(cph,p3),Point(1,1,1))
        self.assertEqual(intersection(cph,p4),Segment(origin(),Point(0,0,1)))
        self.assertTrue(intersection(cph,p5).eq_without_narmal(ConvexPolygen((Point(0,0,0.3),Point(0,0.3,0),Point(0.3,0,0)))))
        self.assertTrue(intersection(cph,p6) is None)
        self.assertTrue(intersection(cph,p7) is None)

class SegmentIntersectionTest(unittest.TestCase):
    def test_intersection_segment_segment(self):
        p1 = Point(-0.5,0,0)
        p2 = origin()
        p3 = Point(0.5,0,0)
        p4 = Point(1,0,0)
        p5 = Point(0,-0.5,0)
        p6 = Point(0,0.5,0)
        p7 = Point(-0.5,1,0)
        p8 = Point(1,1,0)
        self.assertEqual(intersection(Segment(p1,p2),Segment(p2,p4)),p2)
        self.assertEqual(intersection(Segment(p1,p3),Segment(p2,p4)),Segment(p2,p3))
        self.assertEqual(intersection(Segment(p1,p4),Segment(p2,p3)),Segment(p2,p3))
        self.assertTrue(intersection(Segment(p1,p2),Segment(p3,p4)) is None)
        self.assertEqual(intersection(Segment(p5,p6),Segment(p1,p4)),p2)
        self.assertTrue(intersection(Segment(p7,p8),Segment(p1,p2)) is None)
        self.assertTrue(intersection(Segment(p7,p4),Segment(p2,p3)) is None)
        self.assertEqual(intersection(Segment(p1,p4),Segment(p4,p5)),p4)

    def test_intersection_segment_convexpolygen(self):
        cpg = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
        s1 = Segment(origin(),Point(1,0,0))
        s2 = Segment(Point(-0.5,0.5,0),Point(0.5,0.5,0))
        s3 = Segment(Point(-0.5,0.5,0),Point(1.5,0.5,0))
        s4 = Segment(Point(0.2,0.5,0),Point(0.8,0.5,0))
        s5 = Segment(origin(),origin().move(z_unit_vector()))
        s6 = Segment(Point(-1,-1,0),Point(1.5,1.5,0))
        s7 = copy.deepcopy(s5).move(Vector(-0.1,-0.1,0))
        s8 = Segment(Point(0.5,0.5,0.5),Point(0.5,0.5,1))
        s9 = Segment(Point(0.5,0.4,1),Point(0.5,0.5,1))
        self.assertEqual(intersection(cpg,s1),s1)
        self.assertEqual(intersection(cpg,s2),Segment(Point(0,0.5,0),Point(0.5,0.5,0)))
        self.assertEqual(intersection(cpg,s3),Segment(Point(0,0.5,0),Point(1,0.5,0)))
        self.assertEqual(intersection(cpg,s4),s4)
        self.assertEqual(intersection(cpg,s5),origin())
        self.assertEqual(intersection(cpg,s6),Segment(origin(),Point(1,1,0)))
        self.assertTrue(intersection(cpg,s7) is None)
        self.assertTrue(intersection(cpg,s8) is None)
        self.assertTrue(intersection(cpg,s9) is None)

