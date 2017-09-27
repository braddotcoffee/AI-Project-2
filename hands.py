import time
import os.path

from lib.color import Color
from lib.body import Body
from lib.piece import Piece
from lib.coordinate import Coordinate

class Hands():
    print("Made")
    def __init__(self):
        
    
        makeFirstMove = False
        pollNextMove = True
        myColor = Color.NONE
        
        print("Initialized")
        while(pollNextMove == True):
           
            #wait several ms,
            # then poll for move_file            
            time.sleep(2)
            #//TODO: Make the time delay lower
            
            #if exists:
                #init all the things
            
            if(os.path.isfile("myFileName")):
                print ("Our move!")
                #//TODO: Start all the things
                if(makeFirstMove == True):
                    myBody.start_game(myColor)
                    continue

                if(os.path.isfile("move_file")):
                    with open("move_file", "r") as file:
                        if(myColor == Color.NONE):            
                            #This is the first move of the game
                            file.seek(0)
                            first_char = file.read(1)
                            if not first_char:
                                myColor = Color.WHITE
                                myBody = Body(myColor)

                                #Put this in a flag so we don't do it with the file open
                                makeFirstMove = True
                                continue
                            else:
                                 myColor = Color.BLACK
                                 myBody = Body(myColor)
                            file.seek(0)
                            #Initialize all the code here

                        moveString = file.readline()
                        print ("moveString = " + moveString)
                        
                    #File is closed so they don't yell at us
                    #I thought the indices would be -3 and -1, but it seems there's a newline
                        #character at the end. I'm hoping this isn't a CRLF Windows thing.
                        #It might be safer to get the character after the first space and
                        #after the second space.
                    print("column letter: " + moveString[-4])
                    theirColor = Color.opposite(myColor)
                    theirX = self.mapLetterToNumber(moveString[-4])
                    theirY = int(moveString[-2])

                    print("Their X: " + str(theirX))
                    print("Their Y: " + str(theirY))
                        
                    newPiece = Piece(theirColor, Coordinate(theirX,theirY))
                    #pass last move to body
                    myBody.make_move(newPiece)

    def mapLetterToNumber(self,letter):
        #We assume this only gets called with capital letters
        return ord(letter) - 64
    def write_move(self,move):
         #open move_file
         with open("move_file", "r") as file:
             
         #append in our move
         #close file
