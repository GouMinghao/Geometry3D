Installation
============

.. note::
    
    Tested on Linux and Windows at the moment.

Prerequisites
-------------

It is assumed that you already have Python 3 installed. If you want graphic
support, you need to manually install `matplotlib`_.

.. _matplotlib: https://matplotlib.org/index.html

System wide installation
------------------------

You can install Geometry3D via pip::

    $ pip install Geometry3D


Alternatively, you can install Geometry3D from source::

    $ git clone http://github.com/GouMinghao/Geometry3D
    $ cd Geometry3D/
    $ sudo pip install .
    # Alternative:
    $ sudo python setup.py install

Note that the Python (or pip) version you use to install Geometry3D must match the
version you want to use Geometry3D with.

Virtualenv installation
-----------------------

Geometry3D can be installed inside a `virtualenv`_ just like any other python package,
though I suggest the use of `virtualenvwrapper`_.

.. _virtualenv: http://virtualenv.readthedocs.org/en/latest/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/
