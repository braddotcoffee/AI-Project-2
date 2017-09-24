from lib.brain import Brain
from lib.board import Board
from lib.color import Color
from lib.coordinate import Coordinate
from lib.piece import Piece
import code; 



def choose_move(board):
    copy_board = Board.create_copy(board)
    our_color = board.color

    best_score = float('-inf')

    for i in range(5):
        potential_move = copy_board.random_empty_coordinate()
        score = max_turn(copy_board, 5, 0, potential_move)
        if(score > best_score):
            best_score = score
            best_move = potential_move

    print("Score: {}".format(best_score))
    print("Move: {}".format(best_move))
    


def max_turn(board, max_depth, current_depth, move):
    if(current_depth == max_depth):
        return Brain.evaluation_function(board)

    copy_board = Board.create_copy(board)
    copy_board.add_piece(Piece(board.color, move))
    copy_board.color = Color.opposite(board.color) 

    best_score = float('-inf')
    for i in range(3):
        potential_move = copy_board.random_empty_coordinate()
        score = min_turn(copy_board, max_depth, current_depth+1, potential_move)
        if(score > best_score):
            best_score = score

    return best_score

def min_turn(board, max_depth, current_depth, move):
    if(current_depth == max_depth):
        return Brain.evaluation_function(board)

    copy_board = Board.create_copy(board)
    copy_board.add_piece(Piece(board.color, move))
    copy_board.color = Color.opposite(board.color) 

    best_score = float('inf')
    for i in range(3):
        potential_move = copy_board.random_empty_coordinate()
        score = max_turn(copy_board, max_depth, current_depth+1, potential_move)
        if(score < best_score):
            best_score = score

    return best_score



choose_move(Board())
