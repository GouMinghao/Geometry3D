# -*- coding: utf-8 -*-
"""HalfLine Module"""
from .body import GeoBody
from .point import Point
from .plane import Plane
from ..utils.vector import Vector
from .line import Line
from ..utils.constant import get_eps
from ..utils.logger import get_main_logger
from .segment import Segment
import math
import copy
class HalfLine(GeoBody):
    """
    **Input:**
    
    - HalfLine(Point,Point)

    - HalfLine(Point,Vector)
    """
    class_level = 6 # the class level of HalfLine
    def __init__(self,a,b):
        a = copy.deepcopy(a)
        b = copy.deepcopy(b)
        if isinstance(a,Point) and isinstance(b,Point):
            if a == b:
                raise ValueError("Cannot initialize a HalfLine with two identical Points")
            self.line = Line(a,b)
            self.point = a
            self.vector = Vector(a,b)
        elif isinstance(a,Point) and isinstance(b,Vector):
            if b.length() < get_eps():
                raise ValueError("Cannot initialize a HalfLine with the length of Vector is 0")
            self.line = Line(a,b)
            self.point = a
            self.vector = b
        else:
            raise ValueError('Cannot create segment with type:%s and %s' % (type(a),type(b)))

    def __eq__(self,other):
        return self.point == other.point and (self.vector.normalized()-other.vector.normalized()).length() < get_eps()

    def __repr__(self):
        return "HalfLine({}, {})".format(self.point, self.vector)

    def __contains__(self, other):
        """Checks if a point, segment or halfline lies on a halfline"""
        if isinstance(other,Point):
            r1 = other in self.line
            if r1:
                v1 = Vector(self.point,other)
                return v1 * self.vector > -get_eps() 
            else:
                return False
        if isinstance(other,Segment):
            return other.start_point in self and other.end_point in self
        if isinstance(other, HalfLine):
            return (self.line == other.line) and (other.point in self) and ((self.vector * other.vector) > -get_eps())
        else:
            get_main_logger().warning("Calling type {} in type {} which is always False".format(type(other),type(self)))
            return False

    def in_(self,other):
        """other can be plane or line"""
        if isinstance(other,Line):
            return (self.point in other) and (self.vector.parallel(other.dv))
        elif isinstance(other,Plane):
            return (self.point in other) and (self.vector.orthogonal(other.n))
        else:
            return NotImplementedError("")

    def __hash__(self):
        """return the hash value of the HalfLine"""
        return hash(("HalfLine",
        hash(self.point) + hash(self.vector.normalized()),
        hash(self.point) * hash(self.vector.normalized())
        ))

    def move(self, v):
        """Return the HalfLine that you get when you move self by vector v, self is also moved"""
        if isinstance(v,Vector):
            self.point.move(v)
            return HalfLine(self.point,self.vector)
        else:
            raise NotImplementedError("The second parameter for move function must be Vector")

    def parametric(self):
        """Returns (point, vector) so that you can build the information for the halfline
        """
        return (self.point, self.vector)

    # def length(self):
    #     """retutn the length of the segment"""
    #     return self.start_point.distance(self.end_point)

__all__ = ("HalfLine",)