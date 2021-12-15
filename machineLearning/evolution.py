from minimax.algorithm import *
import random


def tune(values):

    bestValues = []

    for x in range(0,6):
        bestValues.append(values[x])

    print(f"Starting Values: {bestValues}")

    for gen in range(1,101):
        newValues = []
        for x in range(0, 6):
            positive = bool(random.getrandbits(1))
            if positive:
                newValues.append(random.uniform(0, 1))
            else:
                newValues.append(-1*random.uniform(0,1))

            newValues[x] += bestValues[x]
            if newValues[x] > 15:
                newValues[x] = 15
            if newValues[x] < -15:
                newValues[x] = -15

        g = game.Game()

        bestBlack = bool(random.getrandbits(1))

        if bestBlack:
            while not g.gameOver:
                if g.turn == -1:
                    move = [-1,-1]
                    minimaxabpweighted(4,False,g,move,-9999,9999,bestValues)
                    g.doTurn(move[0],move[1])
                else:
                    move = [-1, -1]
                    minimaxabpweighted(4, True, g, move, -9999, 9999, newValues)
                    g.doTurn(move[0], move[1])

        else:
            while not g.gameOver:
                if g.turn == -1:
                    move = [-1,-1]
                    minimaxabpweighted(4,False,g,move,-9999,9999,newValues)
                    g.doTurn(move[0],move[1])
                else:
                    move = [-1, -1]
                    minimaxabpweighted(4, True, g, move, -9999, 9999, bestValues)
                    g.doTurn(move[0], move[1])

        if bestBlack:
            score = g.calcScore()
            if score < 0:
                print(f"Best values won! Values stay at {bestValues}")
            elif score > 0:
                for x in range(0,6):
                    bestValues[x] = (bestValues[x] + newValues[x]) / 2
                print(f"New values won! Values change to {bestValues}")


        else:
            score = g.calcScore()
            if score > 0:
                print(f"Best values won! Values stay at {bestValues}")
            elif score < 0:
                for x in range(0, 6):
                    bestValues[x] = (bestValues[x] + newValues[x]) / 2
                print(f"New values won! Values change to {bestValues}")



