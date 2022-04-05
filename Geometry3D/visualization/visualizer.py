"""Abstract Visualizer Module"""
from .visualizer_matplotlib import MatplotlibVisualizer

def Visualizer(backend='matplotlib'):
    """
    **Input:**
    
    - backend: the backend of the Visualizer
    
    Only matplotlib is supported till now
    """
    if backend == 'matplotlib':
        return MatplotlibVisualizer()
    else:
        raise ValueError('Unknown backend %s' % (backend,))