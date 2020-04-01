# -*- coding: utf-8 -*-
from ..utils.util import unify_types
import math

import numpy as np
from ..utils.constant import *
from ..utils.vector import Vector

class Point(object):
    """Provides a basic Point in the 3D space"""
    @classmethod
    def origin(cls):
        """Returns the origin (0 | 0 | 0)"""
        return cls(0, 0, 0)
    o = origin

    def __init__(self, *args):
        """Point(a, b, c)
        Point([a, b, c]):
        The point with coordinates (a | b | c)

        Point(Vector):
        The point that you get when you move the origin by the given
        vector. If the vector has coordinates (a | b | c), the point
        will have the coordinates (a | b | c) (as easy as π).
        """
        if len(args) == 1:
            # Initialisation by Vector is also handled by this
            coords = args[0]
        elif len(args) == 3:
            coords = args
        else:
            raise TypeError("Point() takes one or three arguments, not {}"
                    .format(len(args)))
        self.x, self.y, self.z = unify_types(coords)

    def __repr__(self):
        return "Point({}, {}, {})".format(
                self.x,
                self.y,
                self.z,
                )

    def __hash__(self):
        return hash(("Point", round(self.x,SIG_FIGURES), round(self.y,SIG_FIGURES), round(self.z,SIG_FIGURES)))

    def __eq__(self, other):
        """Checks if two Points are equal. Always use == and not 'is'!"""
        if isinstance(other,Point):
            return (abs(self.x - other.x) < EPS_F and
                    abs(self.y - other.y) < EPS_F and
                    abs(self.z - other.z) < EPS_F)
        else:
            return False

    def __getitem__(self, item):
        return (self.x, self.y, self.z)[item]

    def __setitem__(self, item, value):
        setattr(self, "xyz"[item], value)
    
    def tonumpy(self):
        return np.array((self.x,self.y,self.z))

    def pv(self):
        """Return the position vector of the point."""
        return Vector(self.x, self.y, self.z)

    def move(self, v):
        """Return the point that you get when you move self by vector v, self is also moved"""
        if isinstance(v,Vector):
            self.x += v[0]
            self.y += v[1]
            self.z += v[2]
            return Point(self.pv())
        else:
            raise NotImplementedError("The second parameter for move function must be Vector")
    
    def distance(self,other):
        """Return the distance between self and other"""
        return math.sqrt((self.x -other.x) ** 2 + (self.y -other.y) ** 2 + (self.z -other.z) ** 2)

__all__ = ("Point",)
