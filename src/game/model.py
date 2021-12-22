import numpy as np
import enum


class Model:
    def __init__(self):

        # Initilizes board to starting position
        self.board = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, -1, 0, 0, 0],
             [0, 0, 0, -1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])


    def setPiece(self, row, col, color):
        """
        Places a piece on the board and flips the appropriate tiles
        :param row: int representing the row where the piece should be placed
        :param col: int representing the column where the piece should be places
        :param color: a 1 or -1 representing whether the piece being placed is white or black, respectively
        :return: None
        """
        for h in range(-1, 2):
            for v in range(-1, 2):
                self.flipColors(row, col, color, h, v)
        self.board[row][col] = color

    def flipColors(self, row, col, color, horizontal, vertical):
        """
        Flips all of the pieces that are the opposite color of the color provided in a certain direction only if it is a vlid flip
        :param row: int representing the row of the piece being placed
        :param col: int representing the column of the piece being placed
        :param color: 1 or -1 representing whether the piece being placed is white or black, respectively
        :param horizontal: 1, 0 or -1 representing whether the pieces should be flipped moving right, vertically or left, respectively
        :param vertical: 1, 0 or -1 representing whether the pieces should be flipped moving down, horizontally or up, respectively
        :return: None
        """
        if (self.isValidFlip(row, col, color, horizontal, vertical)):

            r = row + vertical
            c = col + horizontal

            while (self.board[r][c] == -1 * color):
                self.board[r][c] = color
                r += vertical
                c += horizontal


    def isValidFlip(self, row, col, color, horizontal, vertical):
        """
        Checks whether or not flipping the pieces in a certain direction is valid
        :param row: int representing the row of the piece being placed
        :param col: int representing the column of the piece being placed
        :param color: 1 or -1 representing whether the piece being placed is white or black, respectively
        :param horizontal: 1, 0 or -1 representing whether the pieces should be flipped moving right, vertically or left, respectively
        :param vertical: 1, 0 or -1 representing whether the pieces should be flipped moving down, horizontally or up, respectively
        :return: bool representing whether or not it is a valid flip
        """

        if (self.board[row][col] != 0):
            return False;

        firstTile = (self.isValidPosition(row + vertical, col + horizontal) and self.board[row + vertical][
            col + horizontal] == -1 * color)

        if (not firstTile):
            return False

        r = row + vertical
        c = col + horizontal

        while (r >= 0 and r < 8 and c >= 0 and c < 8):

            if (self.board[r][c] == 0):
                return False;
            elif (self.board[r][c] == color):
                return True;
            else:
                r += vertical
                c += horizontal

        return False;


    def isValidPosition(self, row, col):
        """
        Checks whether or not a certain row/column pair is on the board
        :param row: int representing the row
        :param col: int representing the column
        :return: bool representing whether or not the position is valid
        """
        return not (row < 0 or col < 0 or row > 7 or col > 7)

    def getValidMoves(self, color):
        """
        Gets a list of all of the valid moves for the given color on the board
        :param color: 1 or -1 representing the color to get the valid move for, respectively
        :return: list containing all of the valid positions to place a piece of the provided color at
        """
        moves = []

        for r in range(0, 8):
            for c in range(0, 8):
                if (self.checkSpot(r, c, color)):
                    moves.append([r, c])

        return moves

    def checkSpot(self, r, c, color):
        """
        Checks whether or not the provided location is a valid spot to place the piece
        :param r: int representing the row where the piece is to be placed
        :param c: int representing the column where the piece is to be placed
        :param color: 1 ir -1 representing the color of the piece to be placed, respectively
        :return: bool representing whether or not the spot is valid for the given color
        """

        if (self.board[r][c] != 0):
            return False;

        for h in range(-1, 2):
            for v in range(-1, 2):
                if (self.isValidFlip(r, c, color, h, v)):
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
