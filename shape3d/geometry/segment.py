# -*- coding: utf-8 -*-
from .body import GeoBody
from .point import Point
from .plane import Plane
from ..utils.vector import Vector
from .line import Line
from ..utils.constant import *
import math

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

    def in_(self,other):
        """other can be plane or line"""
        if isinstance(other,Line):
            return (self.start_point in other) and (self.end_point in other)
        elif isinstance(other,Plane):
            return (self.start_point in other) and (self.end_point in other)
        else:
            return NotImplementedError("")

    def __hash__(self):
        return hash(("Segment",
        hash(self.start_point) + hash(self.end_point),
        hash(self.start_point) * hash(self.end_point)
        ))

    def __getitem__(self,idx):
        return (self.start_point,self.end_point)[idx]

    def __setitem__(self,idx,value):
        if idx == 0:
            self.start_point = value
        elif idx == 1:
            self.end_point = value
        else:
            raise IndexError("Index out of range")

    def move(self, v):
        """Return the point that you get when you move self by vector v, self is also moved"""
        if isinstance(v,Vector):
            self.start_point.move(v)
            self.end_point.move(v)
            return Segment(self.start_point,self.end_point)
        else:
            raise NotImplementedError("The second parameter for move function must be Vector")

    def parametric(self):
        """Returns (start_point, end_point) so that you can build the information for the segment
        """
        return (self.start_point, self.end_point)

    def length(self):
        return self.start_point.distance(self.end_point)

__all__ = ("Segment",)