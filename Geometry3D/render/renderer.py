from ..visualization.visualizer import Visualizer
from ..utils.logger import get_main_logger
logger = get_main_logger()
logger.warning("'Renderer' is deprecated, using 'Visualizer' instead.")
Renderer = Visualizer