from lib.color import Color
from lib.coordinate import Coordinate
from lib.board import Board
from lib.brain import Brain
from lib.piece import Piece

class Body():
    def __init__(self, our_color):
        self._brain = Brain()
        self._our_color = our_color
        self._board = Board.create_init_board(our_color)
        self.start_game()
        

    def start_game(self):
        if(self._our_color == Color.WHITE):
            self.make_move()

    #Called by the IO manager whenever the enemy makes a move. 
    def enemy_made_move(self, piece):
        self._board.add_piece(piece)
        self.make_move()

    #Sends the current board state to the brain, gets a move back, and makes it
    def make_move(self):
        our_move = self._brain.make_move(self._board)
        self._board.add_piece(Piece(our_move, self._our_color))
        print("\n**\n")
        print(our_move)
        print("\n//**\n")
        
        #Hands.write_move(our_move)
