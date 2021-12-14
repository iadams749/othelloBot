from copy import deepcopy
from game import game
from game import model

def minimax(depth, max_player,game,move):

    if depth == 0 or game.gameOver:
        return game.calcScore()
        # score = game.calcScore()

        # if(game.gameOver):
        #     print(move)
        #     if score > 0:
        #         return 9999999
        #     elif score < 0:
        #         return -9999999
        # return score


    if(max_player):
        moves = game.getValidMoves()
        outcomes = []
        for m in moves:
            ga = deepcopy(game)
            ga.doTurn(m[0],m[1])
            outcomes.append([m,minimax(depth-1,not max_player,ga,move)])

        bestMove = None
        bestScore = -9999
        for o in outcomes:
            if o[1] > bestScore:
                bestMove = o[0]
                bestScore = o[1]

        move[0] = bestMove[0]
        move[1] = bestMove[1]

        return bestScore

    else:
        moves = game.getValidMoves()
        outcomes = []
        for m in moves:
            ga = deepcopy(game)
            ga.doTurn(m[0], m[1])
            outcomes.append([m, minimax(depth - 1, not max_player, ga, move)])

        bestMove = None
        bestScore = 9999
        for o in outcomes:
            if o[1] < bestScore:
                bestMove = o[0]
                bestScore = o[1]

        move[0] = bestMove[0]
        move[1] = bestMove[1]

        return bestScore








