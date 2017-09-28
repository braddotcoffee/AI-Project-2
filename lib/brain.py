from lib.frontal_lobe import FrontalLobe 
from lib.piece import Piece
from lib.board import Board
from lib.color import Color
import operator

class Brain(object):
    def __init__(self, f_coeff=[1,10,30,90,900], e_coeff=[1,20, 50, 120, 855], branching_factors=[22,5],
            depth=1):
        self._depth = depth
        self._frontal_lobe = FrontalLobe(f_coeff, e_coeff, depth)
        self._branching_factors = branching_factors

    # Chooses move to make
    # Returns Piece to add to board
    def make_move(self, board):
        move_list = board.get_empty_adjacencies()
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(self._branching_factors[0], explored_moves)
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(self._branching_factors[1], explored_moves)
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(1, explored_moves)
        final_move = move_list[0]

        print("Best Score: %d" % explored_moves[final_move])
        print("Best move: %s" % final_move)

        self._frontal_lobe.depth = 1

        return final_move

    def next_pass(self, num, explored_moves):
        move_list = list(explored_moves.keys())
        move_list = Brain.get_num_best(num, move_list, explored_moves)
        self._frontal_lobe.depth += 1
        return move_list


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


