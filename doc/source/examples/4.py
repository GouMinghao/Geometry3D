from sgl import *
plane = Plane(Point(2, 3, 5), Vector(42, 0, 0))

print("General: %ix1 + %ix2 + %ix3 = %i" % plane.general_form())
print("Parametric: x = %s + r * %s + s * %s ; r,s e R" % plane.parametric())
