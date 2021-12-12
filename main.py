from game import model, game
from random import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g = game.Game()
    sum = 0
    for y in range(0,10):
        sum = 0
        for x in range(0,1000):
            g = game.Game()
            g.playGameAuto()
            if(g.calcScore() > 0):
                sum += 1
            elif(g.calcScore() < 0):
                sum -= 1
        print(sum)

    # turn = 1

    # Having the computer play a random game
    # for x in range(0,58):
    #     moves = m.getValidMoves(turn)
    #     position = moves[randint(0, len(moves)-1)]
    #     m.setPiece(position[0],position[1],turn)
    #     turn = -1*turn
    #
    # print(m.board)


