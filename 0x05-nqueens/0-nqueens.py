#!/usr/bin/python3
"""
N queens problem - Solving the N queens puzzle on an NxN chessboard.
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_q < 4:
    print('N must be at least 4')
    exit(1)

def solve_nqueens(n):
    '''Recursively solve the N queens problem.'''
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if is_safe_queen((n, i + 1), solution)]

def is_attack_queen(square, queen):
    '''Check if two queens can attack each other.'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or abs(row1 - row2) == abs(col1 - col2)

def is_safe_queen(sqr, queens):
    '''Check if a queen can be safely placed on a square.'''
    for queen in queens:
        if is_attack_queen(sqr, queen):
            return False
    return True

for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)

