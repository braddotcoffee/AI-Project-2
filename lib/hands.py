import time
import os.path

from color import Color

class Hands():
    print("Made")
    def __init__(self):
    
        #loop:
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

            if(os.path.isfile("move_file")):

                with open("move_file", "r") as file:
                   if(myColor == Color.NONE):            
                       #This is the first move of the game
                       file.seek(0)
                       first_char = file.read(1)
                       if not first_char:
                           myColor = Color.WHITE
                       else:
                            myColor = Color.BLACK
                       file.seek(0)
                       #Initialize all the code here
                    
                    
                #pass last move to body

#    def write_move(move):
        #open move_file
        #append in our move
        #close file

