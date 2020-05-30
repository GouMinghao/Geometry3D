# -*- coding: utf-8 -*-
"""Distance Module"""
import math
from ..geometry.line import Line
from ..geometry.plane import Plane
from ..geometry.point import Point
from ..geometry.segment import Segment
from ..geometry.polygon import ConvexPolygon
from ..geometry.polyhedron import ConvexPolyhedron
from ..utils.solver import solve, null
from ..utils.vector import Vector

from .acute import acute
from .angle import angle, parallel, orthogonal
from .intersection import intersection

def distance(a, b):
    """
    **Input:**

    - a: Point/Line/Line/Plane/Plane

    - b: Point/Point/Line/Point/Line

    **Output:**

    Returns the distance between two objects. This includes
    
    - Point/Point
    
    - Line/Point
    
    - Line/Line
    
    - Plane/Point
    
    - Plane/Line
    """
    if isinstance(a, Point) and isinstance(b, Point):
        # The distance between two Points A and B is just the length of
        # the vector AB
        return Vector(a, b).length()

    elif isinstance(a, Point) and isinstance(b, Line):
        # To get the distance between a point and a line, we place an
        # auxiliary plane P. P is orthogonal to the line and contains
        # the point. To achieve this, we just use the direction vector
        # of the line as the normal vector of the plane.
        aux_plane = Plane(a, b.dv)
        # We then calculate the intersection of the auxiliary plane and
        # the line
        foot = intersection(aux_plane, b)
        # And finally the distance between the point and the
        # intersection point, which can be reduced to a Point-Point
        # distance
        return distance(a, foot)
    elif isinstance(a, Line) and isinstance(b, Point):
        return distance(b, a)

    elif isinstance(a, Line) and isinstance(b, Line):
        # To get the distance between two lines, we just use the formula
        #        _   _    _
        # d = | (q - p) * n |
        # where n is a vector orthogonal to both lines and with length 1!
        # We can achieve this by using the normalized cross product
        normale = a.dv.cross(b.dv).normalized()
        return abs((b.sv - a.sv) * normale)

    elif isinstance(a, Point) and isinstance(b, Plane):
        # To get the distance between a point and a plane, we just take
        # a line that's orthogonal to the plane and goes through the
        # point
        aux_line = Line(a, b.n)
        # We then get the intersection point...
        foot = intersection(aux_line, b)
        # ...and finally the distance
        return distance(a, foot)
    elif isinstance(a, Plane) and isinstance(b, Point):
        return distance(b, a)

    elif isinstance(a, Line) and isinstance(b, Plane):
        if parallel(a, b):
            # If the line is parallel, every point has the same distance
            # to the plane, so we just pick one point and calculate its
            # distance
            return distance(Point(a.sv), b)
        # If they are not parallel, they will eventually intersect, so
        # the distance is 0
        return 0.0
    elif isinstance(a, Plane) and isinstance(b, Line):
        return distance(b, a)
    else:
        raise NotImplementedError("Not implemented distance between {} and {}".format(type(a),type(b)))

__all__ = ('distance',)