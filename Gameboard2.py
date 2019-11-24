import random, math
import matplotlib.pyplot as plt
from pprint import pprint

x = 8 #board size
y = 8
c=8

board = [[random.randint(1, c) for i in range(x)] for j in range(y)]   
pprint(board)

def HoriMonoList(b):     
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
    
            
        
def VertMonoList(b):    
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
                new_move = [[i, j], [i+1, j]]
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
                new_move = [[i, j], [i, j+1]]
                ValidHoriMoves.append(new_move)
            b[i][j] = swap1      #reverting the move
            b[i][j+1] = swap2
    pprint(b)
    print "possible horizontal moves:", ValidHoriMoves
    print "number of horizontal moves:", len(ValidHoriMoves)

    return ValidHoriMoves

def BasicStrat(b, m):
   #this strategy would just use the 0th move in the total list each time, stick to just horizontal moves for now
    swap1 = b[m[0][0][0]][m[0][0][1]]   # not working, idk why!!!!
    swap2 = b[m[0][1][0]][m[0][1][1]]
    b[m[0][0][0]][m[0][0][1]] = swap2
    b[m[0][1][0]][m[0][1][1]] = swap1     #list of lists of lists hence all the indices - will be an easier way
    pprint(b)
    return b

def CleanGameboard():
    MonoZero(board, HoriMonoList(board), VertMonoList(board))
    print "Zeroes should go"
    ZeroRemover(board)
    print "Gravity should occur and board should reset"
    BoardGravity(board)
    ValidVertMoveList(board)
    ValidHoriMoveList(board) 
    if len(HoriMonoList(board)+VertMonoList(board)) > 0:  #to catch chain reaction monos
        CleanGameboard()
    
listoflengths = []
num = 0  # maybe this is okay to have as a global
while num < 5:       # really really really need to put this in a class
    x = 8 #board size
    y = 8   # these need to go into a fucntion or a class or something
    c=8

    board = [[random.randint(1, c) for i in range(x)] for j in range(y)]   
    pprint(board)
    CleanGameboard()

    gamelength = 0        
    while len(ValidHoriMoveList(board)+ValidVertMoveList(board)) > 0:
        BasicStrat(board, ValidHoriMoveList(board) + ValidVertMoveList(board))
        gamelength += 1
        CleanGameboard()
        
    print "Length", gamelength
    listoflengths.append(gamelength)
    num += 1
print listoflengths

#this plots the histogram of the lengths
plt.hist(listoflengths) 
plt.axis([0, 50, 0, 10]) 
#axis([xmin,xmax,ymin,ymax])
plt.xlabel('Game Length')
plt.ylabel('Frequency Density')
plt.title("Game Lengths when using the basic strategy of taking the first move in the list")
plt.show()

# To do

# clean this up - need to put it in a class - OOP
# try and get a distribution of the lengths - just need to run for a long time
# perhaps we can compare this data to the ehrenfest model - need to ask
# need a move implementer and then the distribution for turn lengths
# Need to write up some stuff on Markov chains simple birth-death process - solving, first step decomposition
# expected time to absorption - first step simultaneous linear equations, n=3, n=4, n=5, then take more general
