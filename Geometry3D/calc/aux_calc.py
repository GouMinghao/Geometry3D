# -*- coding: utf-8 -*-
"""
Auxilary Calculation Module. 

Auxilary calculation functions for calculating intersection
"""
import math
from ..geometry.line import Line
from ..geometry.plane import Plane
from ..geometry.point import Point
from ..geometry.segment import Segment
from ..geometry.polygon import ConvexPolygon
from ..geometry.pyramid import Pyramid
from ..geometry.polyhedron import ConvexPolyhedron
from ..geometry.halfline import HalfLine

from ..utils.vector import Vector,x_unit_vector,y_unit_vector
from ..utils.logger import get_main_logger
from ..utils.constant import SMALL_ANGLE

from ..calc.angle import angle

import copy

# import numpy as np
def get_segment_from_point_list(point_list):
    '''
    **Input:**

    - point_list: a list of Points

    **Output:**
    
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
    **Input:**
    
    - v1: Vector
    
    - v2: Vector

    **Output:**
    
    The length of vector that v1 projected on v2
    '''
    if not (isinstance(v1,Vector) or isinstance(v2,Vector)):
        raise TypeError('The type of v1 and v2 must be Vector to get the projection length')
    return v1 * v2 / v2.length()

def get_relative_projection_length(v1,v2):
    '''
    **Input:**

    - v1: Vector
    
    - v2: Vector

    **Output:**
    
    The ratio of length of vector that v1 projected on v2 and the length of v2
    '''
    if not (isinstance(v1,Vector) or isinstance(v2,Vector)):
        raise TypeError('The type of v1 and v2 must be Vector to get relative the projection length')
    return get_projection_length(v1,v2) / v2.length()

def get_segment_convexpolyhedron_intersection_point_set(s,cph):
    '''
    **Input:**
    
    - s: Segment
    
    - cph: ConvexPolyhedron

    **Output:**
    
    A set of intersection points
    '''
    point_set = set()
    for cpg in cph.convex_polygons:
        inter_cpg_s = cpg.intersection(s)
        if inter_cpg_s is None:
            continue
        elif isinstance(inter_cpg_s,Segment):
            continue
        elif isinstance(inter_cpg_s,Point):
            point_set.add(inter_cpg_s)
        else:
            raise TypeError("Bug detected! please contact the author")
    for seg in cph.segment_set:
        inter_s_s = seg.intersection(s)
        if inter_s_s is None:
            continue
        elif isinstance(inter_s_s,Segment):
            continue
        elif isinstance(inter_s_s,Point):
            point_set.add(inter_s_s)
        else:
            raise TypeError("Bug detected! please contact the author")
    return point_set

def get_segment_convexpolygon_intersection_point_set(s,cpg):
    '''
    **Input:**
    
    - s: Segment

    - cpg: ConvexPolygon

    **Output:**
    
    A set of intersection points
    '''
    point_set = set()
        # inter_cpg_s = cpg.intersection(s)
        # if inter_cpg_s is None:
        #     continue
        # elif isinstance(inter_cpg_s,Segment):
        #     continue
        # elif isinstance(inter_cpg_s,Point):
        #     point_set.add(inter_cpg_s)
        # else:
        #     raise TypeError("Bug detected! please contact the author")
    for seg in cpg.segments():
        inter_s_s = seg.intersection(s)
        if inter_s_s is None:
            continue
        elif isinstance(inter_s_s,Segment):
            continue
        elif isinstance(inter_s_s,Point):
            point_set.add(inter_s_s)
        else:
            raise TypeError("Bug detected! please contact the author")
    return point_set

def points_in_a_line(points):
    '''
    **Input:**
    
    - points: Tuple or list of Points

    **Output:**
    
    A set of intersection points
    '''
    if len(points) < 3:
        return True
    else:
        p0 = points[0]
        p1 = points[1]
        l = Line(p0,p1)
        for i in range(2,len(points)):
            if not points[i] in l:
                return False
        return True

def get_halfline_convexpolyhedron_intersection_point_set(h,cph):
    '''
    **Input:**
    
    - h: HalfLine
    
    - cph: ConvexPolyhedron

    **Output:**
    
    A set of intersection points
    '''
    point_set = set()
    for cpg in cph.convex_polygons:
        inter_cpg_h = cpg.intersection(h)
        if inter_cpg_h is None:
            continue
        elif isinstance(inter_cpg_h,Segment):
            continue
        elif isinstance(inter_cpg_h,Point):
            point_set.add(inter_cpg_h)
        else:
            raise TypeError("Bug detected! please contact the author")
    for seg in cph.segment_set:
        inter_s_h = seg.intersection(h)
        if inter_s_h is None:
            continue
        elif isinstance(inter_s_h,Segment):
            continue
        elif isinstance(inter_s_h,Point):
            point_set.add(inter_s_h)
        else:
            raise TypeError("Bug detected! please contact the author")
    return point_set




__all__ = ('get_projection_length','get_relative_projection_length','get_segment_from_point_list','get_segment_convexpolyhedron_intersection_point_set','get_segment_convexpolygon_intersection_point_set','get_halfline_convexpolyhedron_intersection_point_set','points_in_a_line')