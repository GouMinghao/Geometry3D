# bug list
# 3. deal with situation when two polygons are on the same plane
# 4. the function of intersection of ConvexPolyge and Segment should be changed 
 
# might be bug list
# 2. when the accuracy fails

# todo list



from Geometry3D import *
import time

set_log_level('INFO')
logger = get_main_logger()
t1 = time.time()
o = Point(0,0,0)
t2 = time.time()
logger.info('create point time:%f' %(t2 - t1,))

a = Point(1,1,1)
b = Point(-1,1,1)
c = Point(-1,-1,1)
d = Point(1,-1,1)
e = Point(1,1,-1)
f = Point(-1,1,-1)
g = Point(-1,-1,-1)
h = Point(1,-1,-1)
# set_log_level('DEBUG')
t3 = time.time()
cpg0 = ConvexPolygon((a,d,h,e))
t4 = time.time()
logger.info('create polygon time:%f' %(t4 - t3,))
cpg1 = ConvexPolygon((a,e,f,b))
cpg2 = ConvexPolygon((c,b,f,g))
cpg3 = ConvexPolygon((c,g,h,d))
cpg4 = ConvexPolygon((a,b,c,d))
cpg5 = ConvexPolygon((e,h,g,f))
# set_log_level('WARNING')
t5 = time.time()
cph0 = Parallelepiped(Point(-1,-1,-1),Vector(2,0,0),Vector(0,2,0),Vector(0,0,2))
t6 = time.time()
logger.info('create polyhedron time:%f' %(t6 - t5,))
cpg12 = ConvexPolygon((e,c,h))
cpg13 = ConvexPolygon((e,f,c))
cpg14 = ConvexPolygon((c,f,g))
cpg15 = ConvexPolygon((h,c,g))
cpg16 = ConvexPolygon((h,g,f,e))
cph1 = ConvexPolyhedron((cpg12,cpg13,cpg14,cpg15,cpg16))

# set_log_level('INFO')

a1 = Point(1.5,1.5,1.5)
b1 = Point(-0.5,1.5,1.5)
c1 = Point(-0.5,-0.5,1.5)
d1 = Point(1.5,-0.5,1.5)
e1 = Point(1.5,1.5,-0.5)
# f1 = Point(-0.5,1.5,-0.5)
# g1 = Point(-0.5,-0.5,-0.5)
f1 = Point(-0.2,1.5,-0.5)
g1 = Point(-0.2,-0.5,-0.5)
h1 = Point(1.5,-0.5,-0.5)

cpg6 = ConvexPolygon((a1,d1,h1,e1))
cpg7 = ConvexPolygon((a1,e1,f1,b1))
cpg8 = ConvexPolygon((c1,b1,f1,g1))
cpg9 = ConvexPolygon((c1,g1,h1,d1))
cpg10 = ConvexPolygon((a1,b1,c1,d1))
cpg11 = ConvexPolygon((e1,h1,g1,f1))
cph2 = ConvexPolyhedron((cpg6,cpg7,cpg8,cpg9,cpg10,cpg11))

# print(cph1)
# print(volume(cph1))
t7 = time.time()
cph3 = intersection(cph0,cph2)
t8 = time.time()
logger.warning('calculate intersection time:%f' %(t8 - t7,))

cph4 = intersection(cph1,cph2)
logger.info('volume:%f' % (cph2.volume(),))
t9 = time.time()
logger.info('calculate volume time:%f' %(t9 - t8,))
# t2 = time.time()

logger.critical('total time:{}'.format(t9 - t1))
r = Renderer()
r.add((cph0,'r',1),normal_length = 0)
r.add((cph1,'r',1),normal_length = 0)
r.add((cph2,'g',1),normal_length = 0)
r.add((cph3,'b',3),normal_length = 0.5)
r.add((cph4,'y',3),normal_length = 0.5)


r.show()

# cp1 = ConvexPolygon((d,c,b))
# print(cp1.area)

# cp2 = ConvexPolygon((a,b,c,d))
# print(cp2.area)

# cp2 = ConvexPolygon((a,b,c,d))
# p1 = Pyramid(cp2,e)
# print(volume(p1))
# l1 = Line(o,a)
# l2 = Line(o,b)

# v1 = Vector(o,a)

# s1 = Segment(o,v1)
# print(s1)
# s2 = Segment(a,b)
# print(s2)
# print(o in s2)
# print(a in s2)
# print(b in s2)
# print(Point(1.5,2.5,3.5) in s2)

# a = origin()
# b = Point(0.5,0,0)
# c = Point(1.5,0,0)
# d = Point(1,0,0)
# e = Point(0.5,0.5,0)
# s1 = Segment(origin(),d)
# s2 = Segment(e,c)
# a in s1
# b in s1
# c in s1
# a in s2
# b in s2
# c in s2
# cpg = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
# a in cpg
# b in cpg
# c in cpg
# s1 in cpg
# s2 in cpg

# r=Renderer()
# r.add((a,'r',10))
# r.add((b,'r',10))
# r.add((c,'r',10))
# r.add((d,'r',10))
# r.add((e,'r',10))
# r.add((s1,'b',5))
# r.add((s2,'b',5))
# r.add((cpg,'g',2))
# r.show()

# a = origin()
# b = Point(1,0,0)
# c = Point(0,0,0)
# d = Point(2,0,0)
# a == b
# a == c

# s1 = Segment(a,b)
# s2 = Segment(a,b)
# s3 = Segment(b,a)
# s4 = Segment(a,d)
# s1 == s2
# s1 == s3
# s1 == s4

# cpg0 = ConvexPolygon((origin(),Point(1,0,0),Point(0,1,0),Point(1,1,0)))
# cpg1 = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
# cpg0 == cpg1

# p = Plane(origin(),z_unit_vector())
# p
# -p
