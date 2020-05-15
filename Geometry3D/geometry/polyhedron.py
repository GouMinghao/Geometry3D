"""Polyhedron Module"""
from .body import GeoBody
from .polygen import ConvexPolygen,Parallelogram,Circle,get_circle_point_list
from .point import Point
from .line import Line
from .segment import Segment
from .plane import Plane
from .pyramid import Pyramid
from ..utils.vector import Vector,x_unit_vector,y_unit_vector,z_unit_vector
from ..utils.constant import *
from ..utils.logger import get_main_logger
import copy
class ConvexPolyhedron(GeoBody):
    class_level = 5 # the class level of ConvexPolyhedron
    """
    **Input:**
    
    - convex_polygens: tuple of ConvexPolygens

    **Output:**

    - ConvexPolyhedron
    
    - The correctness of convex_polygens are checked According to Euler's formula.

    - The normal of the convex polygens are checked and corrected which should be toward the outer direction
    """
    @classmethod
    def Parallelepiped(cls,base_point,v1,v2,v3):
        """
        A special function for creating Parallelepiped

        **Input:**

        - base_point: a Point

        - v1, v2, v3: three Vectors

        **Output:**

        - A parallelepiped which is a ConvexPolyhedron instance.
        """
        if isinstance(base_point,Point) and isinstance(v1,Vector) and isinstance(v2,Vector) and isinstance(v3,Vector):
            if v1.length() == 0 or v2.length == 0 or v3.length == 0:
                raise ValueError("The length for the three vector shouldn't be zero")
            elif v1.parallel(v2) or v1.parallel(v3) or v2.parallel(v3):
                raise ValueError("The three vectors shouldn't be parallel to each other")
            else:
                p_diag = copy.deepcopy(base_point).move(v1).move(v2).move(v3)
                rectangle0=Parallelogram(base_point,v1,v2)
                rectangle1=Parallelogram(base_point,v2,v3)
                rectangle2=Parallelogram(base_point,v1,v3)
                rectangle3=Parallelogram(p_diag,-v1,-v2)
                rectangle4=Parallelogram(p_diag,-v2,-v3)
                rectangle5=Parallelogram(p_diag,-v1,-v3)
                return cls((rectangle0,rectangle1,rectangle2,rectangle3,rectangle4,rectangle5))

        else:
            raise TypeError("Parallelepiped should be initialized with Point, Vector, Vector and Vector, but the given types are %s, %s, %s and %s" %(type(base_point),type(v1),type(v2),type(v3)))

    @classmethod
    def Sphere(cls,center,radius,n1=10,n2=3):
        """
        A special function for creating the inscribed polyhedron of a sphere 

        **Input:**

        - center: The center of the sphere

        - radius: The radius of the sphere

        - n1=10: The number of Points on a longitude circle

        - n2=3: The number sections of a quater latitude circle 

        **Output:**

        - An inscribed polyhedron of the given sphere.
        """
        import copy
        import math
        cpg_list = []
        mc = get_circle_point_list(center = center,normal = z_unit_vector(),radius = radius,n=n1) # medium circle
        top_point = copy.deepcopy(center).move(radius * z_unit_vector())
        bottom_point = copy.deepcopy(center).move(-radius * z_unit_vector())
        # heights=[]
        # radii = []
        tc = [] # top circles
        bc = [] # bottom circles
        for i in range(n2-1):
            angle_i = math.pi / 2 / n2 *(i+1) 
            height_i=radius * math.sin(angle_i)
            r_i=radius * math.cos(angle_i)
            tc.append(get_circle_point_list(
                center = copy.deepcopy(center).move(height_i * z_unit_vector()),
                normal = z_unit_vector(),
                radius = r_i,
                n=n1
            ))
            bc.append(get_circle_point_list(
                center = copy.deepcopy(center).move(-height_i * z_unit_vector()),
                normal = z_unit_vector(),
                radius = r_i,
                n=n1
            ))
        for i in range(n1):
            start = i
            end = (i + 1) % n1 
            cpg_list.append(ConvexPolygen((mc[start],mc[end],tc[0][end],tc[0][start])))
            cpg_list.append(ConvexPolygen((mc[start],mc[end],bc[0][end],bc[0][start])))
            for j in range(1,n2-1):
                cpg_list.append(ConvexPolygen((tc[j-1][start],tc[j-1][end],tc[j][end],tc[j][start])))
                cpg_list.append(ConvexPolygen((bc[j-1][start],bc[j-1][end],bc[j][end],bc[j][start])))
            cpg_list.append(ConvexPolygen((top_point,tc[n2-2][end],tc[n2-2][start])))
            cpg_list.append(ConvexPolygen((bottom_point,bc[n2-2][end],bc[n2-2][start])))
        return cls(tuple(cpg_list))
        # return cpg_list

    @classmethod
    def Cylinder(cls,circle_center,radius,height_vector,n=10):
        """
        A special function for creating the inscribed polyhedron of a sphere 

        **Input:**

        - circle_center: The center of the bottom circle

        - radius: The radius of the bottom circle

        - height_vector: The Vector from the bottom circle center to the top circle center 

        - n=10: The number of Points on the bottom circle

        **Output:**

        - An inscribed polyhedron of the given cylinder.
        """
        import copy
        top_point = copy.deepcopy(circle_center).move(height_vector)
        # print(top_point)
        bottom_circle = Circle(center=circle_center,normal=height_vector,radius=radius,n=n)
        bottom_circle_point_list = get_circle_point_list(center=circle_center,normal=height_vector,radius=radius,n=n)

        top_circle = Circle(center=top_point,normal=height_vector,radius=radius,n=n)
        top_circle_point_list = get_circle_point_list(center=top_point,normal=height_vector,radius=radius,n=n)
        cpg_list = [top_circle,bottom_circle]
        for i in range(len(top_circle_point_list)):
            start = i
            end = (i + 1) % len(top_circle_point_list)
            cpg_list.append(ConvexPolygen((top_circle_point_list[start],top_circle_point_list[end],bottom_circle_point_list[end],bottom_circle_point_list[start])))
        return cls(tuple(cpg_list))

    @classmethod
    def Cone(cls,circle_center,radius,height_vector,n=10):
        """
        A special function for creating the inscribed polyhedron of a sphere 

        **Input:**

        - circle_center: The center of the bottom circle

        - radius: The radius of the bottom circle

        - height_vector: The Vector from the bottom circle center to the top circle center 

        - n=10: The number of Points on the bottom circle

        **Output:**

        - An inscribed polyhedron of the given cone.
        """
        import copy
        top_point = copy.deepcopy(circle_center).move(height_vector)
        # print(top_point)
        circle = Circle(center=circle_center,normal=height_vector,radius=radius,n=n)
        circle_point_list = get_circle_point_list(center=circle_center,normal=height_vector,radius=radius,n=n)
        cpg_list = [circle]
        for i in range(len(circle_point_list)):
            start = i
            end = (i + 1) % len(circle_point_list)
            cpg_list.append(ConvexPolygen((top_point,circle_point_list[start],circle_point_list[end])))
        return cls(tuple(cpg_list))

    def __init__(self,convex_polygens):
        self.convex_polygens = list(copy.deepcopy(convex_polygens))
        # self.convex_polygens = list(convex_polygens)
        self.point_set = set()
        self.segment_set = set()
        self.pyramid_set = set()
        
        for convex_polygen in self.convex_polygens:    
            for point in convex_polygen.points:
                self.point_set.add(point)
            for segment in convex_polygen.segments():
                self.segment_set.add(segment)
        
        self.center_point = self._get_center_point()

        for i in range(len(self.convex_polygens)):
            convex_polygen = self.convex_polygens[i]
            if Vector(self.center_point,convex_polygen.plane.p) * convex_polygen.plane.n < -get_eps():
                self.convex_polygens[i] = - convex_polygen
            self.pyramid_set.add(Pyramid(convex_polygen,self.center_point,direct_call=False))
        if not self._check_normal():
            raise ValueError('Check Normal Fails For The Convex Polyhedron')
        if not self._euler_check():
            get_main_logger().critical('V:{} E:{} F:{}'.format(len(self.point_set),len(self.segment_set),len(self.convex_polygens)))
            raise ValueError('Check for the number of vertices, faces and edges fails, the polyhedron may not be closed')

    def _euler_check(self):
        number_points = len(self.point_set)
        number_segments = len(self.segment_set)
        number_polygens = len(self.convex_polygens)
        return number_points - number_segments + number_polygens == 2

    def _check_normal(self):
        """return True if all the polygens' normals point to the outside"""
        for convex_polygen in self.convex_polygens:
            if Vector(self.center_point,convex_polygen.plane.p) * convex_polygen.plane.n < -get_eps():
                return False
        return True
    
    def _get_center_point(self):
        """
        **Input:**
        
        - self

        **Output:**

        - The center point of this point set
        """
        x,y,z = 0,0,0
        num_points = len(self.point_set)
        for point in self.point_set:
            x += point.x
            y += point.y
            z += point.z
        return Point(x / num_points,y / num_points, z / num_points)
    
    def __repr__(self):
        return "ConvexPolyhedron({})".format(self.point_set)

    def __contains__(self,other):
        """
        **Input:**

        - point: a Object

        **Output:**

        - Whether the polyhedron contains the point
        """
        if isinstance(other,Point):
            for polygen in self.convex_polygens:
                direction_vector = Vector(polygen.center_point,other)
                if direction_vector * polygen.plane.n > get_eps():
                    return False
            return True

        elif isinstance(other,Segment):
            return ((other.start_point in self) and (other.end_point in self))
        
        elif isinstance(other,ConvexPolygen):
            for point in other.points:
                if not point in self:
                    return False
            return True
        else:
            raise NotImplementedError("")

    def __eq__(self,other):
        if isinstance(other,ConvexPolyhedron):
            return (hash(self) == hash(other))
        else:
            return False

    def move(self,v):
        """Return the ConvexPolyhedron that you get when you move self by vector v, self is also moved"""
        if isinstance(v,Vector):
            convexpolygen_list = []
            for convexpolygen in self.convex_polygens:
                convexpolygen_list.append(convexpolygen.move(v))
            self.convex_polygens = tuple(convexpolygen_list)   
            self.point_set = set()
            self.segment_set = set()
            self.pyramid_set = set()
            for convex_polygen in self.convex_polygens: 
                for point in convex_polygen.points:
                    self.point_set.add(point)
                for segment in convex_polygen.segments():
                    self.segment_set.add(segment)
        
            self.center_point = self._get_center_point()

            for i in range(len(self.convex_polygens)):
                convex_polygen = self.convex_polygens[i]
                if Vector(self.center_point,convex_polygen.plane.p) * convex_polygen.plane.n < -get_eps():
                    self.convex_polygens[i] = - convex_polygen
                self.pyramid_set.add(Pyramid(convex_polygen,self.center_point,direct_call=False))
            if not self._check_normal():
                raise ValueError('Check Normal Fails For The Convex Polyhedron')
            if not self._euler_check():
                get_main_logger().critical('V:{} F:{} E:{}'.format(len(self.point_set),len(self.segment_set),len(self.convex_polygens)))
                raise ValueError('Check for the number of vertices, faces and edges fails, the polyhedron may not be closed')
            return ConvexPolyhedron(self.convex_polygens)
        else:
            raise NotImplementedError("The second parameter for move function must be Vector")

    def _get_polygen_hash_sum(self):
        """return the sum of hash value of all the ConvexPolygens"""
        hash_sum = 0
        for polygen in self.convex_polygens:
            hash_sum += hash(polygen)
        return hash_sum

    def _get_point_hash_sum(self):
        """return the sum of hash value of all the points"""
        hash_sum = 0
        for point in self.point_set:
            hash_sum += hash(point)
        return hash_sum

    # the hash function is not accurate
    # in some extreme case, this function may fail
    # which means it's vulnerable to attacks.
    def __hash__(self):
        """return the hash value of the ConvexPolyhedron"""
        return hash((
            "ConvexPolyhedron",
            round(self._get_polygen_hash_sum(),SIG_FIGURES),
            round(self._get_point_hash_sum(),SIG_FIGURES)
        ))

    #no in_ function

    def length(self):
        """return the total length of the polyhedron"""
        l = 0
        for segment in self.segment_set:
            l += segment.length()
        return l

    def area(self):
        """return the total area of the polyhedron"""
        a = 0
        for polygen in self.convex_polygens:
            a += polygen.area()
        return a

    def volume(self):
        """return the total volume of the polyhedron"""
        v = 0
        for pyramid in self.pyramid_set:
            v += pyramid.volume()
        return v

Parallelepiped = ConvexPolyhedron.Parallelepiped
Cone = ConvexPolyhedron.Cone
Sphere = ConvexPolyhedron.Sphere
Cylinder = ConvexPolyhedron.Cylinder

__all__=("ConvexPolyhedron","Parallelepiped","Cone","Sphere","Cylinder")