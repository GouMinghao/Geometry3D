from ..geometry.point import Point
from ..geometry.segment import Segment
from ..geometry.polygon import ConvexPolygon
from ..geometry.polyhedron import ConvexPolyhedron
from .arrow import Arrow


class BaseVisualizer(object):
    def __init__(self):
        """
        **Input:**
        - No Input

        Initialize matplotlib
        """
        self.point_set = set()
        self.segment_set = set()
        self.arrow_set = set()

    def add(self, obj, normal_length=0):
        """
        **Input:**

        - obj: a tuple (object,color,size)

        - normal_length: the length of normal arrows for ConvexPolyhedron.
        For other objects, normal_length should be zero.
        If you don't want to show the normal arrows for a ConvexPolyhedron, you can set normal_length to 0.

        object can be Point, Segment, ConvexPolygon or ConvexPolyhedron
        """
        if isinstance(obj[0], Point):
            self.point_set.add(obj)
        elif isinstance(obj[0], Segment):
            self.segment_set.add(obj)
        elif isinstance(obj[0], Arrow):
            self.arrow_set.add(obj)
        elif isinstance(obj[0], ConvexPolygon):
            for point in obj[0].points:
                self.add((point, obj[1], obj[2]))
            for segment in obj[0].segments():
                self.add((segment, obj[1], obj[2]))
            if normal_length > 0:
                cpg = obj[0]
                plane = cpg.plane
                normal = plane.n.normalized()
                array = Arrow(
                    cpg.center_point.x,
                    cpg.center_point.y,
                    cpg.center_point.z,
                    normal[0],
                    normal[1],
                    normal[2],
                    normal_length,
                )
                self.add((array, obj[1], obj[2]))

        elif isinstance(obj[0], ConvexPolyhedron):
            for cpg in obj[0].convex_polygons:
                self.add((cpg, obj[1], obj[2]), normal_length=normal_length)
        else:
            raise ValueError("Cannot add object with type:{}".format(type(obj[0])))

    def show(self):
        pass
