from shape3d import *
origin = Point.origin()

print(origin)

line = Line(origin,Point(1,2,3))
print(line)
print(line.move(Vector.x_unit_vector()))
print(Point(0,0,0.0) == origin)