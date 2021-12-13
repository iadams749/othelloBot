import datetime

from game import model, game
from random import *
from minimax.algorithm import minimax

if __name__ == '__main__':
    g = game.Game()

    move = [-1,-1]

    beginTime = datetime.datetime.now()

    while(not g.gameOver):
        if(g.turn == -1):
            move[0] = -1
            move[1] = -1
            minimax(4,False,g,move)
            g.doTurn(move[0], move[1])
            print(g.model.board)
            print(f"Current Score: {g.calcScore()}")
        else:
            # move[0] = -1
            # move[1] = -1
            # minimax(4, True, g, move)
            # g.doTurn(move[0], move[1])
            g.playRandomMove()
            print(g.model.board)
            print(f"Current Score: {g.calcScore()}")

    print(f"Final time: {datetime.datetime.now()-beginTime}")


    # turn = 1

    # Having the computer play a random game
    # for x in range(0,58):
    #     moves = m.getValidMoves(turn)
    #     position = moves[randint(0, len(moves)-1)]
    #     m.setPiece(position[0],position[1],turn)
    #     turn = -1*turn
    #
    # print(m.board)


