#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys


def is_safe(board, row, col):
    """
    Check if placing a Queen at the given position (row, col) is safe.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row of the new Queen being placed.
        col (int): The column of the new Queen being placed.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    # Check for Queen in the same row
    if 1 in board[row]:
        return False

    # Check for Queen in the same column
    if 1 in [board[i][col] for i in range(len(board))]:
        return False

    # Check for Queen in the diagonals
    for i in range(len(board)):
        if row + col - i < len(board) and row + col - i >= 0 and board[i][row + col - i] == 1:
            return False
        if row - col + i < len(board) and row - col + i >= 0 and board[i][row - col + i] == 1:
            return False

    return True


def n_queens_helper(board, col, solutions):
    """
    Helper function to find all valid solutions for placing N Queens.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column being considered.
        solutions (list): List to store the valid solutions.

    Returns:
        None
    """
    # Base case: All columns have been processed (reached the end)
    if col == len(board):
        # Append the current valid solution to the list of solutions
        solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
        return

    # Try placing the Queen in each row of the current column
    for row in range(len(board)):
        if is_safe(board, row, col):
            # Place the Queen in the board
            board[row][col] = 1
            # Recursively explore the next column
            n_queens_helper(board, col + 1, solutions)
            # Backtrack by removing the Queen from the board to explore other possibilities
            board[row][col] = 0


def n_queens(n):
    """
    Find and print all valid solutions for placing N Queens on the chessboard.

    Args:
        n (int): The size of the chessboard (N).

    Returns:
        None
    """
    # Validate the input value of N
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty NxN chessboard filled with zeros
    board = [[0 for _ in range(n)] for _ in range(n)]
    # List to store all valid solutions
    solutions = []

    # Start the backtracking process to find all solutions
    n_queens_helper(board, 0, solutions)

    # Print each valid solution
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    # Validate the command-line argument and get the size of the chessboard (N)
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: nqueens N")
        sys.exit(1)
    n = int(sys.argv[1])
    # Call the main function to find and print all valid solutions
    n_queens(n)

