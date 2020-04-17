"""constants"""
from math import pi,log10

# epsilon to compare if two float numbers equal to each other

SIG_FIGURES = 10
FLOAT_EPS = 1 / (10 ** SIG_FIGURES)

def set_eps(eps):
    global FLOAT_EPS,SIG_FIGURES
    FLOAT_EPS = eps
    SIG_FIGURES = round(log10(1 / eps))

def get_eps():
    global FLOAT_EPS
    return FLOAT_EPS

def get_sig_figures():
    global SIG_FIGURES
    return SIG_FIGURES

def set_sig_figures(sig_figures):
    global FLOAT_EPS,SIG_FIGURES
    SIG_FIGURES = sig_figures
    FLOAT_EPS = 1 / (10 ** SIG_FIGURES)

__all__=('SIG_FIGURES','FLOAT_EPS','set_eps','get_eps','get_sig_figures','set_sig_figures')
    