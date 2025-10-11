"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    
    count_X, count_O = 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if X == board[i][j]:
                count_X += 1
            elif O == board[i][j]:
                    count_O += 1
    if count_X == count_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action.")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[0][1] == board[0][2] == X) or (board[1][0] == board[1][1] == board[1][2] == X) or (board[2][0] == board[2][1] == board[2][2] == X):
        return X
    elif (board[0][0] == board[1][0] == board[2][0] == X) or (board[0][1] == board[1][1] == board[2][1] == X) or (board[0][2] == board[1][2] == board[2][2] == X):
        return X
    elif (board[0][0] == board[1][1] == board[2][2] == X) or (board[0][2] == board[1][1] == board[2][0] == X):
        return X
    elif (board[0][0] == board[0][1] == board[0][2] == O) or (board[1][0] == board[1][1] == board[1][2] == O) or (board[2][0] == board[2][1] == board[2][2] == O):
        return O
    elif (board[0][0] == board[1][0] == board[2][0] == O) or (board[0][1] == board[1][1] == board[2][1] == O) or (board[0][2] == board[1][2] == board[2][2] == O):
        return O
    elif (board[0][0] == board[1][1] == board[2][2] == O) or (board[0][2] == board[1][1] == board[2][0] == O):
        return O
    else:
        return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win is not None:
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win is None:
        return 0
    return 1 if win == X else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    player = player(board)

    if player == X:
        best_score = float("-inf")
        alpha = float("-inf")
        beta = float("inf")
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action), alpha, beta)
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else:
        best_score = float("inf")
        alpha = float("-inf")
        beta = float("inf")
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action), alpha, beta)
            if score < best_score:
                best_score = score
                best_action = action
        return best_action


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v