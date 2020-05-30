# -*- coding: utf-8 -*-
import unittest
from Geometry3D import solve


class SolverTest(unittest.TestCase):
    def test_has_no_solutions(self):
        m = [
            [2, 4, 6],
            [2, 4, 7],
        ]
        solution = solve(m)
        self.assertFalse(solution)

    def test_has_exact_solution(self):
        m = [
            [2, 2, 8],
            [2, -2, 0],
        ]
        solution = solve(m)
        self.assertTrue(solution)
        self.assertTrue(solution.exact)

    def test_has_many_solutions(self):
        m = [
            [2, 2, 8],
            [1, 1, 4],
        ]
        solution = solve(m)
        self.assertTrue(solution)
        self.assertFalse(solution.exact)

    def test_yields_different_solutions_for_different_input(self):
        m = [
            [2, 2, 8],
            [1, 1, 4],
        ]
        solution = solve(m)
        s1 = solution(1)
        s2 = solution(2)
        self.assertNotEqual(s1, s2)

    def test_yields_correct_solution(self):
        m = [
            [2, 2, 8],
            [2, -2, 0],
        ]
        solution = solve(m)
        s = solution()
        self.assertEqual(s, (2, 2))
