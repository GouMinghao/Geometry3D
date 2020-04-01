# -*- coding: utf-8 -*-
from .body import GeoBody
from .point import Point
from ..utils.vector import Vector
from .line import Line
from .segment import Segment
from .polygen import ConvexPolygen

class Pyramid(GeoBody):
    """Provides a pyramid in 3d space"""
    def __init__(self,cp,p):
        """Input:
        cp: a ConvexPolygen
        p: a Point
        """
        if isinstance(cp,ConvexPolygen) and isinstance(p,Point):
            self.convex_polygen = cp
            self.point = p
            if self.point in self.convex_polygen.plane:
                raise ValueError('Cannot create Pyramid with point on the polygen plane')
        else:
            raise ValueError('Cannot create Pyramid with type:%s and %s' % (type(a),type(b)))
    
    def __repr__(self):
        return "Pyramid({}, {})".format(self.convex_polygen, self.point)

__all__ = ("Pyramid",)
