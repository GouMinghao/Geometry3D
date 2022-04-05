"""Arrow Module for Renderer"""
from ..utils.constant import get_eps,get_sig_figures
class Arrow():
    """Arrow Class"""
    def __init__(self,x,y,z,u,v,w,length):
        self.x = x
        self.y = y
        self.z = z
        self.u = u
        self.v = v
        self.w = w
        self.length = length

    def __eq__(self,other):
        return (
            abs(self.x - other.x) < get_eps() and
            abs(self.y - other.y) < get_eps() and
            abs(self.z - other.z) < get_eps() and 
            abs(self.u - other.u) < get_eps() and
            abs(self.v - other.v) < get_eps() and
            abs(self.w - other.w) < get_eps() and
            abs(self.length - other.length) < get_eps())
    
    def __hash__(self):
        return hash((
            round(self.x,get_sig_figures()),
            round(self.y,get_sig_figures()),
            round(self.z,get_sig_figures()),
            round(self.u,get_sig_figures()),
            round(self.v,get_sig_figures()),
            round(self.w,get_sig_figures()),
            round(self.length,get_sig_figures())
        ))
    
    def get_tuple(self):
        """return the tuple expression of the arrow"""
        return (self.x,self.y,self.z,self.u,self.v,self.w,self.length)