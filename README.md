sgl
===

![Screenshot](/Screenshot.png?raw=true)

sgl is a small Python library that's useful for 3D analytic geometry.
It has representations for Points, Vectors, Lines and Planes and can
do some math on them like calculating distances or visualizing them.

It is mainly intended as a toy for students that learn analytic geometry
in school and is inspired by [Vektoris 3D](http://produkte.kapieren.de/
vektoris3d-raumgeometrie-anschaulich/) that seems to have issues with
a non-german locale. Since I haven't found a nice and free™[1] alternative to
it (maybe I'm just too stupid to use google), I decided to code one by myself,
mainly to control the stuff I did for school.

[1] free as in "free speech" and "free beer", I mean who doesn't like free beer?!?

Requirements
------------

* 400g flour
* 4 eggs
* 100ml fizzy water
* 400ml milk
* 1 small packet of vanilla sugar
* 200g sugar
* 1 apple
* 1 pinch of salt
* [Python](http://www.python.org) 2 or 3 (if you want a visualization,
  you need Python 2)
* <del>[numpy](http://www.numpy.org) and [scipy](http://www.scipy.org)</del>
* optional for the visualization: [vtk](http://www.vtk.org)
* optional for a better experience: [ipython](http://ipython.org)

Documentation
-------------

At http://kingdread.de/sgl/

Installation
------------

Run `python setup.py install` to install the library system-wide. If you want
to install it in "developement mode", use `python setup.py develop`. Of course
you need to replace `python` with the version you want to use, e.g. `python2`
or `python3`.

Usage
-----

The library has no GUI (yet) so the preferred way to work with it is the
interactive Python interpreter (REPL). Just use `from sgl import *` and
you can work with the library:

    $ python2 -ic "from sgl import *" # Replace with ipython if you want to
    >>> Point(0, 1, 1) in Plane(Point(0, 0, 0), Vector(1, 0, 0))
    True
    >>> Plane(Point(0, 0, 0), Vector(1, 0, 0)).parametric()
    (Vector(0, 0, 0), Vector(0.0, 1.0, 1.0), Vector(0.0, -1.0, 1.0))

use `help(...)` to get some help on how to use the objects (documentation
is not yet available).

If you have vtk installed, you can use the `draw()` function to get a nice[2]
interactive representation of your objects

    >>> plane = Plane(Point(0, 0, 0), Vector(1, 0, 0))
    >>> line = Line(Point(0, 0, 5), Vector(1, 0, 0))
    >>> draw([plane, line, plane.intersection(line)])

[2] nice is of course subject to the eyes of the beholder

Todo
----

* Magic
* Examples
* More objects like triangles, circles, rectangles and pyramids, cylinders, ...
* GUI
* Tests

License
-------

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Contact
-------

If you have a bug report, pull request or some other question, please do the
following steps to contact me:

1. Write your request on a red sheet of paper with the dimensions 6.66cm x 6.66cm
2. At full moon, first sign your request with a drop of blood from your right thumb
3. Next place the paper on the ground, text facing towards the sky
4. Acquire 5 candles (not the aromatic ones) and place them around the paper, such
   that they form a pentagram with the paper in the center
5. When the clock hits 0 o'clock, wait until the 6th chime
6. Turn on ["Ja, wenn wir Englein wären" by Frank Zander](http://www.youtube.com/watch?v=9nGIwVF5Re0)
7. Do the chicken dance while shouting "Please accept my sacrifice"
8. With a change of `ln(1) * 1337 * pi / 42` percent, I will get your message.
9. If I don't get and respond to your message, go to step 1.

Alternatively, you can use github to send a pull request or create an issue.
