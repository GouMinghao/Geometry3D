from Geometry3D import *
import copy
r = Renderer()
cph0 = Parallelepiped(origin(),x_unit_vector(),y_unit_vector(),z_unit_vector())
cph6 = Parallelepiped(origin(),2 * x_unit_vector(),2 * y_unit_vector(),2 * z_unit_vector())
r.add((cph0,'b',1),normal_length = 0.5)
r.add((cph6,'r',1),normal_length = 0.5)
r.add((intersection(cph6,cph0),'g',2))
print(intersection(cph0,cph6))
r.show()
