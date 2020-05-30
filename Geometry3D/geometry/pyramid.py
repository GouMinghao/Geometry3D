# -*- coding: utf-8 -*-
"""Pyramid Module"""
from .body import GeoBody
from .point import Point
from ..utils.vector import Vector
from .line import Line
from .polygon import ConvexPolygon
from ..utils.logger import get_main_logger
# Pyramid is an auxilary geometry
# Direct use is not suggested
# Calculation of pyramids should be applied using ConvexPolygon

class Pyramid(GeoBody):
    """
    **Input:**
    
    - cp: a ConvexPolygon
    
    - p: a Point
    """
    def __init__(self,cp,p,direct_call=True):
        if direct_call:
            get_main_logger().warning('Pyramid is an auxilary geometry. Direct use is not suggested. Consider using ConvexPolyhedron instead.')
        if isinstance(cp,ConvexPolygon) and isinstance(p,Point):
            self.convex_polygon = cp
            self.point = p
            if self.point in self.convex_polygon.plane:
                raise ValueError('Cannot create Pyramid with point on the polygon plane')
        else:
            raise ValueError('Cannot create Pyramid with type:%s and %s' % (type(cp),type(p)))
    
    def __repr__(self):
        return "Pyramid({}, {})".format(self.convex_polygon, self.point)
    
    def height(self):
        """ return the height of the pyramid"""
        p0 = self.convex_polygon.points[0]
        return abs(Vector(p0,self.point)*self.convex_polygon.plane.n.normalized())
    
    def volume(self):
        """ return the volume of the pryamid"""
        h = self.height()
        return 1 / 3 * h * self.convex_polygon.area()

__all__ = ("Pyramid",)
