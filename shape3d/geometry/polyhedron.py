from .body import GeoBody
from .polygen import ConvexPolygen
from .point import Point
from .line import Line
from .segment import Segment
from .plane import Plane
from .pyramid import Pyramid
from ..utils.vector import Vector
from ..utils.constant import *
class ConvexPolyhedron(GeoBody):
    """Provides a convex polyhedron in 3d space"""
    def __init__(self,convex_polygens):
        """Input:
        convex_polygens: tuple of ConvexPolygens

        The correctness of convex_polygens are not checked by this function

        The normal of the convex polygens are not checked not which should be in the outer direction
        """
        self.convex_polygens = list(convex_polygens)
        self.point_set = set()
        self.segment_set = set()
        self.pyramid_set = set()
        
        for convex_polygen in self.convex_polygens:    
            for point in convex_polygen.points:
                self.point_set.add(point)
            for segment in convex_polygen.segment_list:
                self.segment_set.add(segment)
        
        self.center_point = self._get_center_point()

        for i in range(len(self.convex_polygens)):
            convex_polygen = self.convex_polygens[i]
            if Vector(self.center_point,convex_polygen.plane.p) * convex_polygen.plane.n < -EPS_F:
                self.convex_polygens[i] = - convex_polygen
            self.pyramid_set.add(Pyramid(convex_polygen,self.center_point))
        if not self._check_normal():
            raise ValueError('Check Normal Fails For The Convex Polyhedron')
        if not self._euler_check():
            raise ValueError('Check for the number of vertices, faces and edges')

    def _euler_check(self):
        number_points = len(self.point_set)
        number_segments = len(self.segment_set)
        number_polygens = len(self.convex_polygens)
        print('V:{},E:{},F:{}'.format(number_points,number_segments,number_polygens))
        return number_points - number_segments + number_polygens == 2

    def _check_normal(self):
        """return True if all the polygens' normals point to the outside"""
        for convex_polygen in self.convex_polygens:
            if Vector(self.center_point,convex_polygen.plane.p) * convex_polygen.plane.n < -EPS_F:
                return False
        return True
    
    def _get_center_point(self):
        """Input:
        self

        Output:
        The center point of this point set
        """
        x,y,z = 0,0,0
        num_points = len(self.point_set)
        for point in self.point_set:
            x += point.x
            y += point.y
            z += point.z
        return Point(x / num_points,y / num_points, z / num_points)
    
    def __repr__(self):
        return "ConvecPolyhedron\npyramid set:{}\npoint set:{}".format(self.pyramid_set,self.point_set)

    def __contains__(self,point):
        """Input:
        point: a Point

        Output:
        Whether the polyhedron contains the point
        """
        for polygen in self.convex_polygens:
            direction_vector = Vector(polygen.center_point,point)
            if direction_vector * polygen.plane.n > - EPS_F:
                return False
        return True
        

        