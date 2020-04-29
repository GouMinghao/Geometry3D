"""Abstract Renderer Module"""
from .renderer_matplotlib import MatplotlibRenderer

def Renderer(backend='matplotlib'):
    """
    **Input:**
    
    - backend: the backend of the renderer
    
    Only matplotlib is supported till now
    """
    if backend == 'matplotlib':
        return MatplotlibRenderer()
    else:
        raise ValueError('Unknown backend %s' % (backend,))