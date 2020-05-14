from Geometry3D import *
b = Circle(origin(),y_unit_vector(),10,20)
a = Circle(origin(),x_unit_vector(),10,20)
c = Circle(origin(),z_unit_vector(),10,20)
r = Renderer()
r.add((a,'g',3))
r.add((b,'b',3))
r.add((c,'r',3))



cone = Cone(origin(),3,20 * z_unit_vector(),n=20)
r.add((cone,'y',1),normal_length=0)

cylinder = Cylinder(Point(0,0,20),2,5 * z_unit_vector(),n=15)
r.add((cylinder,'g',1),normal_length=1)

r.show()