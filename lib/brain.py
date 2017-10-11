from lib.frontal_lobe import FrontalLobe 
from lib.piece import Piece
from lib.board import Board
from lib.color import Color
import operator

class Brain(object):
    def __init__(self, f_coeff=[1,20,50,100,900], e_coeff=[1,35, 60, 150, 855], depth=1):
        self._depth = depth
        self._frontal_lobe = FrontalLobe(f_coeff, e_coeff, depth)

    # Chooses move to make
    # Returns Piece to add to board
    def make_move(self, board):
        move_list = board.get_empty_adjacencies()
        branching_factors = Brain.get_branching_factors(len(move_list))
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(branching_factors[0], explored_moves)
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(branching_factors[1], explored_moves)
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(1, explored_moves)
        final_move = move_list[0]

        self._frontal_lobe.depth = 1

        return final_move

    def next_pass(self, num, explored_moves):
        move_list = list(explored_moves.keys())
        move_list = Brain.get_num_best(num, move_list, explored_moves)
        self._frontal_lobe.depth += 1
        return move_list

    @staticmethod
    def get_branching_factors(len_move_list):
        if len_move_list < 30:
            return (25, 5)
        elif len_move_list < 50:
            return (20, 3)
        else:
            return (18,2)

    @staticmethod
    def get_num_best(num, move_list, explored_moves):
        best = []
        for i in range(num):
            best_score = float("-inf")
            best_move = None
            for move in move_list:
                curr_score = explored_moves[move]
                if curr_score > best_score:
                    best_score = curr_score
                    best_move = move
            best.append(best_move)
        return best


