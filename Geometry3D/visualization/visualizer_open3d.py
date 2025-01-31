import open3d as o3d
import numpy as np

from ..utils.logger import get_main_logger
from .base_visualizer import BaseVisualizer


class Open3dVisualizer(BaseVisualizer):
    def __init__(self):
        super(Open3dVisualizer, self).__init__()

    def show(self):
        """
        Draw the image
        """
        geometries = []

        get_main_logger().info(
            "Showing geometries with %d points, %d segments, %d arrows using open3d"
            % (len(self.point_set), len(self.segment_set), len(self.arrow_set))
        )
        # visualize points
        for point_tuple in self.point_set:
            point = point_tuple[0]
            color = point_tuple[1]
            size = point_tuple[2]
            box = o3d.geometry.TriangleMesh.create_box(size, size, size)
            box.translate(np.zeros((3, 1), dtype=np.float64), relative=False)
            # breakpoint()
            box.translate(np.array((point.x, point.y, point.z), dtype=np.float64))
            box.paint_uniform_color(np.array(color, dtype=np.float64))
            geometries.append(box)

        # visualize segments
        for segment_tuple in self.segment_set:
            segment = segment_tuple[0]
            color = segment_tuple[1]
            size = segment_tuple[2]
            pts_list = []
            idx_list = []
            pts_list.append(
                (segment.start_point.x, segment.start_point.y, segment.start_point.z)
            )
            pts_list.append(
                (segment.end_point.x, segment.end_point.y, segment.end_point.z)
            )
            idx_list.append([0, 1])
            line_set = o3d.geometry.LineSet()
            line_set.points = o3d.utility.Vector3dVector(
                np.array(pts_list, dtype=np.float64)
            )
            line_set.lines = o3d.utility.Vector2iVector(
                np.array(idx_list, dtype=np.int32)
            )
            line_set.paint_uniform_color(np.array(color, dtype=np.float64))
            geometries.append(line_set)

        # visualize arrow
        for arrow_tuple in self.arrow_set:
            x, y, z, u, v, w, length = arrow_tuple[0].get_tuple()
            color = arrow_tuple[1]
            size = arrow_tuple[2]
            arrow_geometry = o3d.geometry.TriangleMesh.create_arrow(
                cylinder_radius=size * 0.5,
                cone_radius=size,
                cylinder_height=length * 0.95,
                cone_height=length * 0.05,
                resolution=4,
                cylinder_split=4,
                cone_split=1,
            )
            rot_z = np.array((u, v, w))
            rot_x = np.cross(rot_z, np.array((0, 0, 1)))
            if np.linalg.norm(rot_x) < 0.05:  # if norm is small, create another vector
                rot_x = np.cross(rot_z, np.array((0, 1, 0)))
            rot_x = rot_x / np.linalg.norm(rot_x)
            rot_y = np.cross(rot_z, rot_x)
            rot = np.vstack((rot_x, rot_y, rot_z)).T
            arrow_geometry.rotate(rot, center=np.zeros((3, 1), dtype=np.float64))
            arrow_geometry.translate(np.array((x, y, z), dtype=np.float64))
            arrow_geometry.paint_uniform_color(np.array(color, dtype=np.float64))
            geometries.append(arrow_geometry)
        o3d.visualization.draw_geometries(geometries)
