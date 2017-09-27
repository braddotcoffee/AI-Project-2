import time
import os.path

from lib.color import Color
from lib.body import Body
from lib.piece import Piece
from lib.coordinate import Coordinate

class Hands():
    
    def __init__(self, color=Color.WHITE, groupname="iron"):
        
        self.pollNextMove = True
        self.groupname = groupname
        self.first_move = True
        self.color = color
        
    def run(self):
        
        while(self.pollNextMove == True):
           
            #wait several ms,
            # then poll for move_file            
            time.sleep(7)
            #//TODO: Make the time delay lower
            
            #if exists:
                #init all the things
            
            if(os.path.isfile(self.groupname + ".go")):

                if(os.path.isfile("end_game")):
                   self.pollNextMove = False
                   break

                print ("Our move!")
                move = Hands.check_move_file()
                #//TODO: Start all the things
                if(self.first_move):
                    self.first_move = False
                    if move: 
                        self.color = Color.BLACK
                        self.body = Body(self.color)
                        self.body.make_move()
                    else: self.color = Color.WHITE


                move = move.split()
                x = Hands.mapLetterToNumber(move[1])
                y = int(move[2])
                enemy_piece = Piece(Color.opposite(self.color), Coordinate(x,y))
                self.body.enemy_made_move(enemy_piece)
                our_move = self.body.make_move()
                self.write_move(move)


                   

    @staticmethod
    def mapLetterToNumber(letter):
        #We assume this only gets called with capital letters
        return ord(letter) - 64

    @staticmethod
    def mapNumberToLetter(number):
        return chr(number + 64)

    @staticmethod
    def check_move_file():
        with open("move_file", "r") as move_file:
            for line in move_file:
                return line

    def write_move(self, move):
        with open("move_file", "w") as file:
            file.write("%s %s %d" % (self.groupname, Hands.mapNumberToLetter(move.x), move.y))
