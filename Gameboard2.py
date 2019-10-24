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
                    for a in range(0, streak):
                        newmonopositions = [i, position+a]  #for monos greater than 3 it repeats the positons again, okay for now but probably should work out a fix
                        Hori.append(newmonopositions)
            position += streak   # need to work on the reporting of the monos - eg for a mono of 6 it will print the position 4 times as the length is 3, 4, 5, 6
    print "Horizontal Monos: ", Hori
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
                        newmonopositions = [position+a, j]  #for monos greater than 3 it repeats the positons again, okay for now but probably should work out a fix
                        Vert.append(newmonopositions)
            position += streak 
    print "Vertical Monos: ", Vert
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



#def ValidMoveList(b, m):        #this is for a board with no monos - come back later
 #   m = HoriMonoList(b) + VertMonoList(b)
 #   for i in range(0, x):
  ##      for j in range(0, y):
  #          swap1 = b[i][j]
   #         swap2 = b[i+1][j]
   #         b[i][j] = swap2     #this is a horizontal move - probably a better way
    #        b[i+1][j] = swap1
     #       New_M = 



#HoriMonoList(board)
#VertMonoList(board)
MonoZero(board, HoriMonoList(board), VertMonoList(board))
print "Zeroes should go"
ZeroRemover(board)
print "Gravity should occur and board should reset"
BoardGravity(board)