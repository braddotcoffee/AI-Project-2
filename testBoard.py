from lib.analyze_board import *
from lib.coordinate import Coordinate
import cProfile
from lib.board import Board
from lib.color import Color
from lib.piece import Piece
from multiprocessing import Pool
from lib.brain import Brain
import unittest

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

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.testBoard = Board()
        self.brain = Brain()

    def test_empty(self):
        self.assertEqual(self.brain.evaluation_function(self.testBoard), 0)
        self.assertEqual(sets_by_row(1, self.testBoard.all_friendly()), 0)
        self.assertEqual(sets_by_col(1, self.testBoard.all_friendly()), 0)
        self.assertEqual(sets_by_diag(1, self.testBoard.all_friendly()), 0)

    def test_horizontal(self):
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(2,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(3,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(5,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(6,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(7,1)))

        """
        #############################
        #                           #  
        #                           #  
        #                           #  
        #                           #  
        #                           #  
        #                           #  
        # x x x  x x x              #  
        #############################

        sets(1) = 18 [count each diag and each vertical]
        sets(2) = 0
        sets(3) = 2

        """
        self.assertEqual(self.brain.evaluation_function(self.testBoard), 28)

    def test_vertical(self):
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,2)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,3)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,5)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,6)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,7)))

        """
        #############################
        # x                         #  
        # x                         #  
        # x                         #  
        #                           #  
        # x                         #  
        # x                         #  
        # x                         #  
        #############################

        sets(1) = 18 [couont each diag and each horizontal]
        sets(2) = 0
        sets(3) = 2

        """
        self.assertEqual(self.brain.evaluation_function(self.testBoard), 28)

    def test_diag(self):
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(2,2)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(3,3)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(2,4)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,5)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(4,2)))

        """
        #############################
        #                           #  
        #                           #  
        # x                         #  
        #   x                       #  
        #     x                     #  
        #   x   x                   #  
        # x                         #  
        #############################

        sets(1) = 18 [couont each diag and each horizontal] * 1
        sets(2) = 0 * 3
        sets(3) = 1 * 5
        sets(4) = 1 * 7

        """
        self.assertEqual(self.brain.evaluation_function(self.testBoard), 30)

if __name__ == "__main__":
    unittest.main()
