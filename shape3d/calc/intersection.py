# -*- coding: utf-8 -*-
import math
from ..geometry.line import Line
from ..geometry.plane import Plane
from ..geometry.point import Point
from ..geometry.segment import Segment
from ..geometry.polygen import ConvexPolygen
from ..geometry.pyramid import Pyramid
from ..geometry.polyhedron import ConvexPolyhedron

from ..utils.solver import solve, null
from ..utils.vector import Vector
from ..utils.logger import get_main_logger

from .acute import acute
from .angle import angle, parallel, orthogonal
from .aux_calc import get_segment_from_point_list

def intersection(a, b):
    """Return the intersection between two objects.
    Input:
    a: GeoBody
    b: GeoBody
    
    Output:
    intersection
    maybe None or GeoBody
    The intersection operation is closed.
    """
    get_main_logger().debug('Calling intersection with {} and {}'.format(a,b))
    # There are totally 6 * 6 = 36 situations
    # Point
    if isinstance(a,Point) and isinstance(b,Point):
        return inter_point_point(a,b)
    elif isinstance(a,Point) and isinstance(b,Line):
        return inter_point_line(a,b)
    elif isinstance(a,Line) and isinstance(b,Point):
        return inter_point_line(b,a)
    elif isinstance(a,Point) and isinstance(b,Plane):
        return inter_point_plane(a,b)
    elif isinstance(a,Plane) and isinstance(b,Point):
        return inter_point_plane(b,a)
    elif isinstance(a,Point) and isinstance(b,Segment):
        return inter_point_segment(a,b)
    elif isinstance(a,Segment) and isinstance(b,Point):
        return inter_point_segment(b,a)
    elif isinstance(a,Point) and isinstance(b,ConvexPolygen):
        return inter_point_convexpolygen(a,b)
    elif isinstance(a,ConvexPolygen) and isinstance(b,Point):
        return inter_point_convexpolygen(b,a)
    elif isinstance(a,Point) and isinstance(b,ConvexPolyhedron):
        return inter_point_convexpolyhedron(a,b)
    elif isinstance(a,ConvexPolyhedron) and isinstance(b,Point):
        return inter_point_convexpolyhedron(b,a)
    # Line
    elif isinstance(a, Line) and isinstance(b, Line):
        return inter_line_line(a,b)
    elif isinstance(a, Line) and isinstance(b, Plane):
        return inter_line_plane(a,b)
    elif isinstance(a, Plane) and isinstance(b, Line):
        return inter_line_plane(b,a)
    elif isinstance(a, Line) and isinstance(b, Segment):
        return inter_line_segment(a,b)
    elif isinstance(a, Segment) and isinstance(b, Line):
        return inter_line_segment(b,a)
    elif isinstance(a, Line) and isinstance(b,ConvexPolygen):
        return inter_line_convexpolygen(a,b)
    elif isinstance(a, ConvexPolygen) and isinstance(b, Line):
        return inter_line_convexpolygen(b,a)
    elif isinstance(a, Line) and isinstance(b, ConvexPolyhedron):
        return inter_line_convexpolyhedron(a,b)
    elif isinstance(a, ConvexPolyhedron) and isinstance(b, Line):
        return inter_line_convexpolyhedron(b,a)
    elif isinstance(a, Plane) and isinstance(b, Plane):
        # if you solve
        # a x1 + b x2 + c x3 = d
        # e x1 + f x2 + g x3 = h
        # you will get infinitely many solutions (if the planes are
        # intersecting). All those solutions are points on the 
        # intersection line. So we just chose two solutions, i.e.
        # two points, and lay a line through both of these.
        solution = solve([
            list(a.n) + [a.n * a.p.pv()],
            list(b.n) + [b.n * b.p.pv()],
        ])
        if not solution:
            return None
        # Choose two arbitrary points/solutions
        p1, p2 = Point(solution(1)), Point(solution(2))
        return Line(p1.pv(), p2.pv() - p1.pv())

    elif isinstance(a,Segment) and isinstance(b,Segment):
        inter = intersection(a,b)
        if inter is None:
            # parallel
            return None
        elif isinstance(inter,Line):
            pass
            # on the same line:
            # it seems that there are so many cases
        else:
            # point
            if (inter in a) and (inter in b):
                return inter
    elif isinstance(a,Segment) and isinstance(b,ConvexPolygen):
        # two situations. The segment on the plane and the segment not on the plane.
        p = intersection(a.line,b.plane)
        if isinstance(p,Point):
            if p is None:
                return None
            elif (not p in a) or (not p in b):
                return None
            else:
                return p
        
        elif isinstance(p,Line):
            if (a.start_point in b) and (a.end_point in b):
                return a
            else:
                intersection_point_set = set()
                #######################
                # not implemented now #
                #######################
        elif p is None:
            return None
    
    elif isinstance(a,ConvexPolygen) and isinstance(b,Segment):
        # Segment in ConvexPolygen needs to be handled
        return intersection(b,a)
    
    elif isinstance(a,ConvexPolyhedron) and isinstance(b,ConvexPolyhedron):
        return ConvexPolyhedron_intersection(a,b)
    
    elif isinstance(a,ConvexPolyhedron) and isinstance(b,ConvexPolygen):
        return ConvexPolyhedron_ConvexPolygen_intersection(a,b)

    elif isinstance(a,ConvexPolygen) and isinstance(b,ConvexPolyhedron):
        return ConvexPolyhedron_ConvexPolygen_intersection(b,a)
    
    raise NotImplementedError("not implement intersecting %s with %s"%(type(a),type(b)))

