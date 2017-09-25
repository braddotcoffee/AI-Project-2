import time
import os.path

class Hands():
    print("Made")
    #def __init__(self):
    if(True):
        #loop:
        started = False
        pollNextMove=False
        print("Hi")
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
               print ("yes")
               #//TODO: Start all the things
               


        while(pollNextMove):
        #loop:
            #wait several ms
            #poll for our file
            time.sleep(0.5)
            if(os.path.isfile("move_file")):
            #if exists:
                #read move_file
               with open("move_file", "r") as file:
                   for line in file:
                       if not line: #file is empty
                           print("empty")
                           pollNextMove = false
               
               
               
                #if we don't know what color we are:
                    #if empty:
                        #we are first to move
                    #else
                        #we're second to move
                #pass last move to body

#    def write_move(move):
        #open move_file
        #append in our move
        #close file

