from lib.analyze_board import sets_of_adjacent
from lib.board import Board
from lib.color import Color

class FrontalLobe(object):
    def __init__(self, coeff=[1,3,5,7,900], branching_factor=12):
        self._coeff = coeff
        self._branching_factor = branching_factor

    def evaluation_function(self, board):
        own_score = [ sets_of_adjacent(i, board.all_friendly())  for i in range(1,6) ]
        enemy_score = [ sets_of_adjacent(i, board.all_enemy())  for i in range(1,6) ]
        score = 0
        for i in range(5):
            score += FrontalLobe.apply_coefficient(own_score[i], enemy_score[i], self._coeff[i])
        return score

    @staticmethod
    def apply_coefficient(own, enemy, coeff):
        return (coeff * own) - (coeff * enemy)

    def max_turn(self, board, current_depth, alpha, beta):
        if(current_depth == 0): ##Also need to implement game_over_state
            return self.evaluation_function(board)

        best_score = float('-inf')
        for index in range(self._branching_factor):
            potential_move = board.empty_random_piece()
            copy_board = Board.make_move_on_copy_board(board, potential_move, board.color)

            best_score = max(best_score, self.min_turn(copy_board, current_depth-1, alpha, beta))
            alpha = max(alpha, best_score)

            if(beta < alpha):
                #print("Prune")
                return best_score

        return best_score

    def min_turn(self, board, current_depth, alpha, beta):
        if(current_depth == 0):
            return self.evaluation_function(board)

        best_score = float('inf')
        for index in range(self._branching_factor):
            potential_move = board.empty_random_piece()
            copy_board = Board.make_move_on_copy_board(board, potential_move, Color.opposite(board.color))

            best_score = min(best_score, self.max_turn(copy_board, current_depth-1, alpha, beta))
            beta = min(beta, best_score)

            if(beta < alpha):
                #print("Prune")
                return best_score

        return best_score


