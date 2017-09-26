from lib.analyze_board import *
from lib.coordinate import Coordinate
import cProfile
from lib.board import Board
from lib.color import Color
from lib.piece import Piece
from multiprocessing import Pool
from lib.brain import Brain
import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.testBoard = Board()
        self.brain = Brain()

    def test_within_time(self):
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(1,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(2,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(3,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(5,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(6,1)))
        self.testBoard.add_piece(Piece(Color.WHITE, Coordinate(7,1)))

        self.testBoard.add_piece(Piece(Color.BLACK, Coordinate(1,4)))
        self.testBoard.add_piece(Piece(Color.BLACK, Coordinate(2,4)))
        self.testBoard.add_piece(Piece(Color.BLACK, Coordinate(3,4)))
        self.testBoard.add_piece(Piece(Color.BLACK, Coordinate(5,4)))
        self.testBoard.add_piece(Piece(Color.BLACK, Coordinate(6,4)))
        self.testBoard.add_piece(Piece(Color.BLACK, Coordinate(7,4)))

        """

        ##############################
        #                            #         
        #                            #         
        #                            #         
        # B B B    B B B             #         
        #                            #         
        #                            #         
        # W W W    W W W             #         
        ##############################

        """

        self.brain.make_move(self.testBoard)


if __name__ == "__main__":
    unittest.main()

