from copy import deepcopy
from game import game
from game import model


def minimax(depth, max_player, game, move):
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

    if (max_player):
        moves = game.getValidMoves()
        bestMove = [-1, -1]
        bestScore = -9999
        for m in moves:
            ga = deepcopy(game)
            ga.doTurn(m[0], m[1])
            score = minimax(depth - 1, not max_player, ga, move)
            if score > bestScore:
                bestMove[0] = m[0]
                bestMove[1] = m[1]
                bestScore = score

        move[0] = bestMove[0]
        move[1] = bestMove[1]

        return bestScore

    else:
        moves = game.getValidMoves()
        bestMove = [-1, -1]
        bestScore = 9999
        for m in moves:
            ga = deepcopy(game)
            ga.doTurn(m[0], m[1])
            score = minimax(depth - 1, not max_player, ga, move)
            if score < bestScore:
                bestMove[0] = m[0]
                bestMove[1] = m[1]
                bestScore = score

        move[0] = bestMove[0]
        move[1] = bestMove[1]

        return bestScore


def minimaxabp(depth, max_player, game, move, alpha, beta):
    if depth == 0 or game.gameOver:
        return game.calcScore()

    if (max_player):
        moves = game.getValidMoves()
        bestMove = [-1, -1]
        bestScore = -9999

        for m in moves:
            ga = deepcopy(game)
            ga.doTurn(m[0], m[1])
            score = minimaxabp(depth - 1, not max_player, ga, move, alpha, beta)
            if score > bestScore:
                bestMove[0] = m[0]
                bestMove[1] = m[1]
                bestScore = score

            alpha = max(alpha, bestScore)

            if beta <= alpha:
                break

        move[0] = bestMove[0]
        move[1] = bestMove[1]

        return bestScore

    else:
        moves = game.getValidMoves()
        bestMove = [-1, -1]
        bestScore = 9999

        for m in moves:
            ga = deepcopy(game)
            ga.doTurn(m[0], m[1])
            score = minimaxabp(depth - 1, not max_player, ga, move, alpha, beta)
            if score < bestScore:
                bestMove[0] = m[0]
                bestMove[1] = m[1]
                bestScore = score

            beta = min(beta, bestScore)

            if beta <= alpha:
                break

        move[0] = bestMove[0]
        move[1] = bestMove[1]

        return bestScore
