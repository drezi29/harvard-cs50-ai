"""
Tic Tac Toe Player
"""

import copy, math

X = "X"
O = "O"
EMPTY = None

WINNING_STATES = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

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
    if count_empty_cells(board) % 2 == 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Action is not valid")
    
    i, j = action
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board_copy)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for state in WINNING_STATES:
        values = []
        for position in state:
            x, y = position
            values.append(board[x][y])
        if values.count(values[0]) == len(values) and values[0] != EMPTY:
            return values[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif count_empty_cells(board) > 0:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    alpha = -math.inf
    beta = math.inf
    moves = []

    if player(board) == X:
        for action in actions(board):
            moves.append((min_value(result(board, action), alpha, beta), action))
        return sorted(moves, key= lambda x: x[0], reverse=True)[0][1]
    else:
        for action in actions(board):
            moves.append((max_value(result(board, action), alpha, beta), action))
        return sorted(moves, key= lambda x: x[0])[0][1]


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        action_value = min_value(result(board, action), alpha, beta)
        v = max(v, action_value)
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        action_value = max_value(result(board, action), alpha, beta)
        v = min(v, action_value)
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v


def count_empty_cells(board):
    return [item for row in board for item in row].count(EMPTY)