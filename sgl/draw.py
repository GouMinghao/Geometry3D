# -*- coding: utf-8 -*-
import math
from .line import Line
from .point import Point
from .vector import Vector

def draw_parallels(renderer, box, start, count, direction, delta,
                   color=(0.7, 0.7, 0.7), opacity=0.5):
    """Draw count parallel lines, pointing in direction, starting at
    start and changing by delta each step.
    """
    for i in range(count):
        Line(start, direction).draw(renderer, box, color=color)
        start = Point(start.pv() + delta)


def draw(elements, background=(0.5, 0.5, 0.5), size=(640, 480),
        box=((-10, -10, -10), (10, 10, 10)), grid=(1, 0, 1)):
    """Visualize the given elements.

    box defines a cuboid that acts as a boundary. Only stuff inside of
    the cuboid is drawn. The cuboid is defined as
        ((minx, miny, minz), (maxx, maxy, maxz)).

    grid defines if a coordinate grid should be drawn. It conists of
    three float values (x1x2, x1x3, x2x3). The values specify the
    distance between each grid line. If the distance is 0, the grid
    will not be drawn.
    """
    min_, max_ = box
    import vtk

    renderer = vtk.vtkRenderer()
    renderer.SetBackground(*background)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(*size)
    renderWindow.LineSmoothingOn()
    renderWindow.PolygonSmoothingOn()
    renderWindow.PointSmoothingOn()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName("sgl")

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderWindowInteractor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    # Add axes
    axes = vtk.vtkAxesActor()
    axes.SetTotalLength(10, 10, 10)
    for actor in (
            axes.GetXAxisCaptionActor2D().GetTextActor(),
            axes.GetYAxisCaptionActor2D().GetTextActor(),
            axes.GetZAxisCaptionActor2D().GetTextActor(),
        ):
        actor.SetTextScaleModeToNone()
        actor.GetTextProperty().SetFontSize(25)
        actor.GetTextProperty().SetColor(0, 0, 0)
        actor.GetTextProperty().ShadowOff()
    axes.SetXAxisLabelText("x2")
    axes.SetYAxisLabelText("x3")
    axes.SetZAxisLabelText("x1")
    axes.SetConeRadius(0.1)
    renderer.AddActor(axes)

    # Add grid
    if grid[0]:  # x1x2
        start = int(math.ceil(min_[0]))
        stop = int(math.floor(max_[0]))
        delta = grid[0]
        draw_parallels(renderer, box,
                start=Point(start, 0, 0),
                direction=Vector(0, 1, 0),
                delta=Vector(delta, 0, 0),
                count=(stop - start + 1)/delta,
        )
        start = int(math.ceil(min_[1]))
        stop = int(math.floor(max_[1]))
        delta = grid[0]
        draw_parallels(renderer, box,
                start=Point(0, start, 0),
                direction=Vector(1, 0, 0),
                delta=Vector(0, delta, 0),
                count=(stop - start + 1)/delta,
        )

    if grid[1]:  # x1x3
        start = int(math.ceil(min_[0]))
        stop = int(math.floor(max_[0]))
        delta = grid[1]
        draw_parallels(renderer, box,
                start=Point(start, 0, 0),
                direction=Vector(0, 0, 1),
                delta=Vector(delta, 0, 0),
                count=(stop - start + 1)/delta,
        )
        start = int(math.ceil(min_[2]))
        stop = int(math.floor(max_[2]))
        delta = grid[1]
        draw_parallels(renderer, box,
                start=Point(0, 0, start),
                direction=Vector(1, 0, 0),
                delta=Vector(0, 0, delta),
                count=(stop - start + 1)/delta,
        )

    if grid[2]:  # x2x3
        start = int(math.ceil(min_[1]))
        stop = int(math.floor(max_[1]))
        delta = grid[2]
        draw_parallels(renderer, box,
                start=Point(0, start, 0),
                direction=Vector(0, 0, 1),
                delta=Vector(0, delta, 0),
                count=(stop - start + 1)/delta,
        )
        start = int(math.ceil(min_[2]))
        stop = int(math.floor(max_[2]))
        delta = grid[2]
        draw_parallels(renderer, box,
                start=Point(0, 0, start),
                direction=Vector(0, 1, 0),
                delta=Vector(0, 0, delta),
                count=(stop - start + 1)/delta,
        )
        
    for element in elements:
        element.draw(renderer, box)

    renderer.ResetCamera()
    renderer.GetActiveCamera().SetFocalPoint(0, 0, 0)
    renderWindow.Render()
    renderWindowInteractor.Start()


__all__ = ("draw",)
