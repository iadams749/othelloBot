from copy import deepcopy


def minimax(depth, max_player, game, move):
    """Recursively calls a simple minimax algorithm on the provided game with all pieces weighted equally

    :param depth: int representing the current depth of the call
    :param max_player: bool representing whether or not the call aims to maximize the score
    :param game: Game that represents the current came for the algorithm to be called on
    :param move: int[] that is a placeholder which will hold the best move to be made when the top level call return
    :return: int representing the maximum or minimum score for the game, depending on whether or not it is black or white to move
    """

    if depth == 0 or game.gameOver:
        return game.calcScore()

    if (max_player):
        moves = game.getValidMoves()
        bestMove = [-1, -1]
        bestScore = -9999
        for m in moves:
            ga = deepcopy(game)
            ga.doTurn(m[0], m[1])
            if ga.turn == -1:
                score = minimax(depth - 1, False, ga, move)
            else:
                score = minimax(depth - 1, True, ga, move)
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
            if (ga.turn == -1):
                score = minimax(depth - 1, False, ga, move)
            else:
                score = minimax(depth - 1, True, ga, move)
            if score < bestScore:
                bestMove[0] = m[0]
                bestMove[1] = m[1]
                bestScore = score

        move[0] = bestMove[0]
        move[1] = bestMove[1]

        return bestScore


def minimaxabp(depth, max_player, game, move, alpha, beta):
    """Recursively calls a minimax algorithm that has alpha-beta pruning implemented in order to increase efficiency, uses a weighted value of one for all pieces

    :param depth: int representing the current depth of the call
    :param max_player: bool representing whether or not the call aims to maximize the score
    :param game: Game that represents the current came for the algorithm to be called on
    :param move: int[] that is a placeholder which will hold the best move to be made when the top level call return
    :param alpha: int representing the alpha value to be used in alpha-beta pruning
    :param beta: int representing the beta value to be used in the alpha-beta pruning
    :return: int representing the maximum or minimum score for the game, depending on whether or not it is black or white to move
    """
    return minimaxabpweighted(depth, max_player, game, move, alpha, beta, [1, 1, 1, 1, 1, 1])


def minimaxabpweighted(depth, max_player, game, move, alpha, beta, values):
    """Recursively calls a minimax algorithm that has alpha-beta pruning implemented in order to increase efficiency, calculates weighted score based off of provided weights

    :param depth: int representing the current depth of the call
    :param max_player: bool representing whether or not the call aims to maximize the score
    :param game: Game that represents the current came for the algorithm to be called on
    :param move: int[] that is a placeholder which will hold the best move to be made when the top level call return
    :param alpha: int representing the alpha value to be used in alpha-beta pruning
    :param beta: int representing the beta value to be used in the alpha-beta pruning
    :param values: double[] representing the weights for each position
    :return: int representing the maximum or minimum score for the game, depending on whether or not it is black or white to move
    """
    if depth == 0 or game.gameOver:
        return game.calcWeightedScore(values)

    if (max_player):
        moves = game.getValidMoves()
        bestMove = [-1, -1]
        bestScore = -9999

        for m in moves:
            ga = deepcopy(game)
            ga.doTurn(m[0], m[1])
            if (ga.turn == -1):
                score = minimaxabpweighted(depth - 1, False, ga, move, alpha, beta, values)
            else:
                score = minimaxabpweighted(depth - 1, True, ga, move, alpha, beta, values)
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
            if (ga.turn == -1):
                score = minimaxabpweighted(depth - 1, False, ga, move, alpha, beta, values)
            else:
                score = minimaxabpweighted(depth - 1, True, ga, move, alpha, beta, values)

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
