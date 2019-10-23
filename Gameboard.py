import random, math
from pprint import pprint


x = 8 #board size
y = 8
c=4 #number of colours in the game, easier to see the monos if this value is lower

score = 0
s=x-2  
board = [[random.randint(1, c) for i in range(x)] for j in range(y)]     
plist = {} #this is now a dictionary - thought was that it would be useful to find exactly where each mono was in a column/row
plist2 = {} 
mlist = {}      #massive issue here is that I have too many globals
mlist2 = {}
mlist3 = {}
mlist4 = {}   
chain = 0  # my intial thoughts into the chain reaction
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
def HoriMonoList(b):
    Hori = []
    for i in range(0,x):
        position = 0
        while position < x:
            initcol = b[i][position]
            streak = 0 
            while b[i][position + streak] == initcol and position + streak <= x:
                streak += 1
                if streak >= 3:
                    for j in range(streak + 1):
                        newmonopositions = [(i, j)] 
                    Hori.append(newmonopositions)
                    position += streak
    print Hori


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
            #print "Indicies: " + str(indicies)
            for idx in indicies:
                board[i].pop(idx)

def BoardGravity():
    for i in range(0, x):
        f = x - len(board[i])
        extras = [random.randint(1, c) for k in range(f)]
        #print extras #just to give a visual on what is happening
        board[i] = board[i] + extras

def MoveChecker():
    # check horizontally and vertically, and then print in to a list to start with
        for i in range(0,x):                
            for j in range(0,s):
                try: 
                    if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+3]:
                        mlist[i] = [j+2, j+3]
                except:
                    a=1    # need to read up documentation on try and except - basically we risk that we evaluate values out of range
                try:
                    if board[i][j] == board[i][j+2] and board[i][j+2] == board[i][j+3]:
                        mlist2[i] = [j, j+1]
                except: 
                    a=1 # some dummy variable for now - just until I can think of something to put there
        for j in range(0,x):                
            for i in range(0,s):
                try:
                    if board[i][j] == board[i+1][j] and board[i+2][j] == board[i+3][j]:
                        mlist3[j] = [i+2, i+3]
                except:
                    a=1
                try: 
                    if board[i][j] == board[i+2][j] and board[i+2][j] == board[i+3][j]:
                        mlist4[j] = [i, i+1]  # needs more thought
                except:
                    a=1
        print 'the horizontal moves to be made are here (row: [position to swap]): ', mlist, " and here:", mlist2, 'and the vertical moves are here (column: [position to swap]): ', mlist3, 'and here: ', mlist4

def HoriMoveMaker():
    for key in mlist:
        print "check row(s): ", mlist.keys()
        board[key][mlist[key][0]], board[key][mlist[key][1]] = board[key][mlist[key][1]], board[key][mlist[key][0]]
        pprint(board)
    for key in mlist2:
        print "check row(s): ", mlist2.keys()
        board[key][mlist2[key][0]], board[key][mlist2[key][1]] = board[key][mlist2[key][1]], board[key][mlist2[key][0]]
        pprint(board)

def Gameboard(x, y):
    #plist.clear() #reset this variable for when it loops - otherwise you delete non monos
    #plist2.clear()
    #Monochecker()
    HoriMonoList(board)
    #ZeroMonos()
    #pprint(board)
      
    #ZeroRemover()       
    #print "Zeroes removed"  # the 0s should have been removed here
    #pprint(board)

    #BoardGravity()
    #print "this next board should be reset (unless chain reaction)"
    #pprint(board)


    
Gameboard(x,y)
# The loop to deal with chain reactions - for now - need to reconsider when add moves
#while chain < 1: 
    #Gameboard(x,y)

#MoveChecker()

#HoriMoveMaker()
#chain = 0  # really need to think of a better way to do this - come back later
#Gameboard(x,y)

#while chain < 1: 
#    Gameboard(x,y)





# horizontal checking works perfectly, need to think of a way to precisely locate verticals
# issue with reporting vertical moves which require a change of column - this may be a pain later


# have built a function which makes all the horizontal moves for now, but need to put more thought into vertical

# still have the situation that it only removes mono runs of 3 and unsure what to do if it is a 4
    

