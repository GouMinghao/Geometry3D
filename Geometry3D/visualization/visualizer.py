"""Abstract Visualizer Module"""

from ..utils.logger import get_main_logger

try:
    from .visualizer_matplotlib import MatplotlibVisualizer
except ModuleNotFoundError:
    get_main_logger().info("Fail to load matplotlib Visualizer")

try:
    from .visualizer_open3d import Open3dVisualizer
except ModuleNotFoundError:
    get_main_logger().info("Fail to load open3d Visualizer")


def Visualizer(backend="matplotlib"):
    """
    **Input:**

    - backend: the backend of the Visualizer

    Only matplotlib is supported till now
    """
    if backend == "matplotlib":
        return MatplotlibVisualizer()
    elif backend == "open3d":
        return Open3dVisualizer()
    else:
        raise ValueError("Unknown backend {}".format(backend))
