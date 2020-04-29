# shape3d


![Screenshot](/Screenshot.png?raw=true)

shape3d is a small Python library that's useful for 3D analytic geometry.
It has representations for Points, Vectors, Lines, Planes, Segments, Convex Polygens and Convex Polyhedrons and can do some calculations such as the distance, length, area and volume.

All the geometries are convex so intersection of objects is supported.

The library also implements a naive renderer based on matplotlib.

Some of the code comes from [sgl](https://github.com/Kingdread/sgl) whose author is really humorous.


## Requirements

* [Python](http://www.python.org) 3 (python2 is not tested)
* no requirements, it's written in pure python and standard library. 
* Matplotlib is needed if you want to use the renderer.
* optional for a better experience: [ipython](http://ipython.org)

## Documentation
No documentation yet.

## Installation
```bash
pip install shape3d
```

## Usage

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


## Todo

Examples  
More objects like Full intersection support

## License

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

## Contact
gouminghao@gmail.com