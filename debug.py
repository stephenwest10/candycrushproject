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
        moves = self.getPossibleVerticalMoves() + self.getPossibleHorizontalMoves()
        print moves
        moveSorted = sorted(moves, key=lambda x: x[0][0])
        print moveSorted
        return self.getPossibleVerticalMoves() + self.getPossibleHorizontalMoves()
       
    def doMove(self, move):
        swap = self.board[move[0][1]][move[0][0]]
        self.board[move[0][1]][move[0][0]] = self.board[move[1][1]][move[1][0]]
        self.board[move[1][1]][move[1][0]] = swap
        self.clearBoard()
        #pprint(self.board)
        self.gameLength += 1
    
    def gameOver(self):
        return len(self.getPossibleMoves()) == 0

def topStrat(game):
    moves = game.getPossibleMoves()
    moveSorted = sorted(moves, key=lambda x: x[0][0])
    return moveSorted[-1]  


game = Game(8, 8, 9)
game.clearBoard()
game.getPossibleMoves()

while not game.gameOver():
    move = topStrat(game)     
    game.doMove(move)
      
