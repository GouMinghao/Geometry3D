# -*- coding: utf-8 -*-
from .body import GeoBody
from .point import Point
from ..utils.vector import Vector
from .line import Line
from .segment import Segment
from .plane import Plane
from ..utils.constant import *
import math

def get_triangle_area(pa,pb,pc):
    """Input:
    pa: a Point
    pb: a Point
    pc: a Point

    Output:
    The area of the triangle composed by pa, pb and pc
    Heron's formula is used
    """
    a = pa.distance(pb)
    b = pb.distance(pc)
    c = pc.distance(pa)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

class ConvexPolygen(GeoBody):
    """Provides a convex polygen in 3d space"""
    def __init__(self,points,reverse = False, check=False):
        """points: a tuple of points
        The points given shold be in order
        """
        
        self.points = points
        if len(points) < 3:
            raise ValueError('Cannot build a polygen with number of points smaller than 3')
        if reverse:
            self.plane = -Plane(self.points[0],self.points[1],self.points[2])
        else:
            self.plane = Plane(self.points[0],self.points[1],self.points[2])
    
        self.center_point = self._get_center_point()

        self._check_and_sort_points()

        self.segment_list = self._get_segment_list()

    def _get_segment_list(self):
        """Input:
        self

        Output:
        a list of segments
        """
        segment_list = []
        for i in range(len(self.points)):
            index_0 = i
            if i == len(self.points) - 1:
                index_1 = 0
            else:
                index_1 = i + 1
            segment_list.append(Segment(self.points[index_0],self.points[index_1]))
        return segment_list
    
    def _get_center_point(self):
        """Input:
        points: tuple of points

        Output:
        The center point of given points"""
        x,y,z =(0,0,0)
        num_points = len(self.points)
        for point in self.points:
            x += point.x
            y += point.y
            z += point.z
        return Point(float(x) / num_points,float(y) / num_points,float(z) / num_points)
    
    def area(self):
        """
        Input:
        self

        Output:
        The area of the convex polygen
        """
        area = 0
        for i in range(len(self.points)):
            index_0 = i
            if i == len(self.points) - 1:
                index_1 = 0
            else:
                index_1 = i + 1
            area += get_triangle_area(self.center_point,self.points[index_0],self.points[index_1])
        return area

    def _check_and_sort_points(self):
        """input:
        self

        Output:
        True for check passed
        False for check not passed

        This is only a weak check, passing the check doesn't guarantee it is a convex polygen
        """
        the_normal = (self.plane.n).normalized()
        v0 = Vector(self.center_point,self.points[0]).normalized()
        v1 = the_normal.cross(v0)
        angle_point_dict = dict() # dict[angle] = Point
        for point in self.points:
            if not point in self.plane:
                raise ValueError('Convex Check Fails Because {} Is Not On {}'.format(point,self.plane))
            pv = point.pv() - self.center_point.pv()
            y_coordinate = pv * v0
            z_coordinate = pv * v1
            # the range of vector_angle is [0,2*pi)
            vector_angle = math.atan2(z_coordinate,y_coordinate)
            if vector_angle < 0:
                vector_angle += 2 * math.pi
            angle_point_dict[vector_angle] = point
        point_list = [angle_point_dict[angle] for angle in sorted(angle_point_dict)]
        self.points = tuple(point_list)
        return True
    
    def __repr__(self):
        return "ConvexPolygen({})".format(self.points)

    def __contains__(self, obj):
        """Checks if a point or segment lies in a ConvexPolygen"""
        if isinstance(obj,Point):
            r1 = obj in self.plane
            # requirement 1: the point is on the plane
            the_normal = self.plane.n.normalized()
            r2 = True
            # requirement 2: the point is inside the polygen
            for i in range(len(self.points)):
                # check if the point lies in the inside direction of every segment
                index_0 = i
                if i == len(self.points) - 1:
                    index_1 = 0
                else:
                    index_1 = i + 1
                # self.points[index_0] and self.points[index_1] is the i^th segment
                v0 = Vector(self.points[index_0],self.points[index_1])
                v1 = the_normal.cross(v0)
                vec = Vector(self.points[index_0],obj)
                if vec * v1 < - EPS_F:
                    r2 = False
                    break
            return r1 and r2
        
        elif isinstance(obj,Segment):
            return (obj.start_point in self) and (obj.end_point in self) 

    def __neg__(self):
        return ConvexPolygen(self.points,reverse=True)

__all__ = ("ConvexPolygen",)
