"""Matplotlib Visualizer Module"""

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ..utils.logger import get_main_logger
from .base_visualizer import BaseVisualizer


class MatplotlibVisualizer(BaseVisualizer):
    """Visualizer module to visualize geometries"""

    def __init__(self):
        super(MatplotlibVisualizer, self).__init__()

    def show(self):
        """
        Draw the image
        """
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        get_main_logger().info(
            "Showing geometries with %d points, %d segments, %d arrows using matplotlib"
            % (len(self.point_set), len(self.segment_set), len(self.arrow_set))
        )
        for point_tuple in self.point_set:
            point = point_tuple[0]
            color = point_tuple[1]
            size = point_tuple[2]
            ax.scatter(point.x, point.y, point.z, c=color, s=size)

        for segment_tuple in self.segment_set:
            segment = segment_tuple[0]
            color = segment_tuple[1]
            size = segment_tuple[2]
            x = [segment.start_point.x, segment.end_point.x]
            y = [segment.start_point.y, segment.end_point.y]
            z = [segment.start_point.z, segment.end_point.z]
            ax.plot(x, y, z, color=color, linewidth=size)

        for arrow_tuple in self.arrow_set:
            x, y, z, u, v, w, length = arrow_tuple[0].get_tuple()
            color = arrow_tuple[1]
            size = arrow_tuple[2]
            ax.quiver(x, y, z, u, v, w, color=color, length=length)

        plt.show()
