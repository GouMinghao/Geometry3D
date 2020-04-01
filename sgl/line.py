# -*- coding: utf-8 -*-
from .body import GeoBody
from .point import Point
from .vector import Vector

class Line(GeoBody):
    """Provides a line in 3d space"""
    def __init__(self, a, b):
        """Line(Point, Point):
        A Line going through both given points.

        Line(Point, Vector):
        A Line going through the given point, in the direction pointed
        by the given Vector.

        Line(Vector, Vector):
        The same as Line(Point, Vector), but with instead of the point
        only the position vector of the point is given.
        """
        # We're storing the position vector, so if a point is given we
        # need to convert it first
        if isinstance(a, Point):
            a = a.pv()
        # Support vector
        self.sv = a
        if isinstance(b, Vector):
            self.dv = b
        elif isinstance(b, Point):
            # We just take the vector AB as the direction vector
            self.dv = b.pv() - self.sv

        if self.dv == Vector.zero():
            raise ValueError("Invalid Line, Vector(0 | 0 | 0)")

    def __repr__(self):
        return "Line({}, {})".format(self.sv, self.dv)

    def __contains__(self, point):
        """Checks if a point lies on a line"""
        v = point.pv() - self.sv
        return v.parallel(self.dv)

    def __eq__(self, other):
        """Checks if two lines are equal"""
        return Point(other.sv) in self and other.dv.parallel(self.dv)

    def parametric(self):
        """Returns (s, u) so that you can build the equation for the line
           _   _    _
        g: x = s + ru ; r e R
        """
        return (self.sv, self.dv)

    def draw(self, renderer, box, color=(0, 0, 1)):
        """Draw the plane on the given renderer (vtk). box should have
        the shape ((minx, miny, minz), (maxx, maxy, maxz)) and it
        defines the cuboid in which the plane should be drawn.

        color defaults to blue.
        """
        from .plane import Plane
        min_, max_ = box
        # Define the boundary planes
        boundaries = [
            Plane(Point(max_[0], 0, 0), Vector(1, 0, 0)),
            Plane(Point(min_[0], 0, 0), Vector(1, 0, 0)),
            Plane(Point(0, max_[1], 0), Vector(0, 1, 0)),
            Plane(Point(0, min_[1], 0), Vector(0, 1, 0)),
            Plane(Point(0, 0, max_[2]), Vector(0, 0, 1)),
            Plane(Point(0, 0, min_[2]), Vector(0, 0, 1)),
        ]
        intersections = filter(None, map(self.intersection, boundaries))
        # If a line is a subset of a plane, we get Lines as results. We
        # need to remove them or they will fuck everything up.
        intersections = filter(lambda x: not isinstance(x, Line),
                intersections)
        # Filter out the out-of-bounds points and remove duplicates
        def in_bounds(point):
            return (
                min_[0] <= point.x <= max_[0] and
                min_[1] <= point.y <= max_[1] and
                min_[2] <= point.z <= max_[2]
            )
        intersections = list(set(filter(in_bounds, intersections)))
        # If everything went right, we will have 2 points left
        if len(intersections) != 2:
            # This happens if the line has no part within the given
            # cuboid (or it just touches a corner)
            return
        A, B = intersections

        import vtk
        source = vtk.vtkLineSource()
        # Coordinate axes are labelled differently in maths and 3d
        # graphics programming
        source.SetPoint1(A.y, A.z, A.x)
        source.SetPoint2(B.y, B.z, B.x)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInput(source.GetOutput())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(*color)
        renderer.AddActor(actor)

__all__ = ("Line",)
