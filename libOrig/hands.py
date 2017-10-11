import time
import os.path
import random

from lib.color import Color
from lib.body import Body
from lib.piece import Piece
from lib.coordinate import Coordinate

class Hands():
    
    def __init__(self, color=Color.WHITE, groupname="golem"):
        
        self.pollNextMove = True
        self.groupname = groupname
        self.first_move = True
        self.color = color
        self.mids = [Coordinate(7,7), Coordinate(7,8), Coordinate(8,7), Coordinate(8,8)]
        
    def run(self):
        
        while(self.pollNextMove):
           
            #wait several ms,
            # then poll for move_file            
            time.sleep(0.5)
            #//TODO: Make the time delay lower
            
            if(os.path.isfile(self.groupname + ".go")):

                if(os.path.isfile("end_game")):
                   self.pollNextMove = False
                   break

                enemy_move = Hands.check_move_file()
                #//TODO: Start all the things
                if(self.first_move):
                    self.first_move = False
                    if enemy_move: 
                        self.color = Color.BLACK
                        self.body = Body(self.color)
                    else: # Executes one at most
                        self.color = Color.WHITE
                        self.body = Body(self.color)
                        self.write_move(self.mids[random.randint(0,3)])
                        continue

                # Normal Gameflow
                enemy_move = enemy_move.split()
                x = Hands.mapLetterToNumber(enemy_move[1])
                y = int(enemy_move[2])
                enemy_piece = Piece(Color.opposite(self.color), Coordinate(x,y))
                self.body.enemy_made_move(enemy_piece)
                our_move = self.body.make_move()
                self.write_move(our_move)
                time.sleep(3)


                   

    @staticmethod
    def mapLetterToNumber(letter):
        return ord(letter) - 96

    @staticmethod
    def mapNumberToLetter(number):
        return chr(number + 96)

    @staticmethod
    def check_move_file():
        with open("move_file", "r") as move_file:
            for line in move_file:
                return line

    def write_move(self, move):
        with open("move_file", "w") as file:
            file.write("%s %s %d" % (self.groupname, Hands.mapNumberToLetter(move.x), move.y))
