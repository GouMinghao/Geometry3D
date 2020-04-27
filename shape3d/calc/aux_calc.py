# -*- coding: utf-8 -*-
import math
from ..geometry.line import Line
from ..geometry.plane import Plane
from ..geometry.point import Point
from ..geometry.segment import Segment
from ..geometry.polygen import ConvexPolygen
from ..geometry.pyramid import Pyramid
from ..geometry.polyhedron import ConvexPolyhedron

from ..utils.vector import Vector
from ..utils.logger import get_main_logger
import copy

# import numpy as np
def get_segment_from_point_list(point_list):
    '''Input:
    point_list: a list of Points

    Output:
    The longest segment between the points
    '''
    if len(point_list) < 2:
        raise ValueError('The length of point list mush be no less than 2')
    p0 = point_list[0]
    p1 = point_list[1]
    v0 = Vector(p0,p1)
    relative_length_list =[0,1]
    for i in range(2,len(point_list)):
        pi = point_list[i]
        vi = Vector(p0,pi)
        if not vi.parallel(v0):
            raise ValueError('The points are not on a line')
        relative_length_list.append(get_relative_projection_length(vi,v0))
    get_main_logger().debug('relative length list:{}'.format(relative_length_list))
    p_start = copy.deepcopy(p0).move(v0 * min(relative_length_list))
    p_end = copy.deepcopy(p0).move(v0 * max(relative_length_list))
    return Segment(p_start,p_end)

def get_projection_length(v1,v2):
    '''
    Input:
    v1: Vector
    v2: Vector

    Output:
    The length of vector that v1 projected on v2
    '''
    if not (isinstance(v1,Vector) or isinstance(v2,Vector)):
        raise TypeError('The type of v1 and v2 must be Vector to get the projection length')
    return v1 * v2 / v2.length()

def get_relative_projection_length(v1,v2):
    '''
    Input:
    v1: Vector
    v2: Vector

    Output:
    The ratio of length of vector that v1 projected on v2 and the length of v2
    '''
    if not (isinstance(v1,Vector) or isinstance(v2,Vector)):
        raise TypeError('The type of v1 and v2 must be Vector to get relative the projection length')
    return get_projection_length(v1,v2) / v2.length()

__all__ = ('get_projection_length','get_relative_projection_length','get_segment_from_point_list')