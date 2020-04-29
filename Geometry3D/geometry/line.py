# -*- coding: utf-8 -*-
"""Line Module"""
from .body import GeoBody
from .point import Point,origin
from ..utils.vector import Vector
from ..utils.constant import *
class Line(GeoBody):
    """
    - Line(Point, Point):
    
    A Line going through both given points.

    - Line(Point, Vector):
    
    A Line going through the given point, in the direction pointed
    by the given Vector.

    - Line(Vector, Vector):
    
    The same as Line(Point, Vector), but with instead of the point
    only the position vector of the point is given.
    """
    class_level = 1 # the class level of Line
    @classmethod
    def x_axis(cls):
        """return x axis which is a Line"""
        return cls(origin(),Point(1,0,0))
    
    @classmethod
    def y_axis(cls):
        """return y axis which is a Line"""
        return cls(origin(),Point(0,1,0))

    @classmethod
    def z_axis(cls):
        """return z axis which is a Line"""
        return cls(origin(),Point(0,0,1))
    
    def __init__(self, a, b):
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

    def __contains__(self, other):
        """Checks if a object lies on a line"""
        if isinstance(other,Point):
            v = other.pv() - self.sv
            return v.parallel(self.dv)
        elif other.class_level > self.class_level:
            return other.in_(self)
        else:
            raise NotImplementedError("")

    def __eq__(self, other):
        """Checks if two lines are equal"""
        if isinstance(other,Line):
            return Point(other.sv) in self and other.dv.parallel(self.dv)
        else:
            return False

    def __hash__(self):
        """Return hash of a Line"""
        return hash(("Line",
        round(self.dv[0],SIG_FIGURES),
        round(self.dv[1],SIG_FIGURES),
        round(self.dv[0] * self.sv[1] - self.dv[1] * self.sv[0],SIG_FIGURES)
        ))
    
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

x_axis = Line.x_axis
y_axis = Line.y_axis
z_axis = Line.z_axis

__all__ = ("Line","x_axis","y_axis","z_axis")
