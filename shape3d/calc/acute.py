# -*- coding: utf-8 -*-
import math
def acute(rad):
    """If the given angle is >90° (pi/2), return the opposite angle"""
    if rad > 0.5 * math.pi:
        rad = math.pi - rad
    return rad