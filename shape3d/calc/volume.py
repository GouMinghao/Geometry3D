# -*- coding: utf-8 -*-
from ..geometry.pyramid import Pyramid
from ..geometry.polyhedron import ConvexPolyhedron
from .calc import distance
def volume(arg):
    """Returns the object. This includes
    - Pyramid
    - ConvexPolyhedron
    """
    if isinstance(arg,Pyramid):
        height = distance(arg.point,arg.convex_polygen.plane)
        return 1 / 3 * height * arg.convex_polygen.area()
    elif isinstance(arg,ConvexPolyhedron):
        total_volume = 0
        for pyramid in arg.pyramid_set:
            total_volume += volume(pyramid)
        return total_volume
    else:
        raise ValueError("No attribut volume for this object")