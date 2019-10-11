import random, math
from pprint import pprint


x = 8 #board size
y = 8
c=4 #number of colours in the game, easier to see the monos if this value is lower

score = 0
s=x-2   # this is causing a bit of a bug with the last column - need to look into this
board = [[random.randint(1, c) for i in range(x)] for j in range(y)]     
plist = {} #this is now a dictionary
plist2 = {} 
mlist = {}
mlist2 = {}
mlist3 = {}
mlist4 = {}   
chain = 0
pprint(board) 
def Monochecker():

    for i in range(0,x):                
        for j in range(0,s):
            if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2]:
                plist[i] = [j, j+1, j+2]
                
            
    for j in range(0,x):
        for i in range(0,s):
            if board[i][j] == board[i+1][j] and board[i+1][j] == board[i+2][j]:
                plist2[j] = [i, i+1, i+2]
                
    if plist == {} and plist2 == {}:
        print "No more monos to be found"   
        global chain
        chain += 1         
    print 'the horizontal monos are here (row number and horizontal position): ', plist, 'and the vertical monos are here (column number and vertical position): ', plist2

def ZeroMonos():

    #horizontally
    for key in plist:
        board[key][plist[key][0]] = 0
        board[key][plist[key][1]] = 0
        board[key][plist[key][2]] = 0
    #vertically
    for key in plist2:
        board[plist2[key][0]][key] = 0
        board[plist2[key][1]][key] = 0
        board[plist2[key][2]][key] = 0
    print "we have now zeroed the monos"

def ZeroRemover():
        for i in range(x):  # maybe this x value needs to change at some point
            indicies = [idx for idx, n in enumerate(board[i]) if n == 0]
            indicies.reverse() # work backwards from the end
            print "Indicies: " + str(indicies)
            for idx in indicies:
                board[i].pop(idx)

def BoardGravity():
    for i in range(0, x):
        f = x - len(board[i])
        extras = [random.randint(1, c) for k in range(f)]
        print extras #just to give a visual on what is happening
        board[i] = board[i] + extras

def MoveChecker():
    # check horizontally and vertically, and then print in to a list to start with
        for i in range(0,x):                
            for j in range(0,s):
                try: 
                    if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+3]:
                        mlist[i] = [j+2, j+3]
                except:
                    print "Unsure what is happening"
                try:
                    if board[i][j] == board[i][j+2] and board[i][j+2] == board[i][j+3]:
                        mlist2[i] = [j, j+1]
                except: 
                    print 'out of range?'
        for j in range(0,x):                
            for i in range(0,s):
                try:
                    if board[i][j] == board[i+1][j] and board[i+2][j] == board[i+3][j]:
                        mlist3[j] = [i+2, i+3]
                except:
                    print 'out of range vertical'
                try: 
                    if board[i][j] == board[i+2][j] and board[i+2][j] == board[i+3][j]:
                        mlist4[j] = [i, i+1]
                except:
                    print 'out of range vertical?'
        print 'the horizontal moves to be made are here: ', mlist, " and here:", mlist2, 'and the vertical moves are here: ', mlist3, 'and here: ', mlist4
    
def Gameboard(x, y):
    plist.clear() #reset this variable for when it loops - otherwise you delete non monos
    plist2.clear()
    Monochecker()
    ZeroMonos()
    pprint(board)
      
    ZeroRemover()       
    print "Has anything changed?"  # the 0s should have been removed here
    pprint(board)

    BoardGravity()
    
    pprint(board)


    
Gameboard(x,y)
# The loop to deal with chain reactions - for now - need to reconsider when add moves
while chain < 1: 
    Gameboard(x,y)

MoveChecker()



    

