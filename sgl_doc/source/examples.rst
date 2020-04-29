Examples
========

Point on Line
-------------
Given point :math:`P(1 | 2 | 3)` and line
:math:`l: \vec{x} = \begin{pmatrix}-1\\-2\\-3\end{pmatrix} + r\begin{pmatrix}1\\2\\3\end{pmatrix}; r \in \mathbb{R}`
, is P on l?

.. literalinclude:: examples/1.py

Output::

    True

Line comparison
---------------
Are the lines
:math:`l1: \vec{x} = \begin{pmatrix}0\\0\\0\end{pmatrix} + r\begin{pmatrix}3\\5\\7\end{pmatrix}; r \in \mathbb{R}`
and
:math:`l2: \vec{x} = \begin{pmatrix}-3\\-5\\-7\end{pmatrix} + r\begin{pmatrix}6\\10\\14\end{pmatrix}; r \in \mathbb{R}`
the same?

.. literalinclude:: examples/2.py

Output::

    True

Pyramid
-------
Given Points :math:`A(0 | 0 | 0)`, :math:`B(3 | 0 | 0)`, :math:`C(0 | 5 | 0)`
and :math:`D(0 | 0 | 7)`. Compute the area of the Triangle :math:`\Delta ABC`
and the volume of the pyramid ``ABCD``.

.. literalinclude:: examples/3.py

Output::
    
    Area: 7.500000
    Volume: 17.500000

Different representations
-------------------------
Give the general form and the parametric form of the plane given by
:math:`P: \left[\vec{x} - \begin{pmatrix}2\\3\\5\end{pmatrix}\right]\begin{pmatrix}42\\0\\0\end{pmatrix} = 0`

.. literalinclude:: examples/4.py

Output::

    General: 42x1 + 0x2 + 0x3 = 84
    Parametric: x = Vector(2, 3, 5) + r * Vector(0.0, 1.0, 1.0) + s * Vector(0.0, -1.0, 1.0) ; r,s e R

More mathy:

.. math::

    General: 42x_{1} + 0x_{2} + 0x_{3} = 84 \\
    
    Parametric: \vec{x} = \begin{pmatrix}2\\3\\5\end{pmatrix} +
    r\begin{pmatrix}0\\1\\1\end{pmatrix} +
    s\begin{pmatrix}0\\-1\\1\end{pmatrix} ; (r, s) \in \mathbb{R}

Drawing
-------

The :func:`~sgl.draw.draw` function is not hard to use:

.. literalinclude:: examples/5.py

Output:

.. image:: _static/Screenshot-example-draw.png
