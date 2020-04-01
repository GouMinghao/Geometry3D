from sgl import *
line = Line(Point(0, 0, 0), Vector(1, 1, 1))
plane = Plane(Point(0, 0, 0), Vector(1, 1, 1))
vector = Vector(3, 5, 7)
point = intersection(line, plane)

draw([line, plane, vector, point])
