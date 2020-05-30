Getting Attributes
==================

Creating Geometries
-------------------

    >>> a = Point(1,1,1)
    >>> d = Point(1,-1,1)
    >>> c = Point(-1,-1,1)
    >>> e = Point(1,1,-1)
    >>> h = Point(1,-1,-1)
    >>> 
    >>> s = Segment(a,c)
    >>> 
    >>> cpg = ConvexPolygon((a,d,h,e))
    >>> 
    >>> cph = Parallelepiped(Point(-1,-1,-1),Vector(2,0,0),Vector(0,2,0),Vector(0,0,2))

Calculating the length
----------------------

    >>> s.length() # 2 * sqrt(2)
    2.8284271247461903
    >>> cpg.length() # 8
    8.0
    >>> cph.length() # 24
    24.0

Calculating the area
--------------------

    >>> cph.area() # 24
    23.999999999999993
    >>> cpg.area() # 4
    3.9999999999999982
    >>> # Floating point calculation error

Calculating the volume
----------------------

    >>> cph.volume() # 8
    7.999999999999995
    >>> volume(cph0) # 8
    7.999999999999995
