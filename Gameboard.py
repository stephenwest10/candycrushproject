import random, math
from pprint import pprint


x = 8 #board size
y = 8
c=4 #number of colours in the game, easier to see monos if lower

score = 0
s=6 # 2 below the length of the row for the if statements below hard coded for now
def Gameboard(x, y):
    board = [[random.randint(1, c) for i in range(x)] for j in range(y)]         
    pprint(board) 

    for i in range(0,s):                         #note that here it does the rows first before it goes through the columns, only relevant when noticing T shape monos
        for j in range(0,s):
            if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2]:
                board[i][j] = 0
                board[i][j+1] = 0
                board[i][j+2] = 0
    for j in range(0,s):
        for i in range(0,s):
            if board[i][j] == board[i+1][j] and board[i+1][j] == board[i+2][j]:
                board[i][j] = 0
                board[i+1][j] = 0
                board[i+2][j] = 0

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

    
Gameboard(x,y)