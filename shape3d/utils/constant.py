"""Constant module
Eps and significant numbers for comparing float point numbers.
two float numbers are deemed equal if they equal with each other within significant numbers.
significant numbers = log(1 / eps) all the time
"""
from math import pi,log10

# epsilon to compare if two float numbers equal to each other

SIG_FIGURES = 10
FLOAT_EPS = 1 / (10 ** SIG_FIGURES)

def set_eps(eps):
    """
    Input: eps

    Output:
    no output but set EPS to eps
    signigicant numbers is also changed.
    """
    global FLOAT_EPS,SIG_FIGURES
    FLOAT_EPS = eps
    SIG_FIGURES = round(log10(1 / eps))

def get_eps():
    '''
    Input: no input

    Output: current eps
    '''
    global FLOAT_EPS
    return FLOAT_EPS

def get_sig_figures():
    '''
    Input: no input

    Output: current significant numbers
    '''
    global SIG_FIGURES
    return SIG_FIGURES

def set_sig_figures(sig_figures):
    '''
    Input: sig_figures

    Output:
    no output but set signigicant numbers to sig_figures
    EPS is also changed.
    '''
    global FLOAT_EPS,SIG_FIGURES
    SIG_FIGURES = sig_figures
    FLOAT_EPS = 1 / (10 ** SIG_FIGURES)

__all__=('SIG_FIGURES','FLOAT_EPS','set_eps','get_eps','get_sig_figures','set_sig_figures')
    