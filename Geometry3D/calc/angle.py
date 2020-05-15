"""Angle Module"""
import math
from ..geometry.line import Line
from ..geometry.plane import Plane
from ..geometry.point import Point
from ..utils.solver import solve, null
from ..utils.vector import Vector
from ..geometry.segment import Segment
from .acute import acute

def angle(a, b):
    """
    **Input:**
    
    - a: Line/Plane/Plane/Vector

    - b: Line/Line/Plane/Vector


    **Output:**
    
    The angle (in radians) between
    
    - Line/Line
    
    - Plane/Line
    
    - Plane/Plane
    
    - Vector/Vector
    """
    if isinstance(a, Line) and isinstance(b, Line):
        return acute(a.dv.angle(b.dv))

    elif isinstance(a, Line) and isinstance(b, Plane):
        rad = acute(a.dv.angle(b.n))
        # What we are actually calculating is the angle between
        # the normal of the plane and the line, but the normal
        # is 90 from the plane. So the actual angle between a plane
        # a line is 90 - that angle
        return 0.5 * math.pi - rad
    
    elif isinstance(a, Plane) and isinstance(b, Line):
        return angle(b, a)

    elif isinstance(a, Plane) and isinstance(b, Plane):
        return acute(a.n.angle(b.n))

    elif isinstance(a, Vector) and isinstance(b, Vector):
        return acute(a.angle(b))
    
    else:
        raise NotImplementedError("Not implement angle function between %s and %s" % (type(a),type(b)))

def parallel(a, b):
    """
    **Input:**

    - a:Line/Plane/Plane/Vector

    - b:Line/Line/Plane/Vector

    **Output:**
    
    A boolean of whether the two objects are parallel. This can check
    
    - Line/Line
    
    - Plane/Line
    
    - Plane/Plane
    
    - Vector/Vector
    """
    if isinstance(a, Line) and isinstance(b, Line):
        return a.dv.parallel(b.dv)

    elif isinstance(a, Line) and isinstance(b, Plane):
        return a.dv.orthogonal(b.n)
    elif isinstance(a, Plane) and isinstance(b, Line):
        return parallel(b, a)
    
    elif isinstance(a, Plane) and isinstance(b, Plane):
        return a.n.parallel(b.n)
    
    elif isinstance(a, Vector) and isinstance(b, Vector):
        return a.parallel(b)

    else:
        raise NotImplementedError("Not implement parallel function between %s and %s" % (type(a),type(b)))

def orthogonal(a, b):
    """
    **Input:**

    - a:Line/Plane/Plane/Vector

    - b:Line/Line/Plane/Vector

    **Output:**
    
    A boolean of whether the two objects are orthogonal. This can check
    
    - Line/Line
    
    - Plane/Line
    
    - Plane/Plane
    
    - Vector/Vector
    """
    if isinstance(a, Line) and isinstance(b, Line):
        return null(a.dv * b.dv)

    elif isinstance(a, Line) and isinstance(b, Plane):
        return a.dv.parallel(b.n)
    elif isinstance(a, Plane) and isinstance(b, Line):
        return orthogonal(b, a)

    elif isinstance(a, Plane) and isinstance(b, Plane):
        return a.n.orthogonal(b.n)
    elif isinstance(a, Vector) and isinstance(b, Vector):
        return a.orthogonal(b)
    else:
        raise NotImplementedError("Not implement orthogonal function between %s and %s" % (type(a),type(b)))

__all__=('angle','parallel','orthogonal')