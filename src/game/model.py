import numpy as np
import enum

class Model:
    def __init__(self):

        #Initializing the empty board
        self.board = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,-1,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])

    # Sets the piece of the specified color on the board and flips all of the appropriate tiles
    def setPiece(self,row,col,color):
        for h in range(-1,2):
            for v in range(-1,2):
                self.flipColors(row,col,color,h,v)
        self.board[row][col] = color

        # print(self.board)

    # Flips all of the appropriate tiles in a certain direction
    def flipColors(self,row,col,color,horizontal,vertical):
        if(self.isValidFlip(row,col,color,horizontal,vertical)):

            r = row+vertical
            c = col+horizontal

            while(self.board[r][c] == -1*color):
                self.board[r][c] = color
                r += vertical
                c+= horizontal

    # Checks if a certain direction from a spot qualifies a move as valid
    def isValidFlip(self,row,col,color,horizontal,vertical):

        if (self.board[row][col] != 0):
            return False;

        firstTile = (self.isValidPosition(row+vertical,col+horizontal) and self.board[row+vertical][col+horizontal] == -1*color)

        if(not firstTile):
            return False

        r = row+vertical
        c = col+horizontal

        while(r >= 0 and r < 8 and c >= 0 and c < 8):

            if(self.board[r][c] == 0):
                return False;
            elif(self.board[r][c] == color):
                return True;
            else:
                r += vertical
                c+= horizontal

        return False;

    # Checks if a position is on the board or not
    def isValidPosition(self,row,col):
        return not(row < 0 or col < 0 or row > 7 or col > 7)

    # Returns a list of all the valid moves for a certain color
    def getValidMoves(self,color):
        moves = []

        for r in range(0,8):
            for c in range(0,8):
                if(self.checkSpot(r,c,color)):
                    moves.append([r,c])

        return moves

    # Checks if a single spot is a valid placement for a piece
    def checkSpot(self,r,c,color):

        if(self.board[r][c] != 0):
            return False;

        for h in range(-1, 2):
            for v in range(-1, 2):
                if (self.isValidFlip(r,c,color,h,v)):
                    return True

        return False


class Color(enum.Enum):
    black = -1
    white = 1


class Direction(enum.Enum):
    right = 1
    left = -1
    up = 1
    down = -1
    straight = 0
