from lib.coordinate import Coordinate
from lib.color import Color

class AdjacencyMatrix(object):
    def __init__(self, color=Color.WHITE):
        self.color = color
        self.matrix = [[0]*255]*255
