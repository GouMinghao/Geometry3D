# -*- coding: utf-8 -*-
"""Util Module"""
from decimal import Decimal
from fractions import Fraction

def unify_types(items):
    """Promote all items to the same type. The resulting type is the
    "most valueable" that an item already has as defined by the list
    (top = least valueable):
    
    - int
    
    - float
    
    - decimal.Decimal
    
    - fractions.Fraction
    
    - user defined
    """
    type_values = {
        Fraction: 1,
        Decimal: 2,
        float: 3,
        int: 4,
    }
    types = []
    for item in items:
        for type_, value in type_values.items():
            if isinstance(item, type_):
                types.append((value, type_))
                break
        else:
            types.append((0, type(item)))
    result_type = min(types)[1]
    return [result_type(i) for i in items]

