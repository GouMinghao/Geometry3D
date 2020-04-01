# -*- coding: utf-8 -*-
from .body import GeoBody
from .point import Point
from ..utils.vector import Vector

class Line(GeoBody):
    """Provides a line in 3d space"""
    def __init__(self, a, b):
        """Line(Point, Point):
        A Line going through both given points.

        Line(Point, Vector):
        A Line going through the given point, in the direction pointed
        by the given Vector.

        Line(Vector, Vector):
        The same as Line(Point, Vector), but with instead of the point
        only the position vector of the point is given.
        """
        # We're storing the position vector, so if a point is given we
        # need to convert it first
        if isinstance(a, Point):
            a = a.pv()
        # Support vector
        self.sv = a
        if isinstance(b, Vector):
            self.dv = b
        elif isinstance(b, Point):
            # We just take the vector AB as the direction vector
            self.dv = b.pv() - self.sv

        if self.dv == Vector.zero():
            raise ValueError("Invalid Line, Vector(0 | 0 | 0)")
        # sv is the point and dv is the direction

    def __repr__(self):
        """expresion of a line"""
        return "Line(sv={},dv={})".format(self.sv, self.dv)

    def __contains__(self, point):
        """Checks if a point lies on a line"""
        if isinstance(point,Point):
            v = point.pv() - self.sv
            return v.parallel(self.dv)
        else:
            raise NotImplementedError("")

    def __eq__(self, other):
        """Checks if two lines are equal"""
        if isinstance(other,Line):
            return Point(other.sv) in self and other.dv.parallel(self.dv)
        else:
            return False

    ########################
    # needs to be modified #
    ########################
    def __hash__(self):
        return hash("Line",self.sv,self.dv)
    
    def move(self, v):
        """Return the line that you get when you move self by vector v, self is also moved"""
        if isinstance(v,Vector):
            self.sv[0] += v[0]
            self.sv[1] += v[1]
            self.sv[2] += v[2]
            return Line(self.sv,self.dv)
        else:
            raise NotImplementedError("The second parameter for move function must be Vector")

    def parametric(self):
        """Returns (s, u) so that you can build the equation for the line
           _   _    _
        g: x = s + ru ; r e R
        """
        return (self.sv, self.dv)

__all__ = ("Line",)
