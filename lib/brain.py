from lib.analyze_board import sets_of_adjacent
from lib.coordinate import Coordinate
from lib.piece import Piece
from lib.board import Board
from lib.color import Color

class Brain(object):
    def __init__(self, color=Color.WHITE, coeff=[1,3,5,7,9]):
        self._color = color
        self._coeff = coeff

    # Chooses move to make
    # Returns Piece to add to board
    def make_move(self, board):
        pass

    @staticmethod
    def evaluation_function(board, coeff=[1,3,5,7,9]):
        
        own_score = [ sets_of_adjacent(i, board.all_friendly())  for i in range(1,6) ]
        enemy_score = [ sets_of_adjacent(i, board.all_enemy())  for i in range(1,6) ]
        score = 0
        for i in range(5):
            score += Brain.apply_coefficient(own_score[i], enemy_score[i], coeff[i])
        return score

    @staticmethod
    def apply_coefficient(own, enemy, coeff):
        return (coeff * own) - (coeff * enemy)
