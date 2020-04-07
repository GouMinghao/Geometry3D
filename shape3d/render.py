"""model to visualize some geometries"""
from .geometry.point import Point
# from .vector import Vector
# from .line import Line
from .geometry.segment import Segment
# from .plane import Plane
from .geometry.polygen import ConvexPolygen
from .geometry.polyhedron import ConvexPolyhedron
from matplotlib import pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from .utils.constant import *
class Arrow():
    def __init__(self,x,y,z,u,v,w,length):
        self.x = x
        self.y = y
        self.z = z
        self.u = u
        self.v = v
        self.w = w
        self.length = length

    def __eq__(self,other):
        return (
            abs(self.x - other.x) < EPS_F and
            abs(self.y - other.y) < EPS_F and
            abs(self.z - other.z) < EPS_F and 
            abs(self.u - other.u) < EPS_F and
            abs(self.v - other.v) < EPS_F and
            abs(self.w - other.w) < EPS_F and
            abs(self.length - other.length) < EPS_F)
    
    def __hash__(self):
        return hash((
            round(self.x,SIG_FIGURES),
            round(self.y,SIG_FIGURES),
            round(self.z,SIG_FIGURES),
            round(self.u,SIG_FIGURES),
            round(self.v,SIG_FIGURES),
            round(self.w,SIG_FIGURES),
            round(self.length,SIG_FIGURES)
        ))
    
    def get_tuple(self):
        return (self.x,self.y,self.z,self.u,self.v,self.w,self.length)
        

class Renderer():
    """ Renderer module to visualize geometries"""
    def __init__(self):
        """Input:
        None

        initialize matplotlib
        """
        self.point_set = set()
        self.segment_set = set()
        self.arrow_set = set()
    def show(self):
        """Input:
        legend: boolean, if True legend will be drawn

        """
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        for point_tuple in self.point_set:
            point = point_tuple[0]
            color = point_tuple[1]
            size = point_tuple[2]
            ax.scatter(point.x,point.y,point.z,c=color,s=size)
        
        for segment_tuple in self.segment_set:
            segment = segment_tuple[0]
            color = segment_tuple[1]
            size = segment_tuple[2]
            x = [segment.start_point.x,segment.end_point.x]
            y = [segment.start_point.y,segment.end_point.y]
            z = [segment.start_point.z,segment.end_point.z]
            ax.plot(x,y,z,color=color,linewidth=size)

        for arrow_tuple in self.arrow_set:
            x,y,z,u,v,w,length = arrow_tuple[0].get_tuple()
            color = arrow_tuple[1]
            size = arrow_tuple[1]
            ax.quiver(x,y,z,u,v,w,color = color,length = length)

        plt.show()
        
    def add(self,obj,normal_length = 0):
        """Input
        
        obj: a tuple (object,color,size)
        object can be Point, Segment, ConvexPolygen or ConvexPolyhedron
        """
        if isinstance(obj[0],Point):
            self.point_set.add(obj)
        elif isinstance(obj[0],Segment):
            self.segment_set.add(obj)
        elif isinstance(obj[0],Arrow):
            self.arrow_set.add(obj)
        elif isinstance(obj[0],ConvexPolygen):
            for point in obj[0].points:
                self.add((point,obj[1],obj[2]))
            for segment in obj[0].segments():
                self.add((segment,obj[1],obj[2]))
            if normal_length > 0:
                cpg = obj[0]
                plane = cpg.plane
                normal = plane.n.normalized()
                array = Arrow(cpg.center_point.x,cpg.center_point.y,cpg.center_point.z,normal[0],normal[1],normal[2],normal_length)
                self.add((array,obj[1],obj[2]))
    
        elif isinstance(obj[0],ConvexPolyhedron):
            for cpg in obj[0].convex_polygens:
                self.add((cpg,obj[1],obj[2]),normal_length = normal_length)
        else:
            raise ValueError('Cannot add object with type:{}'.format(type(obj[0])))