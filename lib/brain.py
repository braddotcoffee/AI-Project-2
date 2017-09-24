from lib.analyze_board import sets_of_adjacent
from lib.coordinate import Coordinate
from lib.piece import Piece
from lib.board import Board
from lib.color import Color
import operator

class Brain(object):
    def __init__(self, coeff=[1,3,5,7,9]):
        self._coeff = coeff

    # Chooses move to make
    # Returns Piece to add to board
    def make_move(self, board):
        copy_board = Board.create_copy(board)

        best_score = float('-inf')

        for i in range(5):
            potential_move = copy_board.random_empty_coordinate()
            score = self.min_turn(copy_board, 4, 0, potential_move)
            if(score > best_score):
                best_score = score
                best_move = potential_move

        print("Score: {}".format(best_score))
        print("Move: {}".format(best_move))
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


    def max_turn(self, board, max_depth, current_depth, move):
        if(current_depth == max_depth):
            return self.evaluation_function(board)

        copy_board = self.make_move_on_copy_board(board, move)

        best_score = self.find_best_move(copy_board, max_depth, current_depth, self.min_turn, operator.gt, float('-inf'))

        return best_score

    def min_turn(self, board, max_depth, current_depth, move):
        if(current_depth == max_depth):
            brain = Brain()
            return brain.evaluation_function(board)

        copy_board = self.make_move_on_copy_board(board, move)

        best_score = self.find_best_move(copy_board, max_depth, current_depth, self.max_turn, operator.lt, float('inf'))
        return best_score

    #Make a move on a copy of the board and return the new board
    #Switch the color of the copy board so that the next move does the opposite color
    def make_move_on_copy_board(self, board, move):
        copy_board = Board.create_copy(board)
        copy_board.add_piece(Piece(board.color, move))
        copy_board.color = Color.opposite(board.color) 
        return copy_board

    def find_best_move(self, board, max_depth, current_depth, function_to_call, operation, base_score):
        best_score = base_score
        for i in range(3):
            potential_move = board.random_empty_coordinate()
            score = function_to_call(board, max_depth, current_depth+1, potential_move)
            if(operation(score, best_score)):
                best_score = score
        return best_score

