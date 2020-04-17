from .renderer_matplotlib import MatplotlibRenderer

def Renderer(backend='matplotlib'):
    if backend == 'matplotlib':
        return MatplotlibRenderer()
    else:
        raise ValueError('Unknown backend %s' % (backend,))