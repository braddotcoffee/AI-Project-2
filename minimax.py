from lib.brain import Brain
from lib.board import Board
from lib.color import Color
from lib.coordinate import Coordinate
from lib.piece import Piece
import code
import operator


#Top level function called by the brain. It chooses a move given a board state using minimax.
#Should probably refactor choose_board to DRY it at some point
def choose_move(board):
    copy_board = Board.create_copy(board)

    best_score = float('-inf')

    for i in range(5):
        potential_move = copy_board.random_empty_coordinate()
        score = min_turn(copy_board, 4, 0, potential_move)
        if(score > best_score):
            best_score = score
            best_move = potential_move

    print("Score: {}".format(best_score))
    print("Move: {}".format(best_move))
    return best_move
    


def max_turn(board, max_depth, current_depth, move):
    if(current_depth == max_depth):
        brain = Brain()
        return brain.evaluation_function(board)

    copy_board = make_move_on_copy_board(board, move)

    best_score = find_best_move(copy_board, max_depth, current_depth, min_turn, operator.gt, float('-inf'))

    return best_score

def min_turn(board, max_depth, current_depth, move):
    if(current_depth == max_depth):
        brain = Brain()
        return brain.evaluation_function(board)

    copy_board = make_move_on_copy_board(board, move)

    best_score = find_best_move(copy_board, max_depth, current_depth, max_turn, operator.lt, float('inf'))
    return best_score

def make_move_on_copy_board(board, move):
    copy_board = Board.create_copy(board)
    copy_board.add_piece(Piece(board.color, move))
    copy_board.color = Color.opposite(board.color) 
    return copy_board

def find_best_move(board, max_depth, current_depth, function_to_call, operation, base_score):
    best_score = base_score
    for i in range(3):
        potential_move = board.random_empty_coordinate()
        score = function_to_call(board, max_depth, current_depth+1, potential_move)
        if(operation(score, best_score)):
            best_score = score
    return best_score



choose_move(Board())
