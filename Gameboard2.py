import random, math
from pprint import pprint

x = 8 #board size
y = 8
c=4

board = [[random.randint(1, c) for i in range(x)] for j in range(y)]   
pprint(board)

def HoriMonoList(b):    #This should print out the horizontal monos on the board 
    Hori = []
    for i in range(0,x):
        position = 0
        
        
        while position < x-1:
            initcol = b[i][position]
            streak = 1 

            while position + streak < x and b[i][position+streak] == initcol:
                streak += 1
                if streak >= 3:
                    newmonopositions = [i, position]
                    Hori.append(newmonopositions)
            position += streak   # need to work on the reporting of the monos - eg for a mono of 6 it will print the position 4 times as the length is 3, 4, 5, 6

            #need to do the same for veritcal and copy in the zero remover etc
            #need to do the move checker and then check if the move is valid and creates more monos
        
                

    print Hori

HoriMonoList(board)