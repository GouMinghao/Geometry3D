# -*- coding: utf-8 -*-
"""Solver Module, An Auxilary Module"""
from __future__ import division
from .constant import get_eps
def shape(m):
    if not m:
        return (0, 0)
    return (len(m), len(m[0]))

def null(f):
    return abs(f) < get_eps()

def nullrow(r):
    return all(map(null, r))

def find_pivot_row(m):
    candidates = []
    for i, row in enumerate(m):
        # Only rows where the pivot element is not zero can be used
        if row[0] != 0:
            candidates.append((abs(row[0]), i))
    if not candidates:
        return None
    # We use the one with the biggest absolute value
    return max(candidates)[1]

def gaussian_elimination(m):
    """Return the row echelon form of m by applying the gaussian
    elimination"""
    # Shape of the matrix
    M, N = shape(m)
    for j in range(N-1):
        # We ignore everything above the jth row and everything left of
        # the jth column (we assume they are 0 already)
        pivot = find_pivot_row([row[j:] for row in m[j:]])
        if pivot is None:
            continue
        # find_pivot_row returns the index relative to j, so we need to
        # calculate the absolute index
        pivot += j
        # Swap the rows
        m[j], m[pivot] = m[pivot], m[j]
        # Note that the pivot row is now m[j]!
        # Eliminate everything else
        for i in range(j + 1, M):
            factor = m[i][j] / m[j][j] * -1
            # Multiply the pivot row before adding them
            multiplied_row = [factor * x for x in m[j]]
            # Looks ugly, but we don't need numpy for it
            # Replace the ith row with the sum of the ith row and the
            # pivot row
            m[i] = [x + y for x, y in zip(m[i], multiplied_row)]
    # m shold now be in row echelon form
    return m

def solve(matrix):
    ref = gaussian_elimination(matrix)
    return Solution(ref)

def count(f, l):
    c = 0
    for i in l:
        if f(i):
            c += 1
    return c

def index(f, l):
    for i, v in enumerate(l):
        if f(v):
            return i
    raise ValueError("No item satisfies {}".format(f))

def first_nonzero(r):
    for i, v in enumerate(r):
        if not null(v):
            return i
    return len(r)

class Solution(object):
    """Holds a solution to a system of equations."""
    def __init__(self, s):
        self._s = s
        self.varcount = shape(s)[1] - 1
        # No solution, 0a + 0b + 0c + ... = 1 which can never be true
        self._solvable = not any(
            all(null(coeff) for coeff in row[:-1]) and not null(row[-1])
            for row in s
        )
        unique_equations = sum(1 for row in s if not nullrow(row))
        self.varargs = self.varcount - unique_equations
        self.exact =  self.varargs == 0

    def __bool__(self):
        return self._solvable
    __nonzero__ = __bool__

    def __call__(self, *v):
        if not self._solvable:
            raise ValueError("Has no solution")
        if len(v) != self.varargs:
            raise ValueError("Expected {} values, got {}".format(
                self.varargs, len(v)))
        v = list(v)
        vals = [None] * self.varcount
        # Scan for real solutions
        for i, row in enumerate(self._s):
            # Can't use .count here because we need null()
            # I miss Haskell lambdas :(
            if count(lambda i: not null(i), row[:-1]) == 1:
                # We can find a variable here
                var = index(lambda i: not null(i), row[:-1])
                vals[var] = row[-1] / row[var]
        # Fill in the rest with given values
        for i in reversed(range(len(vals))):
            if not v:
                break
            if vals[i] is None:
                vals[i] = v.pop()

        for i in reversed(range(len(self._s))):
            row = self._s[i]
            if nullrow(row):
                continue
            tbd = first_nonzero(row)
            s = sum(-1 * row[j] * vals[j] for j in range(tbd + 1, len(row) - 1))
            s += row[-1]
            vals[tbd] = s / row[tbd]
        return tuple(vals)
