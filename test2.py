from Geometry3D import *
cph0 = Parallelepiped(origin(),x_unit_vector(),y_unit_vector(),z_unit_vector())
p = Plane(Point(0.5,0.5,0.5),Vector(1,1,1))
cpg = intersection(cph0,p)
r = Renderer()

r.add((cph0,'r',1),normal_length = 0)
r.add((cpg,'b',1),normal_length=0)

r.show()
