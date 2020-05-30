# -*- coding: utf-8 -*-
import math
import unittest
from Geometry3D import *
import Geometry3D
a = origin()
b = Point(1,0,1)
c = Point(0,1,1)
d = Point(1,1,2)
class ConvexPolygonTest(unittest.TestCase):
    def test_polygon_length(self):
        self.assertAlmostEqual(
            ConvexPolygon((a,b,c,d)).length(),
            4 * math.sqrt(2)
        )
    def test_polygon_area(self):
        self.assertAlmostEqual(
            ConvexPolygon((a,b,c,d)).area(),
            math.sqrt(3)
        )

    def test_polygon_in_plane(self):
        self.assertTrue(
            ConvexPolygon((a,b,c,d)) in Plane(origin(),Vector(1,1,-1))
        )
        self.assertFalse(
            ConvexPolygon((a,b,c,d)) in Plane(origin(),Vector(1,1.1,-1))
        )
    
    def test_polygon_contains_point(self):
        self.assertTrue(
            origin() in ConvexPolygon((a,b,c,d))
        )

        self.assertTrue(
            Point(0.5,0.5,1) in ConvexPolygon((a,b,c,d))
        )

    def test_polygon_contains_segment(self):
        self.assertTrue(
            Segment(origin(),Point(0.5,0.5,1)) in ConvexPolygon((a,b,c,d))
        )
        self.assertTrue(
            Segment(origin(),Point(1,1,2)) in ConvexPolygon((a,b,c,d))
        )
        self.assertFalse(
            Segment(origin().move(Vector(0,0,1)),
            Point(1,1,2).move(Vector(0,0,1))
            ) in ConvexPolygon((a,b,c,d))
        )

    def test_polygon_eq(self):
        self.assertEqual(
            ConvexPolygon((a,b,d,c)),
            ConvexPolygon((c,a,b,d))
        )
        # self.assertNotEqual(
        #     ConvexPolygon((a,b,d,c)),
        #     -ConvexPolygon((c,a,b,d))
        # )

    def test_polygon_eq_without_normal(self):
        self.assertTrue(
            ConvexPolygon((a,b,d,c)) == (ConvexPolygon((c,a,b,d)))
        )
        self.assertTrue(
            ConvexPolygon((a,b,d,c)) == (-ConvexPolygon((c,a,b,d)))
        )
    
    def test_polygon_hash(self):
        s = set()
        s.add(ConvexPolygon((a,b,d,c)))
        s.add(ConvexPolygon((c,a,b,d)))
        self.assertEqual(len(s),1)

    def test_polygon_move(self):
        v = Vector(1,2,3)
        cpg0 = ConvexPolygon((a,b,d,c))
        cpg1 = ConvexPolygon((a.move(v),b.move(v),c.move(v),d.move(v)))
        self.assertEqual(cpg0.move(v),cpg1)

    def test_polygon_Parallelogram(self):
        self.assertTrue(Parallelogram(origin(),Vector(1,0,0),Vector(2,0,1)) == (ConvexPolygon((origin(),Point(3,0,1),Point(1,0,0),Point(2,0,1)))))
        self.assertTrue(Parallelogram(origin(),Vector(1,0,0),Vector(2,0,1)) == (ConvexPolygon((origin(),Point(2,0,1),Point(1,0,0),Point(3,0,1)))))