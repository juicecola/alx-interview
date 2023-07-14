#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters in the file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The fewest number of operations required to reach n 'H' characters. Returns 0 if not possible.
    """

    if n <= 1:
        # If n is less than or equal to 1, it's not possible to reach the desired number of characters.
        return 0

    operations = 0  # Initialize the number of operations to 0.
    characters = 1  # Initialize the number of characters to 1.

    while characters < n:
        # Repeat until the number of characters is less than n.

        if n % characters == 0:
            # If n is divisible by the current number of characters, perform the Copy All operation.
            # Set characters to its current value.
            characters = characters * 2

        operations += 1
        # Increment the number of operations by 1.

    if characters == n:
        # If the number of characters is equal to n, return the number of operations.
        return operations
    else:
        # If it's not possible to reach n characters, return 0.
        return 0

