# -*- coding: utf-8 -*-
from .body import GeoBody
from .point import Point
from ..utils.vector import Vector
from .line import Line
from ..utils.constant import *
class Segment(GeoBody):
    class_level = 3
    """Provides a line segment in 3d space"""
    def __init__(self,a,b):
        if isinstance(a,Point) and isinstance(b,Point):
            self.line = Line(a,b)
            self.start_point = a
            self.end_point = b
        elif isinstance(a,Point) and isinstance(b,Vector):
            self.line = Line(a,b)
            self.start_point = a
            self.end_point = Point(a.pv() + b)
        else:
            raise ValueError('Cannot create segment with type:%s and %s' % (type(a),type(b)))

    def __eq__(self,other):
        return ((self.start_point == other.start_point and self.end_point == other.end_point) or 
        (self.end_point == other.start_point and self.start_point == other.end_point))

    def __repr__(self):
        return "Segment({}, {})".format(self.start_point, self.end_point)

    def __contains__(self, point):
        """Checks if a point lies on a segment"""
        r1 = point in self.line
        r2 = point.x >= (min(self.start_point.x,self.end_point.x) - EPS_F)
        r3 = point.x <= (max(self.start_point.x,self.end_point.x) + EPS_F)
        return r1 and r2 and r3

    def __hash__(self):
        return hash(("Segment", hash(self.start_point) + hash(self.end_point)))

    def parametric(self):
        """Returns (start_point, end_point) so that you can build the information for the segment
        """
        return (self.start_point, self.end_point)

__all__ = ("Segment",)