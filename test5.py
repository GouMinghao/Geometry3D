from Geometry3D import *
import copy
r = Renderer()
cph0 = Parallelepiped(origin(),x_unit_vector(),y_unit_vector(),z_unit_vector())
cph4 = copy.deepcopy(cph0).move(Vector(0.5,0.5,0.5))
r.add((cph0,'b',1),normal_length = 0.5)
r.add((cph4,'r',1),normal_length = 0.5)
r.add((intersection(cph4,cph0),'g',2))
print(intersection(cph0,cph4))
# r.show()
