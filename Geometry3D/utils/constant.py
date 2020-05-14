"""
Constant module

EPS and significant numbers for comparing float point numbers.

Two float numbers are deemed equal if they equal with each other within significant numbers.

Significant numbers = log(1 / eps) all the time
"""
from math import pi,log10

# epsilon to compare if two float numbers equal to each other

SIG_FIGURES = 10
FLOAT_EPS = 1 / (10 ** SIG_FIGURES)

def set_eps(eps = 1e-10):
    """
    **Input:**

    - eps: floating number with 1e-10 the default

    **Output:**
    
    No output but set EPS to eps
    
    Signigicant numbers is also changed.
    """
    global FLOAT_EPS,SIG_FIGURES
    FLOAT_EPS = eps
    SIG_FIGURES = round(log10(1 / eps))

def get_eps():
    '''
    **Input:**

    no input

    **Output:**
    
    - current eps: float
    '''
    global FLOAT_EPS
    return FLOAT_EPS

def get_sig_figures():
    '''
    **Input:**
    
    no input

    **Output:**
    
    - current significant numbers: int
    '''
    global SIG_FIGURES
    return SIG_FIGURES

def set_sig_figures(sig_figures = 10):
    '''
    **Input:**
    
    - sig_figures: int with 10 the default

    **Output:**
    
    No output but set signigicant numbers to sig_figures
    
    EPS is also changed.
    '''
    global FLOAT_EPS,SIG_FIGURES
    SIG_FIGURES = sig_figures
    FLOAT_EPS = 1 / (10 ** SIG_FIGURES)

SMALL_ANGLE = 0.1 # used in ..calc.aux_calc

__all__=('SIG_FIGURES','FLOAT_EPS','SMALL_ANGLE','set_eps','get_eps','get_sig_figures','set_sig_figures')
    