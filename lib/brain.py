from lib.frontal_lobe import FrontalLobe
from lib.piece import Piece
from lib.board import Board
from lib.color import Color
import operator

class Brain(object):
    def __init__(self, coeff=[1,3,5,7,900], depth=1):
        self._depth = depth
        self._frontal_lobe = FrontalLobe(coeff, depth)

    # Chooses move to make
    # Returns Piece to add to board
    def make_move(self, board):
        move_list = board.all_empty()
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(22, explored_moves)
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(2, explored_moves)
        explored_moves = self._frontal_lobe.make_move(board, move_list)
        move_list = self.next_pass(1, explored_moves)
        final_move = move_list[0]

        print("Best Score: %d" % explored_moves[final_move])
        print("Best move: %s" % final_move)

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


