"""
Tic Tac Toe Player
"""

import math

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
    playerX = X
    playerO = O
    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == playerX:
                countX += 1
            elif board[i][j] == playerO:
                countO += 1
    if countX > countO:
        return playerO
    else:
        return playerX


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row[:] for row in board]  # Create a deep copy of the board
    i, j = action
    if i < 0 or i >= 3 or j < 0 or j >= 3:
        raise Exception("Invalid action: Out of bounds")
    if new_board[i][j] is not None:
        raise Exception("Invalid action: Cell already occupied")
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or all(cell is not None for row in board for cell in row):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check if X has won the game
    if winner(board) == X:
        return 1
    # Check if O has won the game
    elif winner(board) == O:
        return -1
    # If the game has ended in a tie
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, action = max_value(board)
        return action
    else:
        value, action = min_value(board)
        return action


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    best_action = None

    for action in actions(board):
        min_val = min_value(result(board, action))[0]
        if min_val > v:
            v = min_val
            best_action = action

    return v, best_action


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    best_action = None

    for action in actions(board):
        max_val = max_value(result(board, action))[0]
        if max_val < v:
            v = max_val
            best_action = action

    return v, best_action
