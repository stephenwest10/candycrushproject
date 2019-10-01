import random, math
x = 8
y = 8
c=4

score = 0
s=6
def Gameboard(x, y):
    col1 = []
    col2 = []
    col3 = []      # this looks so rookie, but lets get it working
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col8 = []
    def col_board(x):
        for i in range(0,x):
            col1.append(random.randint(1,c))    
            col2.append(random.randint(1,c))                              #this really needs tidying and I need to think of a better way
            col3.append(random.randint(1,c))
            col4.append(random.randint(1,c))
            col5.append(random.randint(1,c))
            col6.append(random.randint(1,c))
            col7.append(random.randint(1,c))
            col8.append(random.randint(1,c))

   

    col_board(x)
    
            
            
    board = [col1, col2, col3, col4, col5, col6, col7, col8]   #this is stupidly manual but lets get something working first and come back later    

    print (board[0])
    print (board[1])
    print (board[2])
    print (board[3])
    print (board[4])
    print (board[5])
    print (board[6])
    print (board[7])


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

    

        

    print "Has anything changed?"
    print (board[0])
    print (board[1])
    print (board[2])
    print (board[3])
    print (board[4])
    print (board[5])
    print (board[6])
    print (board[7])

    #board.remove(0)
    #board2 = [1, 2, 3, 4, 5, 6, 7, 8]
    try:
        #board[0] = board[0].remove(0)
        indices = [i for i, x in enumerate(board[0]) if x == 0]
        print indices
        board[0].pop(indices[0])
        board[0].pop(indices[1])
        board[0].pop(indices[2])
    except:
        print "no 0 in line 1"
    try:
        #board[1] = board[1].remove(0)
        indices1 = [i for i, x in enumerate(board[1]) if x == 0]
        print indices1
        board[1].pop(indices1[0])
        board[1].pop(indices1[1])
        board[1].pop(indices1[2])
    except:
        print "no 0 in line 2"
    try:
        #board[2] = board[2].remove(0)
        indices2 = [i for i, x in enumerate(board[2]) if x == 0]
        print indices2
        board[2].pop(indices2[0])
        board[2].pop(indices2[1])
        board[2].pop(indices2[2])
    except:
        print "no 0 in line 3"
    try:
        #board[3] = board[3].remove(0)
        indices3 = [i for i, x in enumerate(board[3]) if x == 0]
        print indices3
        for i in range(0, len(indices3)+1):
            board[3].pop(indices3[i])
        
    except:
        print "no 0 in line 4"
    try:
        #board[4] = board[4].remove(0)
        indices4 = [i for i, x in enumerate(board[4]) if x == 0]
        print indices4
        board[4].pop(indices4[0])
        board[4].pop(indices4[1])
        board[4].pop(indices4[2])
    except:
        print "no 0 in line 5"
    try:
        #board[5] = board[5].remove(0)
        indices5 = [i for i, x in enumerate(board[5]) if x == 0]
        print indices5
        board[5].pop(indices5[0])
        board[5].pop(indices5[1])
        board[5].pop(indices5[2])
    except:
        print "no 0 in line 6"
    try:
        #board[6] = board[6].remove(0)
        indices6 = [i for i, x in enumerate(board[6]) if x == 0]
        print indices6
        board[6].pop(indices6[2])
        board[6].pop(indices6[1])
        board[6].pop(indices6[0])
    except:
        print "no 0 in line 7"
    try:
        #board[7] = board[7].remove(0)
        indices7 = [i for i, x in enumerate(board[7]) if x == 0]
        print indices7
        board[7].pop(indices7[0])
        board[7].pop(indices7[1])
        board[7].pop(indices7[2])
    except:
        print "no 0 in line 8"
    print "Has anything changed?"
    print board[0]
    print board[1]
    print board[2]
    print board[3]
    print board[4]
    print board[5]
    print board[6]
    print board[7]

    
Gameboard(x,y)

















 #def row_board():
     #   for i in range(0,y):
      #      board.append([col_board()])


# from random import randint
# board = []

# for x in range(0,5):
    # board.append(["O"] * 5)

# def print_board(board):
    #for row in board:
       # print " ".join(row)

#def random_row(board):
 #   return randint(0, len(board) - 1)

#def random_col(board):
    # return randint(0, len(board[0]) - 1)

#ship_row = random_row(board)
#ship_col = random_col(board)

#print ship_col
#print ship_row

# Add your code below!
#guess_row = int(raw_input("Guess Row:"))
#uess_col = int(raw_input("Guess Col:"))