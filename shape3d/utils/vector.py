# -*- coding: utf-8 -*-
import math
import numpy as np
from .util import unify_types
from .constant import *

class Vector(object):
    """Provides a basic vector"""
    @classmethod
    def zero(cls):
        """Returns the zero vector (0 | 0 | 0)"""
        return cls(0, 0, 0)
    
    @classmethod
    def x_unit_vector(cls):
        """Returns the unit vector (1 | 0 | 0)"""
        return cls(1, 0, 0)
    
    @classmethod
    def y_unit_vector(cls):
        """Returns the unit vector (0 | 1 | 0)"""
        return cls(0, 1, 0)

    @classmethod
    def z_unit_vector(cls):
        """Returns the unit vector (0 | 0 | 1)"""
        return cls(0, 0, 1)

    def __init__(self, *args):
        """Vector(x, y, z)
        Vector([x, y, z]):
        A vector with coordinates (x | y | z)

        Vector(P1, P2):
        A vector going from point P1 to P2.
        """
        if len(args) == 3:
            # Initialising with 3 coordinates
            self._v = list(args)
        elif len(args) == 2:
            # Initialising from point A to point B
            A, B = args
            self._v = [
                B.x - A.x,
                B.y - A.y,
                B.z - A.z,
            ]
        elif len(args) == 1:
            # Initialising with an array of coordinates
            self._v = list(args[0])
        else:
            raise TypeError("Vector() takes one, two or three parameters, "
                            "not {}".format(len(args)))
        self._v = unify_types(self._v)

    def __hash__(self):
        return hash(("Vector",) + tuple(self))

    def __repr__(self):
        return "Vector({}, {}, {})".format(*self._v)
    
    def __eq__(self, other):
        return (self._v == other._v)

    def __add__(self, other):
        return Vector(x+y for x, y in zip(self, other))
    
    def __sub__(self, other):
        return Vector([x-y for x, y in zip(self, other)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum(x*y for x, y in zip(self, other))
        return Vector([x*other for x in self._v])

    def __rmul__(self, other):
        return self * other
    
    def __neg__(self):
        return self * -1

    def __getitem__(self, item):
        return self._v[item]

    def __setitem__(self, item, value):
        self._v[item] = value
    
    def tonumpy(self):
        return np.array(self._v)
    
    def cross(self, other):
        r"""Calculates the cross product of two vectors, defined as
        _   _   / x2y3 - x3y2 \
        x × y = | x3y1 - x1y3 |
                \ x1y2 - x2y1 /

        The cross product is orthogonal to both vectors and its length
        is the area of the parallelogram given by x and y.
        """
        a, b = self._v, other._v
        return Vector(
                a[1] * b[2] - a[2] * b[1],
                a[2] * b[0] - a[0] * b[2],
                a[0] * b[1] - a[1] * b[0]
                )

    def length(self):
        """Returns |v|, the length of the vector."""
        return (self * self) ** 0.5
    __abs__ = length

    def parallel(self, other):
        """Returns true if both vectors are parallel."""
        from .solver import solve
        if self == Vector.zero() or other == Vector.zero():
            return True
        if self == other:
            return True
        # linear combination:
        # a * self + b * other = 0
        # solution = solve([
        #     [self[0], other[0], 0],
        #     [self[1], other[1], 0],
        #     [self[2], other[2], 0],
        # ])

        return abs(self * other - self.length() * other.length()) < EPS_F 

        # Trivial solution is a = b = 0
        # if there are no other solutions, the vectors are not parallel!
        # otherwise there are infinitely many solutions and the vectors
        # are parallel.
        if solution.exact:
            return False
        return True

    def orthogonal(self, other):
        """Returns true if the two vectors are orthogonal"""
        return self * other == 0

    def angle(self, other):
        """Returns the angle (in radians) enclosed by both vectors."""
        return math.acos((self * other) / (self.length() * other.length()))

    def normalized(self):
        """Return the normalized version of the vector, that is a vector
        pointing in the same direction but with length 1.
        """
        # Division is not defined, so we have to multiply by 1/|v|
        return float(1 / self.length()) * self
    unit = normalized

    def draw(self, renderer, box, origin=(0, 0, 0), color=(1, 0, 0)):
        """Draw the vector, represented by an arrow, starting at the
        given origin on the given renderer (vtk).

        The box argument is ignored.

        origin defaults to (0 | 0 | 0).
        color defaults to red.
        """
        from .point import Point
        import vtk
        if not isinstance(origin, Point):
            origin = Point(origin)
        # Drawing arrows needs transformation matrices, which I don't
        # know anything about, so we just draw a simple line and put
        # a little hat (cone) on it. This the easier way for us
        # mortals.
        lineSrc = vtk.vtkLineSource()
        # Again, using switched coordinates
        lineSrc.SetPoint1(origin.y, origin.z, origin.x)
        end = Point(origin.pv() + self)
        lineSrc.SetPoint2(end.y, end.z, end.x)
        lineMap = vtk.vtkPolyDataMapper()
        lineMap.SetInput(lineSrc.GetOutput())
        lineAct = vtk.vtkActor()
        lineAct.SetMapper(lineMap)
        lineAct.GetProperty().SetColor(*color)
        renderer.AddActor(lineAct)

        # draw the cone
        coneSrc = vtk.vtkConeSource()
        coneSrc.SetCenter(end.y, end.z, end.x)
        coneSrc.SetHeight(1)
        coneSrc.SetRadius(0.2)
        coneSrc.SetDirection(self[1], self[2], self[0])
        coneMap = vtk.vtkPolyDataMapper()
        coneMap.SetInput(coneSrc.GetOutput())
        coneAct = vtk.vtkActor()
        coneAct.SetMapper(coneMap)
        coneAct.GetProperty().SetColor(*color)
        renderer.AddActor(coneAct)


__all__ = ("Vector",)
