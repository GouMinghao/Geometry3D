# -*- coding: utf-8 -*-
"""Volume module"""
from ..geometry.pyramid import Pyramid
from ..geometry.polyhedron import ConvexPolyhedron
from .distance import distance

def volume(arg):
    """
    **Input:**

    - arg: Pyramid or ConvexPolyhedron

    **Output:**

    Returns the object volume. This includes
    
    - Pyramid
    
    - ConvexPolyhedron
    """
    if isinstance(arg,Pyramid):
        height = distance(arg.point,arg.convex_polygon.plane)
        return 1 / 3 * height * arg.convex_polygon.area()
    elif isinstance(arg,ConvexPolyhedron):
        total_volume = 0
        for pyramid in arg.pyramid_set:
            total_volume += volume(pyramid)
        return total_volume
    else:
        raise ValueError("No attribut volume for this object")

__all__=('volume',)