# -*- coding: utf-8 -*-
import math
import unittest
from shape3d import *
import shape3d

class SegmentTest(unittest.TestCase):
    def test_length(self):
        self.assertAlmostEqual(
            Segment(origin(),Point(0,0,1)).length(),
            1
        )
        self.assertAlmostEqual(
            Segment(origin(),Point(1,1,1)).length(),
            math.sqrt(3)
        )

    def test_in_line(self):
        self.assertTrue(
            Segment(origin(),Point(1,0,0)) in x_axis()
        )

    def test_in_plane(self):
        self.assertTrue(
            Segment(origin(),Point(1,0,0)) in xy_plane()
        )
        self.assertTrue(
            Segment(origin(),Point(1,0,0)) in xz_plane()
        )
        self.assertFalse(
            Segment(origin(),Point(1,0,0)) in yz_plane()
        )

    def test_segment_hash(self):
        s = set()
        s.add(
            Segment(origin(),Point(1,0,0))
        )
        s.add(
            Segment(Point(1,0,0),origin())
        )
        self.assertEqual(len(s),1)
    
    def test_move(self):
        self.assertEqual(
            Segment(origin(),Point(2,3,1)).move(Vector(1,2,3)),
            Segment(Point(1,2,3),Vector(2,3,1))
        )
    # def test_vector_zero(self):
    #     self.assertEqual(
    #         Vector.zero(),
    #         Vector(0, 0, 0),
    #     )

    # def test_vector_coordinate_access(self):
    #     v = Vector(1, 2, 3)
    #     self.assertEqual(v[0], 1)
    #     self.assertEqual(v[1], 2)
    #     self.assertEqual(v[2], 3)

    # def test_vector_addition(self):
    #     self.assertEqual(
    #         Vector(2, 3, 5) + Vector(7, 11, 13),
    #         Vector(9, 14, 18),
    #     )
    
    # def test_vector_equality(self):
    #     self.assertEqual(Vector(1, 2, 3), Vector(1, 2, 3))
    #     self.assertNotEqual(Vector(1, 2, 3), Vector(1, 2, 4))

    # def test_vector_subtraction(self):
    #     self.assertEqual(
    #         Vector(9, 14, 18) - Vector(7, 11, 13),
    #         Vector(2, 3, 5),
    #     )

    # def test_vector_multiply_real_with_vector(self):
    #     self.assertEqual(
    #         2 * Vector(2, 3, 5),
    #         Vector(4, 6, 10),
    #     )

    # def test_vector_multiply_vector_with_vector(self):
    #     self.assertEqual(
    #         Vector(2, 3, 5) * Vector(7, 11, 13),
    #         2 * 7 + 3 * 11 + 5 * 13,
    #     )
    
    # def test_vector_inversion(self):
    #     self.assertEqual(
    #         -Vector(2, 3, 5),
    #         Vector(-2, -3, -5),
    #     )

    # def test_vector_coordinate_setting(self):
    #     v = Vector(2, 3, 5)
    #     v[0] = 7
    #     v[1] = 11
    #     v[2] = 13
    #     self.assertEqual(v, Vector(7, 11, 13))

    # def test_vector_cross_product(self):
    #     a = Vector(2, 3, 5)
    #     b = Vector(7, 11, 13)
    #     self.assertEqual(
    #         a.cross(b),
    #         Vector(
    #             3 * 13 - 5 * 11,
    #             5 * 7 - 2 * 13,
    #             2 * 11 - 3 * 7,
    #         ),
    #     )

    # def test_vector_length(self):
    #     self.assertEqual(
    #         abs(Vector(3, 4, 0)),
    #         5,
    #     )

    # def test_vector_parallel(self):
    #     self.assertTrue(Vector(2, 3, 5).parallel(Vector(4, 6, 10)))
    #     self.assertTrue(Vector(1, 0, 0).parallel(Vector(10, 0, 0)))
    #     self.assertFalse(Vector(2, 3, 5).parallel(Vector(4, 6, 11)))
    #     self.assertFalse(Vector(1, 0, 0).parallel(Vector(0, 1, 0)))

    # def test_vector_orthogonal(self):
    #     self.assertTrue(Vector(1, 0, 0).orthogonal(Vector(0, 1, 1)))
    #     self.assertFalse(Vector(1, 0, 0).orthogonal(Vector(1, 0, 0)))

    # def test_vector_angle(self):
    #     self.assertAlmostEqual(
    #         Vector(1, 0, 0).angle(Vector(1, 0, 1)),
    #         math.pi / 4,  # 45 deg
    #     )

    # def test_vector_normalization(self):
    #     self.assertAlmostEqual(abs(Vector(1, 1, 1).normalized()), 1)
