#!/usr/bin/python3
"""Calculate the perimeter of an island - ALX Interview"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by a grid.

    Args:
        grid (list[list[int]]): A 2D grid representing the island.

    Returns:
        int: The total perimeter of the island.
    """
    perimeter = 0
    row, col = len(grid), len(grid[0])

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter

