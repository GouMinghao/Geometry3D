# -*- coding: utf-8 -*-
import math
import unittest
from Geometry3D import *
import Geometry3D
a = origin()
b = Point(1,0,1)
c = Point(0,1,1)
d = Point(1,1,2)
class ConvexPolygenTest(unittest.TestCase):
    def test_polygen_length(self):
        self.assertAlmostEqual(
            ConvexPolygen((a,b,c,d)).length(),
            4 * math.sqrt(2)
        )
    def test_polygen_area(self):
        self.assertAlmostEqual(
            ConvexPolygen((a,b,c,d)).area(),
            math.sqrt(3)
        )

    def test_polygen_in_plane(self):
        self.assertTrue(
            ConvexPolygen((a,b,c,d)) in Plane(origin(),Vector(1,1,-1))
        )
        self.assertFalse(
            ConvexPolygen((a,b,c,d)) in Plane(origin(),Vector(1,1.1,-1))
        )
    
    def test_polygen_contains_point(self):
        self.assertTrue(
            origin() in ConvexPolygen((a,b,c,d))
        )

        self.assertTrue(
            Point(0.5,0.5,1) in ConvexPolygen((a,b,c,d))
        )

    def test_polygen_contains_segment(self):
        self.assertTrue(
            Segment(origin(),Point(0.5,0.5,1)) in ConvexPolygen((a,b,c,d))
        )
        self.assertTrue(
            Segment(origin(),Point(1,1,2)) in ConvexPolygen((a,b,c,d))
        )
        self.assertFalse(
            Segment(origin().move(Vector(0,0,1)),
            Point(1,1,2).move(Vector(0,0,1))
            ) in ConvexPolygen((a,b,c,d))
        )

    def test_polygen_eq(self):
        self.assertEqual(
            ConvexPolygen((a,b,d,c)),
            ConvexPolygen((c,a,b,d))
        )
        # self.assertNotEqual(
        #     ConvexPolygen((a,b,d,c)),
        #     -ConvexPolygen((c,a,b,d))
        # )

    def test_polygen_eq_without_normal(self):
        self.assertTrue(
            ConvexPolygen((a,b,d,c)) == (ConvexPolygen((c,a,b,d)))
        )
        self.assertTrue(
            ConvexPolygen((a,b,d,c)) == (-ConvexPolygen((c,a,b,d)))
        )
    
    def test_polygen_hash(self):
        s = set()
        s.add(ConvexPolygen((a,b,d,c)))
        s.add(ConvexPolygen((c,a,b,d)))
        self.assertEqual(len(s),1)

    def test_polygen_move(self):
        v = Vector(1,2,3)
        cpg0 = ConvexPolygen((a,b,d,c))
        cpg1 = ConvexPolygen((a.move(v),b.move(v),c.move(v),d.move(v)))
        self.assertEqual(cpg0.move(v),cpg1)

    def test_polygen_Parallelogram(self):
        self.assertTrue(Parallelogram(origin(),Vector(1,0,0),Vector(2,0,1)) == (ConvexPolygen((origin(),Point(3,0,1),Point(1,0,0),Point(2,0,1)))))
        self.assertTrue(Parallelogram(origin(),Vector(1,0,0),Vector(2,0,1)) == (ConvexPolygen((origin(),Point(2,0,1),Point(1,0,0),Point(3,0,1)))))