def ConvexPolyhedron_intersection(cph1,cph2):
    """Input:
    cph1: a ConvexPolyhedron
    cph2: a ConvexPolyhefron

    Output:
    a Point, Segment, ConvexPolygen or ConvexPolyhedron
    the intersection part of cph1 and cph2
    """
    if not (isinstance(cph1,ConvexPolyhedron) and isinstance(cph2,ConvexPolyhedron)):
        raise ValueError('convex polyhedron intersection should be called with two ConvexPolyhedron')
    cpg_set = set()
    for cpg in cph1.convex_polygens:
        inter_cpg = ConvexPolyhedron_ConvexPolygen_intersection(cph2,cpg)
        if inter_cpg is not None:
            cpg_set.add(inter_cpg)
    for cpg in cph2.convex_polygens:
        inter_cpg = ConvexPolyhedron_ConvexPolygen_intersection(cph1,cpg)
        if inter_cpg is not None:
            cpg_set.add(inter_cpg)
    return ConvexPolyhedron(tuple(cpg_set))

def ConvexPolyhedron_ConvexPolygen_intersection(cph,cpg):
    """Input:
    cph: a ConvexPolyhedron
    cpg: a ConvexPolygen
     
    Output:
    a Point, Segment or ConvexPolygen
    the intersection part of cph and cpg
    """
    point_set = set()
    # points in ConvexPolygen
    for point in cpg.points:
        if point in cph:
            point_set.add(point)
    # intersection points of polygen segment and convexpolyhedron convexpolygen
    for segment in cpg.segments():
        for polygen in cph.convex_polygens:
            point = intersection(polygen,segment)
            if point is not None:
                if point in cpg:
                    point_set.add(point)
    # intersection points of convexpolyhedron segmetn and polygen
    for polygen in cph.convex_polygens:
        for segment in polygen.segments():
            point = intersection(segment,cpg)
            if point is not None:
                if point in cpg:
                    point_set.add(point)
    if len(point_set) < 3:
        return None
    # sort the point in __init__ in ConvexPolygen class
    return ConvexPolygen(tuple(point_set))

def inter_point_point(p1,p2):
    """intersection function for Point and Point
    input:
    p1: Point
    p2: Point

    output:
    intersection
    """
    if p1==p2:
        return p1
    else:
        return None

def inter_point_line(p,l):
    """intersection function for Point and Line
    input:
    p: Point
    l: Line

    output:
    intersection
    """
    if p in l:
        return p
    else:
        return None

def inter_point_plane(pnt,pln):
    """intersection function for Point and Plane
    input:
    pnt: Point
    pln: Plane

    output:
    intersection
    """
    if pnt in pln:
        return pnt
    else:
        return None

def inter_point_segment(p,s):
    """intersection function for Point and Segment
    input:
    p: Point
    s: Segment

    output:
    intersection
    """
    if p in s:
        return p
    else:
        return None

def inter_point_convexpolygen(p,cpg):
    """intersection function for Point and ConvexPolygen
    input:
    p: Point
    cpg: ConvexPolygen

    output:
    intersection
    """
    if p in cpg:
        return p
    else:
        return None

