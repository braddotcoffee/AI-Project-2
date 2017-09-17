from enum import Enum

class Color(Enum):
    NONE  = -1
    WHITE = 1
    BLACK = 2

    @staticmethod
    def opposite(color):
        if color == Color.WHITE:
            return Color.BLACK
        elif color == Color.BLACK:
            return Color.WHITE
        else:
            return Color.NONE
