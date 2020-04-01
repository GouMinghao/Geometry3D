Installation
============

.. note::
    
    Only tested on Linux at the moment.

Prerequisites
-------------

It is assumed that you already have Python installed. If you want graphic
support, you manually need to install `vtk`_ since it is not found via pip.
Please check their website or your distributions documentation on how to
install vtk.

.. _vtk: http://www.vtk.org

System wide installation
------------------------

You can install sgl system wide, just like any other python package::

    $ git clone http://github.com/Kingdread/sgl
    $ cd sgl/
    $ sudo pip install .
    # Alternative:
    $ sudo python setup.py install

Note that the Python (or pip) version you use to install sgl must match the
version you want to use sgl with.

Virtualenv installation
-----------------------

sgl can be installed inside a `virtualenv`_ just like any other python package,
though I suggest the use of `virtualenvwrapper`_.

If you want to use vtk inside the virtualenv, you need to manually copy the vtk
folder into your virtualenv library path. The vtk folder is usually found at
:file:`/usr/lib/python2.7/site-packages/vtk`, but your mileage may vary.

.. _virtualenv: http://virtualenv.readthedocs.org/en/latest/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/
