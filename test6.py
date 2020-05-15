from Geometry3D import *
import copy

b = Circle(origin(),y_unit_vector(),10,20)
a = Circle(origin(),x_unit_vector(),10,20)
c = Circle(origin(),z_unit_vector(),10,20)
r = Renderer()
r.add((a,'g',3))
r.add((b,'b',3))
r.add((c,'r',3))

s1 = Sphere(Point(20,0,0),10,n1=12,n2=5)
s2 = copy.deepcopy(s1).move(Vector(10,2,-3.9))
s3 = intersection(s1,s2)

r.add((s1,'r',1))
r.add((s2,'b',1))
r.add((s3,'y',3))

cone = Cone(origin(),3,20 * z_unit_vector(),n=20)
r.add((cone,'y',1),normal_length=0)

cylinder = Cylinder(Point(0,0,20),2,5 * z_unit_vector(),n=15)
r.add((cylinder,'g',1),normal_length=1)

r.show()