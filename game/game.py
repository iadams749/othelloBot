import numpy as np
from game import model
from random import *

class Game:
    def __init__(self):
        self.model = model.Model()
        self.turn = -1
        self.gameOver = False
        self.lastMove = []

    def getValidMoves(self):
        return self.model.getValidMoves(self.turn)

    def doTurn(self,row,col):
        self.model.setPiece(row,col,self.turn)
        self.lastMove = [row,col,self.turn]

        self.turn = self.turn * -1
        if(len(self.getValidMoves()) == 0):
            self.turn = self.turn * -1

        if(len(self.getValidMoves()) == 0):
            self.gameOver = True

    def getBoard(self):
        return self.model.board

    def playGamePrinted(self):
        while(not self.gameOver):

            turn = "Color"

            if(self.turn == 1):
                turn = "White"
            else:
                turn = "Black"

            print(self.model.board)
            print(f"Current turn: {turn}")
            print(f"Possible moves: {self.getValidMoves()}")
            row = int(input("Row: "))
            col = int(input("Column: "))

            self.doTurn(row,col)

        print(self.model.board)
        print(f"Final score: {self.calcScore()}")
        if(self.calcScore() > 0):
            print("Winner: White")
        elif(self.calcScore() < 0):
            print("Winner: Black")
        else:
            print("Tie")


    def playGamePrintedAuto(self):
        while(not self.gameOver):

            turn = "Color"

            if(self.turn == 1):
                turn = "White"
            else:
                turn = "Black"

            print(self.model.board)
            print(f"Current turn: {turn}")
            print(f"Possible moves: {self.getValidMoves()}")
            print(f"Current score: {self.calcScore()}")
            print(f"Last move: {self.lastMove}")
            moves = self.getValidMoves()
            position = moves[randint(0, len(moves)-1)]

            self.doTurn(position[0],position[1])

        print(self.model.board)
        print(f"Final score: {self.calcScore()}")
        print(f"Last move: {self.lastMove}")
        if (self.calcScore() > 0):
            print("Winner: White")
        elif (self.calcScore() < 0):
            print("Winner: Black")
        else:
            print("Tie")

    def playGameAuto(self):
        while (not self.gameOver):
            moves = self.getValidMoves()
            position = moves[randint(0, len(moves) - 1)]

            self.doTurn(position[0], position[1])

    def calcScore(self):
        sum = 0

        for r in range(0,8):
            for c in range(0,8):
                sum += self.model.board[r][c]

        return sum

    def playRandomMove(self):
        moves = self.getValidMoves()
        position = moves[randint(0, len(moves) - 1)]

        self.doTurn(position[0], position[1])


