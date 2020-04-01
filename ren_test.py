from sgl import *
from sgl.render import Renderer
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

a = Point(1,1,1)
o = Point(0,0,0)

r = Renderer()
r.add((a,'r',4))
r.add((o,'b',20))
r.show()