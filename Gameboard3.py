import random, math, scipy, numpy
import matplotlib.pyplot as plt
import scipy.stats as stat
from pprint import pprint
from collections import Counter, defaultdict

class Game:
    def __init__(self, width, height, numColors):
        self.width = width
        self.height = height
        self.numColors = numColors
        self.gameLength = 0

        self.board = [[random.randint(1, numColors) for i in range(width)] for j in range(height)]
        self.clearBoard()

    def clearBoard(self):
        monos = self.getMonos()

        #Zero all monos
        for i in range(0, len(monos)):
            self.board[monos[i][0]][monos[i][1]] = 0

        # Clear all zeroes
        for i in range(self.width):  
            indicies = [idx for idx, n in enumerate(self.board[i]) if n == 0]
            indicies.reverse() # work backwards from the end for gravity purposes
            for idx in indicies:
                self.board[i].pop(idx)
                
        # Do gravity
        for i in range(0, self.width):
            f = self.width - len(self.board[i])
            self.board[i] = self.board[i] + [random.randint(1, self.numColors) for k in range(f)]

        if len(self.getMonos()) > 0:
            self.clearBoard()

    def getVerticalMonos(self):
        monos = []
        for y in range(0, self.width):
            x = 0
            
            while x < self.height - 1:
                color = self.board[x][y]
                streak = 1 

                while x + streak < self.width and self.board[x + streak][y] == color:
                    streak += 1
                if streak >= 3:
                    for i in range(0, streak):
                        monos.append([x + i, y])
                x += streak 
        return monos

    def getHorizontalMonos(self):
        monos = []
        for x in range(0, self.width):
            y = 0
            while y < self.height - 1:
                color = self.board[x][y]
                streak = 1 

                while y + streak < self.height and self.board[x][y + streak] == color:
                    streak += 1
                    if streak >= 3:
                        for i in range(0, streak):
                            monos.append([x, y + i])
                y += streak
        return monos

    def getMonos(self):
        return self.getVerticalMonos() + self.getHorizontalMonos()

    def getPossibleVerticalMoves(self):
        moves = []
        for x in range(0, self.width - 1):
            for y in range(0, self.height):
                swap1 = self.board[x][y]
                swap2 = self.board[x + 1][y]
                self.board[x][y] = swap2    
                self.board[x + 1][y] = swap1
                
                if len(self.getMonos()) > 0:
                    moves.append([[x, y], [x + 1, y]])

                # Revert the move
                self.board[x][y] = swap1
                self.board[x + 1][y] = swap2
        return moves

    def getPossibleHorizontalMoves(self):
        moves = []
        for x in range(0, self.width):
            for y in range(0, self.height - 1):
                swap1 = self.board[x][y]
                swap2 = self.board[x][y + 1]
                self.board[x][y] = swap2    
                self.board[x][y + 1] = swap1
                
                if len(self.getMonos()) > 0:
                    moves.append([[x, y], [x, y + 1]])

                # Revert the move
                self.board[x][y] = swap1
                self.board[x][y + 1] = swap2

        return moves

    def getPossibleMoves(self):
        return self.getPossibleVerticalMoves() + self.getPossibleHorizontalMoves()
        #temporary
        print self.getPossibleVerticalMoves() + self.getPossibleHorizontalMoves()

    def gameOver(self):
        return len(self.getPossibleMoves()) == 0

    def doMove(self, move):
        swap = self.board[move[0][0]][move[0][1]]
        self.board[move[0][0]][move[0][1]] = self.board[move[1][0]][move[1][1]]
        self.board[move[1][0]][move[1][1]] = swap
        self.clearBoard()
        self.gameLength += 1
    
#playing from the top
def topStrat(game):
    moves = game.getPossibleMoves()
    moveSorted = sorted(moves, key=lambda x: x[0][0])
    return moveSorted[-1]  #may seem counter-intuitive, but our gravity works from the right, so the monos at the top are those furthest along the board
#playing from the bottom
def bottomStrat(game):
    moves = game.getPossibleMoves()
    moveSorted = sorted(moves, key=lambda x: x[0][0])
    return moveSorted[0]

#PLaying randomly
def randomStrat(game):
    return game.getPossibleMoves()[random.randint(0, len(game.getPossibleMoves())-1)]


def playGame(game, ITERATIONS, strategy):   #Iterations is the number of times you play the game, inputted at the end
    gameLengths = []
    deltaChangeByChainPosition = defaultdict(list)
    for i in range(ITERATIONS):
        game = Game(8, 8, 8) #defines the game parameters, board size and number of colours
        numMovesAvailable = []
        while not game.gameOver():
            move = strategy(game)     
            game.doMove(move)
            numMovesAvailable.append(len(game.getPossibleMoves()))
            #print game.getPossibleMoves()  #to see if the strategy picks the right move
            #pprint(game.board)  #again to work out if game mechanics are working correctly
        gameLengths.append(game.gameLength)
        for a in range(0, len(numMovesAvailable)-1):
            delta = numMovesAvailable[a+1] - numMovesAvailable[a]
            deltaChangeByChainPosition[numMovesAvailable[a]].append(delta)
        print "Game", i, "length:", game.gameLength
        
    print gameLengths # so I can collect the game length data it writes it to a text file.
    data = open("randomStrat15000data.txt","w+")
    data.write(str(gameLengths))
    data.close()
    summaryAndHistPlot(gameLengths, deltaChangeByChainPosition)
    return gameLengths, deltaChangeByChainPosition
   

def summaryAndHistPlot(gameLengths, deltaChangeByChainPosition):
    print stat.describe(gameLengths)   #summary statistics
    print "Mean Game Length:", round(scipy.mean(gameLengths), 3)
    print "Highest Game Length:", max(gameLengths)
    print "Lowest Game Length:", min(gameLengths)
    #Can change this list to print out the different line graphs
    for i in [1, 4, 8, 12, 16]:
        #print i, deltaChangeByChainPosition[i]
        valuesToPlot = Counter(deltaChangeByChainPosition[i])
        n = len(deltaChangeByChainPosition[i])
        plt.plot(sorted(valuesToPlot.keys()), [valuesToPlot[key]/float(n) for key in sorted(valuesToPlot.keys())], label=str(i)) 
    plt.xlim(-10, 10)
    plt.legend()   
    plt.title("Transition Probability from each number of available moves")
    plt.savefig("Move delta positions.png") #Saves our graph in this current directory
    plt.show()
    
    
    #this plots the histogram of the lengths
    plt.hist(gameLengths) 
    plt.axis([0, 100, 0, 50]) 
    #axis([xmin,xmax,ymin,ymax])
    plt.xlabel('Game Length')
    plt.ylabel('Frequency Density')
    #plt.title("Game Lengths when using the basic strategy of taking the first move in the list")  
    plt.title("Game Lengths when using the random strategy of taking a random move in the list")
    plt.show()

playGame(Game, 1, randomStrat) # Enter the number of games and the strategy you want to use