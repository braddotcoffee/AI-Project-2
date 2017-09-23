from lib.analyze_board import sets_of_adjacent
from lib.coordinate import Coordinate
from lib.piece import Piece
from lib.board import Board
from lib.color import Color

class Brain(object):
    def __init__(self, color=Color.WHITE):
        self._color = color

    # Chooses move to make
    # Returns Piece to add to board
    def make_move(self, board):
        pass

    def evaluation_function(self, board):
        own_score = [ sets_of_adjacent(i, board.all_friendly())  for i in range(1,6) ]
        enemy_score = [ sets_of_adjacent(i, board.all_enemy())  for i in range(1,6) ]
        score =  Brain.apply_coefficient(own_score[0], enemy_score[0], 1)
        score += Brain.apply_coefficient(own_score[1], enemy_score[1], 3)
        score += Brain.apply_coefficient(own_score[2], enemy_score[2], 5)
        score += Brain.apply_coefficient(own_score[3], enemy_score[3], 7)
        score += Brain.apply_coefficient(own_score[4], enemy_score[4], 9)
        return score

    @staticmethod
    def apply_coefficient(own, enemy, coeff):
        return (coeff * own) - (coeff * enemy)
