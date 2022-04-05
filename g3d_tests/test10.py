from Geometry3D import *

vis = Visualizer()

poly1=Sphere(Point(15.592607258702628, -66.15776443481445, 32.0),10,n1=7,n2=3)
poly2=Cylinder(Point(229.78870794537943, -64.86530276807025, 32.0),10,Vector(Point(229.78870794537943, -64.86530276807025, 32.0),Point(214.4889864671277, -64.95762145752087, 32.0)),10)
vis.add((poly1, 'r', 1))
vis.add((poly2, 'b', 2))
vis.show()
print(intersection(poly1,poly2))