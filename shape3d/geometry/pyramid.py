# -*- coding: utf-8 -*-
from .body import GeoBody
from .point import Point
from ..utils.vector import Vector
from .line import Line
from .polygen import ConvexPolygen

# Pyramid is an auxilary geometry
# Direct use is not suggested
# Calculation of pyramids should be applied using ConvexPolygen

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
    
    def height(self):
        p0 = self.convex_polygen.points[0]
        return abs(Vector(p0,self.point)*self.convex_polygen.plane.n.normalized())
    
    def volume(self):
        h = self.height()
        return 1 / 3 * h * self.convex_polygen.area()

__all__ = ("Pyramid",)
