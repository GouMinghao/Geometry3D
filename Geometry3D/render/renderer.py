"""Abstract Renderer Module"""

from ..utils.logger import get_main_logger

try:
    from .renderer_matplotlib import MatplotlibRenderer
except ModuleNotFoundError:
    get_main_logger().info("Fail to load matplotlib renderer")

try:
    from .renderer_open3d import Open3dRenderer
except ModuleNotFoundError:
    get_main_logger().info("Fail to load open3d renderer")


def Renderer(backend="matplotlib"):
    """
    **Input:**

    - backend: the backend of the renderer

    Only matplotlib is supported till now
    """
    if backend == "matplotlib":
        return MatplotlibRenderer()
    elif backend == "open3d":
        return Open3dRenderer()
    else:
        raise ValueError("Unknown backend {}".format(backend))
