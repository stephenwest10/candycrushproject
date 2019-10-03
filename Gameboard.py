import random, math
from pprint import pprint


x = 8 #board size
y = 8
c=4 #number of colours in the game, easier to see the monos if this value is lower

score = 0
s=x-2   # this is causing a bit of a bug with the last column - need to look into this
def Gameboard(x, y):
    board = [[random.randint(1, c) for i in range(x)] for j in range(y)]         
    pprint(board) 
    plist = {} #this is now a dictionary
    plist2 = {}
    for i in range(0,s+1):                  #note that here it does the rows first before it goes through the columns, only relevant when noticing T shape monos
        for j in range(0,s):
            if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2]:
                #board[i][j] = 0
                #board[i][j+1] = 0
                #board[i][j+2] = 0
                plist[i] = [j, j+1, j+2]
                
            
    for j in range(0,s+1):
        for i in range(0,s):
            if board[i][j] == board[i+1][j] and board[i+1][j] == board[i+2][j]:
                #board[i][j] = 0
                #board[i+1][j] = 0
                #board[i+2][j] = 0
                plist2[j] = [i, i+1, i+2]
                #plist2[j] = plist2 + position2
                
         
    print 'the horizontal monos are here: ', plist, 'and the vertical monos are here: ', plist2
    print "Has anything changed?"  # just printing to see if it works - will delete later
    pprint(board)

    for i in range(x):
        indicies = [idx for idx, n in enumerate(board[i]) if n == 0]
        indicies.reverse() # work backwards from the end
        print "Indicies: " + str(indicies)
        for idx in indicies:
            board[i].pop(idx)
            
    print "Has anything changed?"  # the 0s should have been removed here
    pprint(board)


    for i in range(0, x):
        f = x - len(board[i])
        extras = [random.randint(1, c) for k in range(f)]
        print extras #just to give a visual on what is happening
        board[i] = board[i] + extras

    pprint(board)
    # this works nicely up to this point - the next step is to work out how to test a 'move'
    # function for 
Gameboard(x,y)


def Monochecker():
     for i in range(0,s):                  #note that here it does the rows first before it goes through the columns, only relevant when noticing T shape monos
        for j in range(0,s):
            if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2]:
                return board.index(i, j)
def locationfinder():
    for i in range(0, x):
        location = [idx for idx, n in enumerate(board[i]) if n == 0]
        print "Indicies: " + str(location)