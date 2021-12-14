import datetime
from minimax.algorithm import *

if __name__ == '__main__':
    g = game.Game()

    move = [-1,-1]
    alpha = -99999
    beta = 99999

    for x in range(0,1):
        beginTime = datetime.datetime.now()
        g = game.Game()

        while(not g.gameOver):
            alpha = -99999
            beta = 99999
            move[0] = -1
            move[1] = -1

            if(g.turn == -1):
                minimaxabp(6,False,g,move,alpha,beta)
                g.doTurn(move[0], move[1])
                print(g.model.board)
                print(f"Current Score: {g.calcScore()}")
            else:
                g.playRandomMove()

        print(f"Final Score: {g.calcScore()}")
        print(f"Completion Time: {datetime.datetime.now()-beginTime}")


