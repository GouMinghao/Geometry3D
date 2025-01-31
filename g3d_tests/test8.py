# program in issue 1
from Geometry3D import *

plane1 = ConvexPolygon((Point(61.32, 0.0, 0.58), Point(-0.21, 50.58, -28.91), Point(-0.21, 0.0, -28.91)))
plane2 = ConvexPolygon((Point(-50.21, 20.0, -78.91), Point(-50.21, 20.0, 50.58), Point(111.32, 20.0, 50.58), Point(111.32, 20.0, -78.91)))

inter = intersection(plane1,plane2)
print(inter)

r = Visualizer()
r.add((plane1, 'r',2))
r.add((plane2, 'b',2),normal_length = 0)
r.add((inter, 'g', 5))
r.show()