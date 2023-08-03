#!/usr/bin/env python3
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

    $ ./nqueens.py 6
    [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""

import sys
import argparse

def is_safe(queen, x, array):
    """
    Check if placing a queen at position (queen, x) is safe.

    Args:
        queen (int): The row position of the queen.
        x (int): The column position of the queen.
        array (List[List[int]]): The current board configuration.

    Returns:
        bool: True if placing the queen at (queen, x) is safe, False otherwise.
    """
    return all(abs(array[column] - x) != queen - column for column in range(queen))

def generate_solutions(row, column, prev_solution):
    """
    Generate all solutions for the N Queens problem using backtracking.

    Args:
        row (int): The row position of the current queen to be placed.
        column (int): The size of the chessboard and the number of queens.
        prev_solution (List[List[int]]): The previously placed queens' positions.

    Returns:
        List[List[int]]: A list of all possible solutions for the N Queens problem.
    """
    if row == column:
        return prev_solution
    solution = []
    for queen in range(column):
        if all(is_safe(row, queen, array) for array in prev_solution):
            solution.extend(place_queen(queen, column, prev_solution))
    return generate_solutions(row + 1, column, solution)

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

def main():
    """
    Main function to solve the N Queens problem and print the solutions.
    """
    parser = argparse.ArgumentParser(description="Solves the N Queens problem.")
    parser.add_argument("N", type=int, help="The size of the chessboard and the number of queens.")
    args = parser.parse_args()

    if args.N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = generate_solutions(0, args.N, [[]])
    for array in solutions:
        print(array)

if __name__ == "__main__":
    main()

