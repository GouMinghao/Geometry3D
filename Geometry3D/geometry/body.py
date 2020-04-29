# -*- coding: utf-8 -*-
"""Geobody module"""
class GeoBody(object):
    """A base class for geometric objects that provides some common
    methods to work with. In the end, everything is dispatched to
    Geometry3D.calc.calc.* anyway, but it sometimes feels nicer to write it like
    L1.intersection(L2)
    instead of
    intersection(L1, L2)
    """
    def intersection(self, other):
        """return the intersection between self and other"""
        from ..calc.intersection import intersection
        return intersection(self, other)

    def distance(self, other):
        """return the distance between self and other"""
        from ..calc.distance import distance
        return distance(self, other)

    def parallel(self, other):
        """return if self and other are parallel to each other"""
        from ..calc.angle import parallel
        return parallel(self, other)

    def angle(self, other):
        """return the angle between self and other"""
        from ..calc.angle import angle
        return angle(self, other)

    def orthogonal(self, other):
        """return if self and other are orthogonal to each other"""
        from ..calc.angle import orthogonal
        return orthogonal(self, other)

