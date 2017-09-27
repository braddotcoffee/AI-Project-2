from lib.color import Color
from lib.coordinate import Coordinate
from lib.board import Board

class Body():
    def __init__(self, our_color):
        self._our_color = our_color
        self._board = Board(our_color)
        self.start_game()


    def start_game(self):
        if(self._our_color == Color.WHITE):
            self.make_move()

    #Called by the IO manager whenever the enemy makes a move. 
    def enemy_made_move(self, piece):
        self._board.add_piece(piece)
        self.make_move(piece)

    #Sends the current board state to the brain, gets a move back, and makes it
    def make_move(self, piece):
        print("Make move")
        #our_move = brain.get_next_move(self._board)
        #io_manager.write_move(our_move)
