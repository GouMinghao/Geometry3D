Dealing With Floating Numbers
=============================

There will be some errors in floating numbers computations. So identical objects may be deemed different.
To tackle with this problem, this library believe two objects equal if their difference is smaller that a small number `eps`. Another value is named `significant number` has the relationship with eps::

    significant number = -log(eps)

The default value of `eps` is 1e-10. You can access and change the value as follows::

    >>> get_eps()
    1e-10
    >>> get_sig_figures()
    10
    >>> set_sig_figures(5)
    >>> get_eps()
    1e-05
    >>> get_sig_figures()
    5
    >>> set_eps(1e-12)
    >>> get_eps()
    1e-12
    >>> get_sig_figures()
    12
