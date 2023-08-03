#!/usr/bin/python3
"""
N Queens Puzzle Solver

This program solves the N Queens problem, which involves placing N non-attacking
queens on an N×N chessboard.

Usage: nqueens N

Arguments:
    N (int): The size of the chessboard and the number of queens.

The program prints every possible solution to the N Queens problem, one solution per line.

Example:
    $ ./nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
"""

import sys

def generate_solutions(row, column):
    """
    Generate all solutions for the N Queens problem using backtracking.

    Args:
        row (int): The current row position of the queen to be placed.
        column (int): The size of the chessboard and the number of queens.

    Returns:
        List[List[int]]: A list of all possible solutions for the N Queens problem.
    """
    if row == column:
        return [[]]  # Base case, return an empty board with no queens placed
    prev_solution = generate_solutions(row + 1, column)
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(row, x, array):
                safe_position.append(array + [x])
    return safe_position

def place_queen(queen, column, prev_solution):
    """
    Place a queen at position (queen, column) on the chessboard.

    Args:
        queen (int): The row position of the queen to be placed.
        column (int): The size of the chessboard and the number of queens.
        prev_solution (List[List[int]]): The previously placed queens' positions.

    Returns:
        List[List[int]]: A list of board configurations after placing the queen.
    """
    return [array + [queen] for array in prev_solution]

def is_safe(q, x, array):
    """
    Check if placing a queen at position (q, x) is safe.

    Args:
        q (int): The row position of the queen.
        x (int): The column position of the queen.
        array (List[int]): The current board configuration.

    Returns:
        bool: True if placing the queen at (q, x) is safe, False otherwise.
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))

def init():
    """
    Initialize the N Queens problem with user input.

    Returns:
        int: The size of the chessboard and the number of queens (N).
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def n_queens():
    """
    Solve and print the N Queens problem.
    """
    n = init()
    # Generate all solutions
    solutions = generate_solutions(0, n)
    # Print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)

if __name__ == '__main__':
    n_queens()

