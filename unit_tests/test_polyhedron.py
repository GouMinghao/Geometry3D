# -*- coding: utf-8 -*-
import math
import unittest
from Geometry3D import *
import Geometry3D
import copy

a = Point(1,1,1)
b = Point(-1,1,1)
c = Point(-1,-1,1)
d = Point(1,-1,1)
e = Point(1,1,-1)
f = Point(-1,1,-1)
g = Point(-1,-1,-1)
h = Point(1,-1,-1)

cpg0 = ConvexPolygon((a,d,h,e))
cpg1 = ConvexPolygon((a,e,f,b))
cpg2 = ConvexPolygon((c,b,f,g))
cpg3 = ConvexPolygon((c,g,h,d))
cpg4 = ConvexPolygon((a,b,c,d))
cpg5 = ConvexPolygon((e,h,g,f))
cph0 = ConvexPolyhedron((cpg0,cpg1,cpg2,cpg3,cpg4,cpg5))
cph00 = ConvexPolyhedron((cpg1,cpg2,cpg0,cpg3,cpg4,cpg5))

cpg12 = ConvexPolygon((e,c,h))
cpg13 = ConvexPolygon((e,f,c))
cpg14 = ConvexPolygon((c,f,g))
cpg15 = ConvexPolygon((h,c,g))
cpg16 = ConvexPolygon((h,g,f,e))
cph1 = ConvexPolyhedron((cpg12,cpg13,cpg14,cpg15,cpg16))

a1 = Point(1.5,1.5,1.5)
b1 = Point(-0.5,1.5,1.5)
c1 = Point(-0.5,-0.5,1.5)
d1 = Point(1.5,-0.5,1.5)
e1 = Point(1.5,1.5,-0.5)
f1 = Point(-0.5,1.5,-0.5)
g1 = Point(-0.5,-0.5,-0.5)
h1 = Point(1.5,-0.5,-0.5)

cpg6 = ConvexPolygon((a1,d1,h1,e1))
cpg7 = ConvexPolygon((a1,e1,f1,b1))
cpg8 = ConvexPolygon((c1,b1,f1,g1))
cpg9 = ConvexPolygon((c1,g1,h1,d1))
cpg10 = ConvexPolygon((a1,b1,c1,d1))
cpg11 = ConvexPolygon((e1,h1,g1,f1))
cph2 = ConvexPolyhedron((cpg6,cpg7,cpg8,cpg9,cpg10,cpg11))

class ConvexPolyhedronTest(unittest.TestCase):
    def test_polyhedron_length(self):
        self.assertAlmostEqual(cph0.length(),24)

    def test_polyhedron_area(self):
        self.assertAlmostEqual(cph0.area(),24)
        self.assertAlmostEqual(cph1.area(),8 + 4*math.sqrt(2))

    def test_polyhedron_volume(self):
        self.assertAlmostEqual(cph0.volume(),8)
        self.assertAlmostEqual(volume(cph0),8)
        self.assertAlmostEqual(cph00.volume(),8)
        self.assertAlmostEqual(volume(cph00),8)
        self.assertAlmostEqual(cph1.volume(),8/3)
        self.assertAlmostEqual(volume(cph1),8/3)

    def test_polyhedron_hash(self):
        self.assertEqual(hash(cph0),hash(cph00))
        self.assertNotEqual(hash(cph0),hash(cph1))
        
    def test_polyhedron_move(self):
        self.assertEqual(copy.deepcopy(cph0).move(Vector(0.5,0.5,0.5)),cph2)
        self.assertNotEqual(copy.deepcopy(cph0).move(Vector(0.1,0.2,0)),cph00)

    def test_polyhedron_contains(self):
        self.assertTrue(origin() in cph00)
        self.assertTrue(a in cph00)
        self.assertFalse(g in cph2)
    
    def test_polyhedron_parallelpiped(self):
        cph = Parallelepiped(Point(-1,-1,-1),Vector(2,0,0),Vector(0,2,0),Vector(0,0,2))
        self.assertAlmostEqual(cph.volume(),8)
