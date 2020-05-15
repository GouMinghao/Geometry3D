"""Acute Module"""
# -*- coding: utf-8 -*-
import math
def acute(rad):
    """
    **Input:**

    - rad: A angle in rad.

    **Output:**

    If the given angle is >90 (pi/2), return the opposite angle.
    
    Return the angle else.
    """
    if rad > 0.5 * math.pi:
        rad = math.pi - rad
    return rad