import time
import os.path

from color import Color

class Hands():
    print("Made")
    def __init__(self):
    
        #loop:
        started = False
        pollNextMove=False
        myColor = Color.NONE
        
        print("Initialized")
        while(started == False):
            #wait several ms,
            # then poll for move_file            
            time.sleep(1)
            #//TODO: Make the time delay lower

            
            #if exists:
                #init all the things
            if(os.path.isfile("myFileName")):
               started = True
               pollNextMove = True
               print ("Started")
               #//TODO: Start all the things
               


        while(pollNextMove): #Run until game over received
            print("Color: ",myColor)
        #loop:
            #wait several ms
            #poll for our file
            time.sleep(2)
            if(os.path.isfile("move_file")):
            #if exists:
                #read move_file
               with open("move_file", "r") as file:
                   if(myColor == Color.NONE):            
                       file.seek(0)
                       first_char = file.read(1)
                       if not first_char:
                           myColor = Color.WHITE
                       else:
                            file.seek(0)
                            myColor = Color.BLACK
                            
                       
                    #else:
                     #  file.seek(0) #go back to beginning
                   
               
                #if we don't know what color we are:
                    #if empty:
                        #we are first to move (white)
                    #else
                        #we're second to move (black)
                #pass last move to body

#    def write_move(move):
        #open move_file
        #append in our move
        #close file

