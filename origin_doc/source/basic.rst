Basic usage
===========

sgl is intended to be used as a library in an interactive session with your
Python interpreter. I advise you to use IPython instead of the normal Python
interpreter because it's better for interactive use.

You can use Python 2 or Python 3, whichever you prefer, but if you want to
use the excellent visualisation, you need Python 2 because vtk is not yet
ported to Python 3.

If you have started your interpreter, e.g. by typing :command:`ipython2` in
the command line, you can turn your interpreter into sgl with just one magic
line::

    from sgl import *

Since this line is so short, you can start your python interpreter with this
command directly::

    ipython2 -ic "from sgl import *"

And if you use sgl more often, you can alias it::

    alias sgl='ipython2 -ic "from sgl import *"'

If you are not using IPython 2 you need to replace the command by whatever
interpreter you use, e.g. :command:`python2`.

The bread and butter: Point and Vector
--------------------------------------

Those are the two most basic classes which everything else is built upon. You
can find the detailed documentation here: :class:`~sgl.point.Point` and
:class:`~sgl.vector.Vector`.

There are not many interesting points about Points and Vectors, they more or
less work as you'd expect them to::

    >>> Vector(1, 0, 1) + Vector(2, 2, 0)
    Vector(3, 2, 1)
    >>> Vector(1, 1, 1) * Vector(0, 1, 0)
    1
    >>> Vector(1, 1, 0).cross(Vector(0, 0, 1))
    Vector(1, -1, 0)

Note that you cannot do math on Points, as that makes little to no sense::

    >>> Point(1, 0, 1) + Point(2, 2, 0)
    ...
    TypeError: unsupported operand type(s) for +: 'Point' and 'Point' 

If you want the position vector of a Point, use its :meth:`~sgl.point.Point.pv`
method::

    >>> Point(1, 0, 0).pv()
    Vector(1, 0, 0)
    >>> Point(1, 0, 0).pv() + Vector(1, 0, 0)
    Vector(2, 0, 0)

The bratwurst and fries: Line and Plane
---------------------------------------

:class:`~sgl.line.Line` and :class:`~sgl.plane.Plane` are the more
advanced objects. There are many ways to initialise a Line or a Plane, refer
to the specific objects reference for more information.

The most basic operations are pretty intuitive. If you want to check if a Point
is on a Line or a Plane, just use the *in* operator::

    >>> point = Point(1, 0, 0)
    >>> line = Line(Point(0, 0, 0), Vector(1, 0, 0))
    >>> plane = Plane(Point(0, 0, 0), Vector(0, 0, 1))
    >>> point in line
    True
    >>> point in plane
    True
    >>> line in plane
    True

.. image:: _static/sgl_basic_contains.png

There is not much more to say about the basics. If you want to learn what each
object can do, take a look at the :doc:`reference`. If you want to see more
examples, look at the :doc:`examples`.
