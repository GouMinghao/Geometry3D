from Geometry3D import *
import copy
r = Renderer()
cph0 = Parallelepiped(origin(),x_unit_vector(),y_unit_vector(),z_unit_vector())
cph4 = Parallelepiped(Point(0.5,0.5,0.8),Vector(0,-1,1),Vector(0,1,1),Vector(1,0,1))
r.add((cph0,'b',1),normal_length = 0.5)
r.add((cph4,'r',1),normal_length = 0.5)
r.add((intersection(cph4,cph0),'g',2))
print(intersection(cph0,cph4))
r.show()
