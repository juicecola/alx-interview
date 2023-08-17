#!/usr/bin/python3
"""
This script defines functions to rotate a 2D matrix 90 degrees clockwise.
"""

def transpose_matrix(matrix, n):
    """
    Transpose the given matrix in-place.

    Args:
        matrix (list[list]): The 2D matrix to be transposed.
        n (int): The size of the matrix (number of rows/columns).
    """
    for i in range(n):
        for j in range(i, n):
            # Swap elements across the main diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_matrix(matrix):
    """
    Reverse the order of elements in each row of the matrix.

    Args:
        matrix (list[list]): The 2D matrix to be reversed row-wise.
    """
    for row in matrix:
        row.reverse()

def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The 2D matrix to be rotated.
    
    Returns:
        list[list]: The rotated matrix.
    """
    n = len(matrix)
    
    # Transpose the matrix (turn rows into columns)
    transpose_matrix(matrix, n)
    
    # Reverse each row to complete the rotation
    reverse_matrix(matrix)
    
    return matrix

