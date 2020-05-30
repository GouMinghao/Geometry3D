Build-In Functions
==================

`__contains__`
--------------
`__contains__` is used in build-in operator `in`, here are some examples::

    >>> a = origin()
    >>> b = Point(0.5,0,0)
    >>> c = Point(1.5,0,0)
    >>> d = Point(1,0,0)
    >>> e = Point(0.5,0.5,0)
    >>> s1 = Segment(origin(),d)
    >>> s2 = Segment(e,c)
    >>> a in s1
    True
    >>> b in s1
    True
    >>> c in s1
    False
    >>> a in s2
    False
    >>> b in s2
    False
    >>> c in s2
    True
    >>> cpg = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
    >>> a in cpg
    True
    >>> b in cpg
    True
    >>> c in cpg
    False
    >>> s1 in cpg
    True
    >>> s2 in cpg
    False
    >>> 
    >>> r=Renderer()
    >>> r.add((a,'r',10))
    >>> r.add((b,'r',10))
    >>> r.add((c,'r',10))
    >>> r.add((d,'r',10))
    >>> r.add((e,'r',10))
    >>> r.add((s1,'b',5))
    >>> r.add((s2,'b',5))
    >>> r.add((cpg,'g',2))
    >>> r.show()

.. image:: _static/p5.png

`__hash___`
-----------

`__hash__` is used in set, here are some examples::

    >>> a = set()
    >>> a.add(origin())
    >>> a
    {Point(0, 0, 0)}
    >>> a.add(Point(0,0,0))
    >>> a
    {Point(0, 0, 0)}
    >>> a.add(Point(0,0,0.01))
    >>> a
    {Point(0, 0, 0), Point(0.0, 0.0, 0.01)}
    >>>
    >>> b = set()
    >>> b.add(Segment(origin(),Point(1,0,0)))
    >>> b
    {Segment(Point(0, 0, 0), Point(1, 0, 0))}
    >>> b.add(Segment(Point(1.0,0,0),Point(0,0,0)))
    >>> b
    {Segment(Point(0, 0, 0), Point(1, 0, 0))}
    >>> b.add(Segment(Point(0,0,0),Point(0,1,1)))
    >>> b
    {Segment(Point(0, 0, 0), Point(1, 0, 0)), Segment(Point(0, 0, 0), Point(0, 1, 1))}

`__eq__`
--------

`__eq__` is the build-in operator `==`, here are some examples::

    >>> a = origin()
    >>> b = Point(1,0,0)
    >>> c = Point(0,0,0)
    >>> d = Point(2,0,0)
    >>> a == b
    False
    >>> a == c
    True
    >>> 
    >>> s1 = Segment(a,b)
    >>> s2 = Segment(a,b)
    >>> s3 = Segment(b,a)
    >>> s4 = Segment(a,d)
    >>> s1 == s2
    True
    >>> s1 == s3
    True
    >>> s1 == s4
    False
    >>> 
    >>> cpg0 = ConvexPolygon((origin(),Point(1,0,0),Point(0,1,0),Point(1,1,0)))
    >>> cpg1 = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
    >>> cpg0 == cpg1
    True

`__neg__`
---------

`__neg__` is the build-in operator `-`, here are some examples::

    >>> p = Plane(origin(),z_unit_vector())
    >>> p
    Plane(Point(0, 0, 0), Vector(0, 0, 1))
    >>> -p
    Plane(Point(0, 0, 0), Vector(0, 0, -1))
