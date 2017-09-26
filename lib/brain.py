from lib.analyze_board import sets_of_adjacent
from lib.coordinate import Coordinate
from lib.piece import Piece
from lib.board import Board
from lib.color import Color
import operator

class Brain(object):
    def __init__(self, coeff=[1,3,5,7,9], branching_factor=12, depth=2):
        self._coeff = coeff
        self._branching_factor = branching_factor
        self._depth = depth

    # Chooses move to make
    # Returns Piece to add to board
    def make_move(self, board):
        count = 0
        best_score = float('-inf')
        for index in range(self._branching_factor):
            potential_move = board.empty_random_piece()
            copy_board = self.make_move_on_copy_board(board, potential_move, board.color)
            score = self.min_turn(copy_board, self._depth, float('-inf'), float('inf'))
            count = count + 1

            if(score > best_score):
                best_score = score
                best_move = potential_move

        print("Score: {}".format(best_score))
        print("Final Move: {}".format(best_move))
        return best_move


    def evaluation_function(self, board):
        own_score = [ sets_of_adjacent(i, board.all_friendly())  for i in range(1,6) ]
        enemy_score = [ sets_of_adjacent(i, board.all_enemy())  for i in range(1,6) ]
        score = 0
        for i in range(5):
            score += Brain.apply_coefficient(own_score[i], enemy_score[i], self._coeff[i])
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
            copy_board = self.make_move_on_copy_board(board, potential_move, board.color)

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
            copy_board = self.make_move_on_copy_board(board, potential_move, Color.opposite(board.color))

            best_score = min(best_score, self.max_turn(copy_board, current_depth-1, alpha, beta))
            beta = min(beta, best_score)

            if(beta < alpha):
                #print("Prune")
                return best_score

        return best_score

    #Make a move on a copy of the board and return the new board
    #Switch the color of the copy board so that the next move does the opposite color
    def make_move_on_copy_board(self, board, move, color):
        copy_board = Board.create_copy(board)
        copy_board.add_piece(Piece(color, move))
        return copy_board

