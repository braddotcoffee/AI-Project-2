from lib.frontal_lobe import FrontalLobe
from lib.piece import Piece
from lib.board import Board
from lib.color import Color
import operator

class Brain(object):
    def __init__(self, coeff=[1,3,5,7,900], branching_factor=12, depth=2):
        self._branching_factor = branching_factor
        self._depth = depth
        self._frontal_lobe = FrontalLobe(coeff, branching_factor)

    # Chooses move to make
    # Returns Piece to add to board
    def make_move(self, board):
        count = 0
        best_score = float('-inf')
        for index in range(self._branching_factor):
            potential_move = board.empty_random_piece()
            copy_board = Board.make_move_on_copy_board(board, potential_move, board.color)
            score = self._frontal_lobe.min_turn(copy_board, self._depth, float('-inf'), float('inf'))
            count = count + 1

            if(score > best_score):
                best_score = score
                best_move = potential_move

        print("Score: {}".format(best_score))
        print("Final Move: {}".format(best_move))
        return best_move
