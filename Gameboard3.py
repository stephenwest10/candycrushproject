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
            self.board[monos[i][1]][monos[i][0]] = 0

        # Clear all zeroes
        for i in range(self.height):  
            indicies = [idx for idx, n in enumerate(self.board[i]) if n == 0]
            indicies.reverse() # work backwards from the end for gravity purposes
            for idx in indicies:
                self.board[i].pop(idx)
                
        # Do gravity
        for i in range(0, self.height):
            f = self.width - len(self.board[i])
            self.board[i] = self.board[i] + [random.randint(1, self.numColors) for k in range(f)]
        if len(self.getMonos()) > 0:
            self.clearBoard()

    #These are horizontal on our board but vertical compared to gravity
    def getVerticalMonos(self):
        monos = []
        for y in range(0, self.height):
            x = 0
            
            while x < self.width - 1:
                color = self.board[y][x]
                streak = 1 

                while x + streak < self.width and self.board[y][x + streak] == color:
                    streak += 1
                if streak >= 3:
                    for i in range(0, streak):
                        monos.append([x + i, y])
                x += streak 
        return monos

    #vertical on our board but horizontal compared to gravity
    def getHorizontalMonos(self):
        monos = []
        for x in range(0, self.width):
            y = 0
            while y < self.height - 1:
                color = self.board[y][x]
                streak = 1 

                while y + streak < self.height and self.board[y + streak][x] == color:
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
                swap1 = self.board[y][x]
                swap2 = self.board[y][x+1]
                self.board[y][x] = swap2    
                self.board[y][x+1] = swap1
                
                if len(self.getMonos()) > 0:
                    moves.append([[x, y], [x + 1, y]])

                # Revert the move
                self.board[y][x] = swap1
                self.board[y][x+1] = swap2
        return moves

    def getPossibleHorizontalMoves(self):
        moves = []
        for x in range(0, self.width):
            for y in range(0, self.height - 1):
                swap1 = self.board[y][x]
                swap2 = self.board[y+1][x]
                self.board[y][x] = swap2    
                self.board[y+1][x] = swap1
                
                if len(self.getMonos()) > 0:
                    moves.append([[x, y], [x, y + 1]])

                # Revert the move
                self.board[y][x] = swap1
                self.board[y+1][x] = swap2
        return moves

    def getPossibleMoves(self):
        #moves = self.getPossibleVerticalMoves() + self.getPossibleHorizontalMoves()
        #print moves
        #moveSorted = sorted(moves, key=lambda x: x[0][0])
        #print moveSorted
        return self.getPossibleVerticalMoves() + self.getPossibleHorizontalMoves()

    def gameOver(self):
        return len(self.getPossibleMoves()) == 0

    def doMove(self, move):
        swap = self.board[move[0][1]][move[0][0]]
        self.board[move[0][1]][move[0][0]] = self.board[move[1][1]][move[1][0]]
        self.board[move[1][1]][move[1][0]] = swap
        self.clearBoard()
        #pprint(self.board)
        self.gameLength += 1
    
#playing from the top
def topStrat(game):
    moves = game.getPossibleMoves()
    moveSorted = sorted(moves, key=lambda x: x[0][0])
    return moveSorted[-1] 
    #may seem counter-intuitive, but our gravity works from the right
    #the monos at the top are those furthest along the board
    #although our mono-checker works as if it was vertical, we log the position as if it was horizontal
    #Thus, this sorting key is the correct one
    #one can test this by printing the board while playing the game

#playing from the bottom
def bottomStrat(game):
    moves = game.getPossibleMoves()
    moveSorted = sorted(moves, key=lambda x: x[0][0])
    return moveSorted[0]

#pLaying randomly
def randomStrat(game):
    return game.getPossibleMoves()[random.randint(0, len(game.getPossibleMoves())-1)]


def playGame(game, ITERATIONS, strategy):  #Iterations is the number of times you play the game
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
        gameLengths.append(game.gameLength)
        for a in range(0, len(numMovesAvailable)-1):
            delta = numMovesAvailable[a+1] - numMovesAvailable[a]
            deltaChangeByChainPosition[numMovesAvailable[a]].append(delta)
        print "Game", i, "length:", game.gameLength
        
    print gameLengths # so I can collect the game length data, this writes it to a text file.
    data = open("newRandom15000Data.txt","w+")
    data.write(str(gameLengths))
    data.close()
    summaryAndHistPlot(gameLengths, deltaChangeByChainPosition)
    return gameLengths, deltaChangeByChainPosition
   

def summaryAndHistPlot(gameLengths, deltaChangeByChainPosition):
    print stat.describe(gameLengths)   #Summary Statistics using SciPy
    #how to calculate own summary stats
    print "Mean Game Length:", round(scipy.mean(gameLengths), 3)
    print "Highest Game Length:", max(gameLengths)
    print "Lowest Game Length:", min(gameLengths)
    
    #A graph for the Move Deltas per position in the Chain
    #Can change this list to print out the different line graphs
    for i in [1, 4, 8, 12, 16]:
        #print i, deltaChangeByChainPosition[i] - the output data which we plot
        valuesToPlot = Counter(deltaChangeByChainPosition[i])
        n = len(deltaChangeByChainPosition[i])
        plt.plot(sorted(valuesToPlot.keys()), [valuesToPlot[key]/float(n) for key in sorted(valuesToPlot.keys())], label=str(i)) 
    plt.xlim(-10, 10)
    plt.legend()   
    plt.title("Move Deltas given each Number of Available Moves")
    plt.savefig("Move delta positions TopStrat.png") #Saves our graph in this current directory
    plt.show()

    #The Expected Jump Graph
    chainPos = []
    expectedChange = []
    for j in deltaChangeByChainPosition.keys():
        chainPos.append(j)
        expectedChange.append(stat.tmean(deltaChangeByChainPosition[j])) #note, trimmed mean
    plt.plot(chainPos, expectedChange)
    plt.title("The Expected Change for each Move by Position in the Chain")
    plt.show()
    
    #This plots the Histogram of the game lengths
    plt.hist(gameLengths) 
    plt.axis([0, 100, 0, 50]) 
    #axis([xmin,xmax,ymin,ymax])
    plt.xlabel('Game Length')
    plt.ylabel('Frequency Density') 
    plt.title("Game Lengths when using the strategy of taking a random move in the list") 
    #Change the title depending on the strategy used
    plt.show()

#Enter the number of game iterations and the strategy you want to use
playGame(Game, 15000, randomStrat) 