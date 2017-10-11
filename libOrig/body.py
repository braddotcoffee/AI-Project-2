from lib.color import Color
from lib.coordinate import Coordinate
from lib.board import Board
from lib.brain import Brain
from lib.piece import Piece

class Body():
    def __init__(self, color):
        self._brain = Brain()
        self._color = color
        self._board = Board.create_init_board(color)

    #Called by the IO manager whenever the enemy makes a move. 
    def enemy_made_move(self, piece):
        self._board.add_piece(piece)

    #Sends the current board state to the brain, gets a move back, and makes it
    def make_move(self):
        our_move = self._brain.make_move(self._board)
        self._board.add_piece(Piece(self._color, our_move))
        return our_move
        
