from lib.analyze_board import sets_of_adjacent
from lib.board import Board
from lib.color import Color
from lib.piece import Piece
from lib.coordinate import Coordinate

class FrontalLobe(object):
    def __init__(self, f_coeff, e_coeff, depth=1):
        self.f_coeff = f_coeff
        self.e_coeff = e_coeff
        self.depth = depth

    def make_move(self, board, move_list):
        explored_moves = {}
        for potential_move in move_list:
            new_move_list, copy_board = Board.make_move_on_copy_board(board, potential_move, board.color)

            score, move = self.min_turn(copy_board, new_move_list, self.depth - 1, float('-inf'), float('inf'))

            if(score < -6000):
                return {move: float('inf')}

            explored_moves[potential_move] = score

        return explored_moves


    def evaluation_function(self, board):
        own_score = sets_of_adjacent(board.all_friendly(), board.all_empty())
        enemy_score = sets_of_adjacent(board.all_enemy(), board.all_empty())
        score = 0
        for i in range(1,6):
            score += FrontalLobe.apply_coefficient(own_score[i], enemy_score[i], self.f_coeff[i-1],
                    self.e_coeff[i-1])
        return score

    @staticmethod
    def apply_coefficient(own, enemy, f_coeff, e_coeff):
        return (f_coeff * own) - (e_coeff * enemy)

    def max_turn(self, board, move_list, current_depth, alpha, beta):
        if(current_depth == 0): ##Also need to implement game_over_state
            return self.evaluation_function(board)


        best_score = float('-inf')
        for potential_move in move_list:
            new_move_list, copy_board = Board.make_move_on_copy_board(board, potential_move, board.color)

            score, move = self.min_turn(copy_board, new_move_list, current_depth-1, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)


            if(beta < alpha):
                return best_score

        return best_score

    def min_turn(self, board, move_list, current_depth, alpha, beta):
        if(current_depth == 0):
            return self.evaluation_function(board), None

        best_score = float('inf')
        for potential_move in move_list:
            new_move_list, copy_board = Board.make_move_on_copy_board(board, potential_move,
                    Color.opposite(board.color))

            best_score = min(best_score, self.max_turn(copy_board, new_move_list, current_depth-1, alpha, beta))
            beta = min(beta, best_score)

            if(best_score < -6000):
                return best_score, potential_move


            if(beta < alpha):
                return best_score, potential_move

        return best_score, None


