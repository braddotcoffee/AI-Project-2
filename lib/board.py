import random
from lib.color import Color
from lib.coordinate import Coordinate
from lib.piece import Piece
from copy import deepcopy

class Board(object):
    def __init__(self, color=Color.WHITE):
        self.color = color
        self._board = { Color.WHITE : {}, Color.BLACK : {} , Color.NONE : {}}

    @staticmethod
    def create_copy(board):
        return deepcopy(board)

    @staticmethod
    def create_init_board(color=Color.WHITE):
        board = Board(color)
        board._init_board()
        return board

    def _init_board(self):
        for i in range(15):
            for j in range(15):
                self.add_empty_piece(Coordinate(i, j))


    def __str__(self):
        return "Num White: {}, Num Black: {}, Num None: {}".format(
                len(self._board[Color.WHITE]),
                len(self._board[Color.BLACK]),
                len(self._board[Color.NONE]))

    def __deepcopy__(self, memodict={}):
        copy_obj = Board(self.color)
        for coord in self.all_empty():
            copy_obj.add_empty_piece(coord)
        for coord in self.all_friendly():
            copy_obj.direct_add_piece(Piece(self.color, coord))
        for coord in self.all_enemy():
            copy_obj.direct_add_piece(Piece(Color.opposite(self.color), coord))
        return copy_obj


    #Make a move on a copy of the board and return the new board
    #Switch the color of the copy board so that the next move does the opposite color
    @staticmethod
    def make_move_on_copy_board(board, move, color):
        copy_board = Board.create_copy(board)
        copy_board.add_piece(Piece(color, move))
        return copy_board.all_empty(), copy_board

    def random_empty_coordinate(self):
        return random.choice(list(self.all_empty().keys())) 

    # Returns dictionary of Coordinate -> Piece
    # Where Piece.Color == self.color
    def all_friendly(self):
        return self._board[self.color]

    # Returns dictionary of Coordinate -> Piece
    # Where Piece.Color == Color.opposite(self.color)
    def all_enemy(self):
        return self._board[Color.opposite(self.color)]

    # Returns dictionary of Coordinate -> Piece
    # Where Piece.Color == NONE
    def all_empty(self):
        return self._board[Color.NONE]

    # Returns an empty list of all empty Coordinates
    def empty_random_piece(self):
        pieces =  list(self.all_empty().keys())
        i = random.randint(0, len(pieces)-1)
        return pieces[i]

    # Returns true when agent owns coordinate
    def is_friendly(self, coordinate):
        return coordinate in self._board[self.color]

    # Returns true when enemy owns coordinate
    def is_enemy(self, coordinate):
        return coordinate in self._board[Color.opposite(self.color)]

    # Returns true if no one owns coordinate
    def is_empty(self, coordinate):
        return not self.is_friendly(coordinate) and not self.is_enemy(coordinate)

    def remove_piece(self, piece):
        self._board[piece.color].pop(piece.coordinate)
        self.add_empty_piece(piece.coordinate)

    # Add a piece to the board
    def add_piece(self, piece):
        self.direct_add_piece(piece)
        del self._board[Color.NONE][piece.coordinate]

    # Adds empty piece to the board
    def add_empty_piece(self, coordinate):
        self._board[Color.NONE][coordinate] = Piece(Color.NONE, coordinate)

    # Adds piece does not delete from none
    def direct_add_piece(self, piece):
        self._board[piece.color][piece.coordinate] = piece