def inter_point_convexpolyhedron(p,cph):
    """intersection function for Point and ConvexPolyhedron
    input:
    p: Point
    cph: ConvexPolyhedron

    output:
    intersection
    """
    if p in cph:
        return p
    else:
        return None
    
def inter_line_line(l1,l2):
    """intersection function for Line and Line
    input:
    l1: Line
    l2: Line

    output:
    intersection
    """
    if l1 == l2:
        return l1
    else:
        # For the line-line intersection, we have to solve
        # s1 + λ u1 = t1 + μ v1
        # s2 + λ u2 = t2 + μ v2
        # s3 + λ u3 = t3 + μ v3
        # rearrange a bit, and you get
        solution = solve([
            [l1.dv[0], -l2.dv[0], l2.sv[0] - l1.sv[0]],
            [l1.dv[1], -l2.dv[1], l2.sv[1] - l1.sv[1]],
            [l1.dv[2], -l2.dv[2], l2.sv[2] - l1.sv[2]],
        ])
        # No intersection
        if not solution:
            return None
        # We get λ and μ, we need to pick one and plug it into the
        # right equation
        lmb, mu = solution()
        lmb = float(lmb)
        # could've chosen b.sv + mu * b.dv instead, it doesn't matter
        # as they will point (pun intended) to the same point.
        return Point(l1.sv + lmb * l1.dv)

def inter_line_plane(l,p):
    """intersection function for Line and Plane 
    input:
    l: Line
    p: Plane

    output:
    intersection
    """
    # the line can be contained in the plane, in this case the whole
    # line is the intersection
    if l in p:
        return l
    # if they are parallel, there is no intersection
    elif parallel(l, p):
        return None
    # Given the plane in general form, if we insert the line
    # coordinate by coordinate we get
    # a (s1 + μ u1) + b (s2 + μ u2) + c (s3 + μ u3) = d
    # where s is the support vector of the line
    #       u is the direction vector of the line
    #       μ is the parameter
    # rearrange and solve for the parameter:
    mu = (p.n * p.p.pv() - p.n * l.sv) / (p.n * l.dv)
    mu = float(mu)
    return Point(l.sv + mu * l.dv)

def inter_line_segment(l,s):
    """intersection function for Line and Segment 
    input:
    l: Line
    s: Segment

    output:
    intersection
    """
    inter = intersection(l,s.line)
    if inter is None:
        return None
    elif isinstance(inter,Line):
        return s
    elif isinstance(inter,Point):
        return intersection(inter,s)
    else:
        raise TypeError("Bug detected! please contact the author")

def inter_line_convexpolygen(l,cpg):
    """intersection function for Line and ConvexPolygen 
    input:
    l: Line
    cpg: ConvexPolygen

    output:
    intersection
    """
    inter = intersection(l,cpg.plane)
    if inter is None:
        return None
    elif isinstance(inter,Line):
        point_set = set()
        for segment in cpg.segments():
            inter_l_s = intersection(segment,l)
            if inter_l_s is None:
                continue
            elif isinstance(inter_l_s,Point):
                point_set.add(inter_l_s)
            elif isinstance(inter_l_s,Segment):
                return inter_l_s
            else:
                raise TypeError("Bug detected! please contact the author")
        if len(point_set) == 1:
            point_list = list(point_set)
            return point_list[0]
        if len(point_set) == 2:
            point_list = list(point_set)
            return Segment(point_list[0],point_list[1])
        else:
            get_main_logger().error("len: %d" %(len(point_set,)))
            raise TypeError("Bug detected! please contact the author")
    elif isinstance(inter,Point):
        return intersection(inter,cpg)
    else:
        raise TypeError("Bug detected! please contact the author")

def inter_line_convexpolyhedron(l,cph):
    """intersection function for Line and ConvexPolygen 
    input:
    l: Line
    cpg: ConvexPolygen

    output:
    intersection
    """
    set_point = set()
    for cpg in cph.convex_polygens:
        inter_cpg_l = intersection(l,cpg)
        if isinstance(inter_cpg_l,Segment):
            return inter_cpg_l
        elif isinstance(inter_cpg_l,Point):
            set_point.add(inter_cpg_l)
        elif inter_cpg_l is None:
            pass
        else:
            raise TypeError("Bug detected! please contact the author")
    if len(set_point) == 0:
        return None
    elif len(set_point) == 1:
        return list(set_point)[0]
    elif len(set_point) >= 2:
        list_point = list(set_point)
        return get_segment_from_point_list(list_point)
        
__all__=('intersection',)