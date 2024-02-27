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
    if [item for row in board for item in row].count(EMPTY) % 2 == 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                actions_set.add((x,y))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x, y) = action
    if board[x][y] != EMPTY:
        raise Exception('Action forbidden - that cell is not empty!')
    
    board_copy = copy.deepcopy(board)
    board_copy[x][y] = player(board_copy)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for state in WINNING_STATES:
        values = []
        for position in state:
            (x,y) = position
            values.append(board[x][y])
        if values.count(values[0]) == len(values) and values[0] != EMPTY:
            return values[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_fields = [item for row in board for item in row].count(EMPTY)
    if empty_fields > 4:
        return False
    
    if winner(board) != None or empty_fields == 0:
        return True
    else:
        return False


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
    raise NotImplementedError
