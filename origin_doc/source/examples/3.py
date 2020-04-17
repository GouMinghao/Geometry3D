from sgl import *
A = Point(0, 0, 0)
B = Point(3, 0, 0)
C = Point(0, 5, 0)
D = Point(0, 0, 7)

# This could be simplified if we account for the fact that this is a
# right-angled triangle, but we're using the generic way here
base = distance(A, B)
baseline = Line(A, B)
baseheight = distance(baseline, C)
area = 0.5 * base * baseheight
print("Area: %f" % area)

# Again we could simplify here, but we're using the generic way
baseplane = Plane(A, B, C)
height = distance(baseplane, D)
volume = 1.0 / 3 * area * height
print("Volume: %f" % volume)
