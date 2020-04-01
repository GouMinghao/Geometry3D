# -*- coding: utf-8 -*-
class GeoBody(object):
    """A base class for geometric objects that provides some common
    methods to work with. In the end, everything is dispatched to
    sgl.calc.* anyway, but it sometimes feels nicer to write it like
    L1.intersection(L2)
    instead of
    intersection(L1, L2)
    """
    def intersection(self, other):
        from .calc import intersection
        return intersection(self, other)

    def distance(self, other):
        from .calc import distance
        return distance(self, other)

    def parallel(self, other):
        from .calc import parallel
        return parallel(self, other)

    def angle(self, other):
        from .calc import angle
        return angle(self, other)

    def orthogonal(self, other):
        from .calc import orthogonal
        return orthogonal(self, other)
