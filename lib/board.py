import random
from lib.color import Color
from lib.coordinate import Coordinate
from lib.piece import Piece
from copy import deepcopy

class Board(object):
    def __init__(self, color=Color.WHITE):
        self.color = color
        self._board = { Color.WHITE : {}, Color.BLACK : {} , Color.NONE : {}}
        self._init_board()

    def _init_board(self):
        for i in range(15):
            for j in range(15):
                self.add_empty_piece(Coordinate(i, j))


    @staticmethod
    def create_copy(board):
        return deepcopy(board)

    def random_empty_coordinate(self):
        return random.choice(list(self._board[Color.NONE].keys())) 

    # Returns dictionary of Coordinate -> Piece
    # Where Piece.Color == self.color
    def all_friendly(self):
        return self._board[self.color]

    # Returns dictionary of Coordinate -> Piece
    # Where Piece.Color == Color.opposite(self.color)
    def all_enemy(self):
        return self._board[Color.opposite(self.color)]

    # Returns true when agent owns coordinate
    def is_friendly(self, coordinate):
        return coordinate in self._board[self.color]

    # Returns true when enemy owns coordinate
    def is_enemy(self, coordinate):
        return coordinate in self._board[Color.opposite(self.color)]

    # Returns true if no one owns coordinate
    def is_empty(self, coordinate):
        return not self.is_friendly(coordinate) and not self.is_enemy(coordinate)

    # Add a piece to the board
    def add_piece(self, piece):
        self._board[piece.color][piece.coordinate] = piece
        del self._board[Color.NONE][piece.coordinate]

    # Adds empty piece to the board
    def add_empty_piece(self, coordinate):
        self._board[Color.NONE][coordinate] = Piece(Color.NONE, coordinate)
