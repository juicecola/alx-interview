#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys


def generate_solutions(row, column):
    """
    Generate all valid solutions for placing N Queens on the NxN chessboard.

    Args:
        row (int): The row of the current Queen being placed.
        column (int): The total number of columns (N).

    Returns:
        list: A list of valid solutions represented as arrays of Queen positions.
    """
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Place a new Queen on the chessboard without attacking the previous ones.

    Args:
        queen (int): The row of the new Queen being placed.
        column (int): The total number of columns (N).
        prev_solution (list): The list of previous solutions.

    Returns:
        list: A list of valid solutions after placing the new Queen.
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    Check if a new Queen can be placed at the given position without attacking other Queens.

    Args:
        q (int): The row of the new Queen being placed.
        x (int): The column of the new Queen being placed.
        array (list): The list of previously placed Queens.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """
    Initialize the program and validate the user input.

    Returns:
        int: The size of the chessboard (N).
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """
    Find and print all valid solutions for placing N Queens on the chessboard.
    """
    n = init()
    # Generate all solutions
    solutions = generate_solutions(n, n)
    # Print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
