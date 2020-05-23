# -*- coding: utf-8 -*-
"""Plane module"""
from .body import GeoBody
from .point import Point,origin
from .line import Line
from ..utils.solver import solve
from ..utils.vector import Vector,x_unit_vector,y_unit_vector,z_unit_vector
from ..utils.constant import *
class Plane(GeoBody):
    """
    - Plane(Point, Point, Point):
    
    Initialise a plane going through the three given points.

    - Plane(Point, Vector, Vector):
    
    Initialise a plane given by a point and two vectors lying on
    the plane.

    - Plane(Point, Vector):
    
    Initialise a plane given by a point and a normal vector (point
    normal form)

    - Plane(a, b, c, d):
    
    Initialise a plane given by the equation
    ax1 + bx2 + cx3 = d (general form).
    """
    class_level = 2 # the class level of Plane
    
    @classmethod
    def xy_plane(cls):
        """return xy plane which is a Plane"""
        return cls(origin(),z_unit_vector())

    @classmethod
    def yz_plane(cls):
        """return yz plane which is a Plane"""
        return cls(origin(),x_unit_vector())

    @classmethod
    def xz_plane(cls):
        """return xz plane which is a Plane"""
        return cls(origin(),y_unit_vector())
    
    def __init__(self, *args):
        if len(args) == 3:
            a, b, c = args
            if (isinstance(a, Point) and
                isinstance(b, Point) and
                isinstance(b, Point)):
                # for three points we just calculate the vectors AB
                # and AC and continue like we were given two vectors
                # instead
                vab = b.pv() - a.pv()
                vac = c.pv() - a.pv()
            elif (isinstance(a, Point) and
                  isinstance(b, Vector) and
                  isinstance(c, Vector)):
                vab, vac = b, c
            # We need a vector orthogonal to the two given ones so we
            # (the length doesn't matter) so we just use the cross
            # product
            vec = vab.cross(vac)
            self._init_pn(a, vec)
        elif len(args) == 2:
            self._init_pn(*args)
        elif len(args) == 4:
            self._init_gf(*args)
    
    def _init_pn(self, p, normale):
        """Initialise a plane given in the point normal form."""
        self.p = p
        self.n = normale.normalized()

    def _init_gf(self, a, b, c, d):
        """Initialise a plane given in the general form."""
        # We need
        # 1) a normal vector -> given by (a, b, c)
        # 2) a point on the plane -> solve the equation and chose a
        #    "random" point
        solution = solve([[a, b, c, d]])
        self.n = Vector(a, b, c).normalized()
        self.p = Point(*solution(1, 1))

    def __eq__(self, other):
        """Checks if two planes are equal. Two planes can be equal even
        if the representation is different!
        """
        if isinstance(other,Plane):
            return self.p in other and self.n.parallel(other.n)
        else:
            return False

    def __contains__(self, other):
        """Checks if a Point lies on the Plane or a Line is a subset of
        the plane.
        """
        if isinstance(other, Point):
            return abs(other.pv() * self.n - self.p.pv() * self.n) < get_eps()
        elif isinstance(other, Line):
            return Point(other.sv) in self and self.parallel(other)
        elif other.class_level > self.class_level:
            return other.in_(self)
        else:
            raise NotImplementedError("")

    def __repr__(self):
        return "Plane({}, {})".format(self.p, self.n)

    def point_normal(self):
        """Returns (p, n) so that you can build the equation
            _   _   
        E: (x - p) n = 0

        to describe the plane.
        """
        # That's the form we use to store the plane internally,
        # we don't have to calculate anything
        return (self.p.pv(), self.n)

    def general_form(self):
        """Returns (a, b, c, d) so that you can build the equation

        E: ax1 + bx2 + cx3 = d

        to describe the plane.
        """
        # Since this form is just the point-normal-form when you do the
        # multiplication, we don't have to calulate much here
        return (
            self.n[0],
            self.n[1],
            self.n[2],
            self.n * self.p.pv(),
        )

    def __hash__(self):
        """return the hash of a Plane"""
        return hash(("Plane",round(self.n[0],SIG_FIGURES),round(self.n[1],SIG_FIGURES),round(self.n[2],SIG_FIGURES),round(self.n * self.p.pv(),SIG_FIGURES)))
    
    def move(self,v):
        """Return the plane that you get when you move self by vector v, self is also moved"""
        if isinstance(v,Vector):
            self.p.move(v)
            return Plane(self.p,self.n)
        else:
            return NotImplementedError("The second parameter for move function must be Vector")

    def parametric(self):
        """Returns (u, v, w) so that you can build the equation
           _   _    _    _ 
        E: x = u + rv + sw ; (r, s) e R

        to describe the plane (a point and two vectors).
        """
        s = solve([list(self.n) + [0]])
        # Pick a first vector orthogonal to the normal vector
        # there are infinitely many solutions, varying in direction
        # and length, so just choose some values
        v = Vector(*s(1, 1))
        assert v.orthogonal(self.n)
        # Pick a second vector orthogonal to the normal vector and
        # orthogonal to the first vector (v)
        # again, there are infinitely many solutions, varying in length
        s = solve([
            list(self.n) + [0],
            list(v) + [0],
        ])
        w = Vector(*s(1))
        return (self.p.pv(), v, w)
    
    def __neg__(self):
        """Return the negative plane, the normal is the negative normal"""
        return Plane(self.p,-self.n)

xy_plane = Plane.xy_plane
yz_plane = Plane.yz_plane
xz_plane = Plane.xz_plane

__all__ = ("Plane","xy_plane","yz_plane","xz_plane")
