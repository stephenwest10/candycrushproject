import random, math
from pprint import pprint

x = 8 #board size
y = 8
c=8

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
                    for a in range(0, streak):
                        newmonopositions = [i, position+a]  #for monos greater than 3 it repeats the positons again, okay for now but probably should work out a fix
                        Hori.append(newmonopositions)
            position += streak   # need to work on the reporting of the monos - eg for a mono of 6 it will print the position 4 times as the length is 3, 4, 5, 6
    #print "Horizontal Monos: ", Hori
    return Hori
    
            
            #need to do the same for veritcal and copy in the zero remover etc
            #need to do the move checker and then check if the move is valid and creates more monos
        
def VertMonoList(b):    #This should print out the horizontal monos on the board 
    Vert = []
    for j in range(0,y):
        position = 0
        
        
        while position < x-1:
            initcol = b[position][j]
            streak = 1 

            while position + streak < x and b[position+streak][j] == initcol:
                streak += 1
                if streak >= 3:
                    for a in range(0, streak):
                        newmonopositions = [position+a, j]  #for monos greater than 3 it repeats the positons again, its fine as it just zeroes the value twice, only a problem if one wanted to print out the list of monos
                        Vert.append(newmonopositions)
            position += streak 
    #print "Vertical Monos: ", Vert
    return Vert
    

def MonoZero(b, m1, m2):
    m = m1 + m2
    for i in range(0, len(m)):
        b[m[i][0]][m[i][1]] = 0

    pprint(b)

def ZeroRemover(b):
        for i in range(x):  
            indicies = [idx for idx, n in enumerate(b[i]) if n == 0]
            indicies.reverse() # work backwards from the end for gravity purposes
            for idx in indicies:
                b[i].pop(idx)
        pprint(b)

def BoardGravity(b):
    for i in range(0, x):
        f = x - len(b[i])
        newvalues = [random.randint(1, c) for k in range(f)]
        b[i] = b[i] + newvalues
    pprint(b)



def ValidVertMoveList(b):        #to be called on a clean board
    ValidVertMoves = []
    for i in range(0, x-1):
        for j in range(0, y):
            swap1 = b[i][j]
            swap2 = b[i+1][j]
            b[i][j] = swap2    
            b[i+1][j] = swap1
            if len(HoriMonoList(b)+VertMonoList(b)) > 0:
                new_move = [i, j], [i+1, j]
                ValidVertMoves.append(new_move)
            b[i][j] = swap1      #reverting the move
            b[i+1][j] = swap2
    pprint(b)
    print "possible vertical moves:", ValidVertMoves
    print "number of vertical moves:", len(ValidVertMoves)
    return ValidVertMoves

def ValidHoriMoveList(b):        #to be called on a clean board
    ValidHoriMoves = []
    for i in range(0, x):
        for j in range(0, y-1):
            swap1 = b[i][j]
            swap2 = b[i][j+1]
            b[i][j] = swap2    
            b[i][j+1] = swap1
            if len(HoriMonoList(b)+VertMonoList(b)) > 0:
                new_move = [i, j], [i, j+1]
                ValidHoriMoves.append(new_move)
            b[i][j] = swap1      #reverting the move
            b[i][j+1] = swap2
    pprint(b)
    print "possible horizontal moves:", ValidHoriMoves
    print "number of horizontal moves:", len(ValidHoriMoves)
    return ValidHoriMoves

def CleanGameboard():
    MonoZero(board, HoriMonoList(board), VertMonoList(board))
    print "Zeroes should go"
    ZeroRemover(board)
    print "Gravity should occur and board should reset"
    BoardGravity(board) 
    if len(HoriMonoList(board)+VertMonoList(board)) > 0:  #to catch chain reaction monos
        CleanGameboard()
    
CleanGameboard()

ValidVertMoveList(board)
ValidHoriMoveList(board)


# next steps - which move to implement? 
# Build some form of turn counter etc to model the number of turns left in the game to compare to ehrenfest etc
# I suppose strategies would be to pick the ones with the lowest x,y co-ords to get a move near the top of our board

