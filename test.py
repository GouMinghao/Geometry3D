# bug list
# 3. deal with situation when two polygens are on the same plane
# 4. the function of intersection of ConvexPolyge and Segment should be changed 
 
# might be bug list
# 2. when the accuracy fails

# todo list



from shape3d import *
# from shape3d.render import Renderer
import time


import logging
from logging.config import dictConfig
logging_config = dict(
    version=1,
    formatters=
    {
        'f':
        {
            'format':'%(asctime)s %(levelname)-9s%(message)s'
        },
        'f1':
        {
            'format':'%(asctime)s %(levelname)-10s%(message)s'
        }
    },
    handlers={
        'h': 
        {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG
        }
    },
    root=
    {
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
)

dictConfig(logging_config)
logger = logging.getLogger()

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

t3 = time.time()
cpg0 = ConvexPolygen((a,d,h,e))
t4 = time.time()
logger.info('create polygen time:%f' %(t4 - t3,))
cpg1 = ConvexPolygen((a,e,f,b))
cpg2 = ConvexPolygen((c,b,f,g))
cpg3 = ConvexPolygen((c,g,h,d))
cpg4 = ConvexPolygen((a,b,c,d))
cpg5 = ConvexPolygen((e,h,g,f))

t5 = time.time()
# cph0 = ConvexPolyhedron((cpg0,cpg1,cpg2,cpg3,cpg4,cpg5))
cph0 = Parallelepiped(Point(-1,-1,-1),Vector(2,0,0),Vector(0,2,0),Vector(0,0,2))
t6 = time.time()
logger.info('create polyhedron time:%f' %(t6 - t5,))
cpg12 = ConvexPolygen((e,c,h))
cpg13 = ConvexPolygen((e,f,c))
cpg14 = ConvexPolygen((c,f,g))
cpg15 = ConvexPolygen((h,c,g))
cpg16 = ConvexPolygen((h,g,f,e))
cph1 = ConvexPolyhedron((cpg12,cpg13,cpg14,cpg15,cpg16))

# print(cph0)
# print(volume(cph0))

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

cpg6 = ConvexPolygen((a1,d1,h1,e1))
cpg7 = ConvexPolygen((a1,e1,f1,b1))
cpg8 = ConvexPolygen((c1,b1,f1,g1))
cpg9 = ConvexPolygen((c1,g1,h1,d1))
cpg10 = ConvexPolygen((a1,b1,c1,d1))
cpg11 = ConvexPolygen((e1,h1,g1,f1))
cph2 = ConvexPolyhedron((cpg6,cpg7,cpg8,cpg9,cpg10,cpg11))

# print(cph1)
# print(volume(cph1))
t7 = time.time()
cph3 = intersection(cph0,cph2)
t8 = time.time()
logger.info('calculate intersection time:%f' %(t8 - t7,))

cph4 = intersection(cph1,cph2)
logger.info('volume:%f' % (cph2.volume(),))
t9 = time.time()
logger.info('calculate volume time:%f' %(t9 - t8,))
# t2 = time.time()

logger.info('total time:{}'.format(t9 - t1))
r = Renderer()
r.add((cph0,'r',1),normal_length = 0)
r.add((cph1,'r',1),normal_length = 0)
r.add((cph2,'g',1),normal_length = 0)
r.add((cph3,'b',3),normal_length = 0.5)
r.add((cph4,'y',3),normal_length = 0.5)


r.show()

# cp1 = ConvexPolygen((d,c,b))
# print(cp1.area)

# cp2 = ConvexPolygen((a,b,c,d))
# print(cp2.area)

# cp2 = ConvexPolygen((a,b,c,d))
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