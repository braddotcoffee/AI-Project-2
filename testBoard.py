from lib.analyze_board import sets_of_adjacent
from lib.coordinate import Coordinate
import cProfile
from lib.board import Board
from lib.color import Color
from lib.piece import Piece
from multiprocessing import Pool
from lib.brain import Brain

def main():
    testBoard = Board()
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,1)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(2,1)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(3,1)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(5,1)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(6,1)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(7,1)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,2)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,3)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,5)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,6)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,7)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(2,2)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(3,3)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(2,4)))
    testBoard.add_piece(Piece(Color.WHITE, Coordinate(4,2)))
    """
    BOARD BEING BUILT

    ###########################
    # x                       #   
    # x                       #   
    # x                       #   
    #   x                     #   
    # x   x                   #   
    # x x   x                 #   
    # x x x   x x x           #   
    ###########################

    """

    # print(sets_of_adjacent(1, testBoard.all_friendly()))
    # print(sets_of_adjacent(2, testBoard.all_friendly()))
    # print(sets_of_adjacent(3, testBoard.all_friendly()))
    # print(sets_of_adjacent(4, testBoard.all_friendly()))
    # print(sets_of_adjacent(5, testBoard.all_friendly()))

    brain = Brain()
    print(brain.evaluation_function(testBoard))

if __name__ == "__main__":
    cProfile.run('main()')
