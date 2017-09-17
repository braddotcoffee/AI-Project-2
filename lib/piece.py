from lib.color import Color
from lib.coordinate import Coordinate

class Piece(object):
    def __init__(self, color, coordinate):
        self.color = color
        self.coordinate = coordinate
