#!/usr/bin/python3

"""
Calculate the fewest operations needed to achieve 'n' 'H' characters
in a text file.
Operations available: 'Copy All' and 'Paste'.
"""

def minOperations(n):
    num_ops = 0  # Total operations
    min_ops = 2  # Minimum divisor

    while n > 1:
        while n % min_ops == 0:
            num_ops += min_ops
            n /= min_ops
        min_ops += 1

    return num_ops  # Total operations required

