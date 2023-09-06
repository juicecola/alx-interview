#!/usr/bin/python3
""" Module for solving the prime game question """

def isWinner(x, nums):
    """
    Determine the winner of a prime game.

    Args:
    - x (int): The number of rounds to play.
    - nums (list): List of integers as 'n' for each round.

    Returns:
    - str or None: Name of the winner (Maria or Ben), or None if undecided.

    Algorithm:
    - Precompute prime numbers up to the max 'n' in 'nums'.
    - Calculate total primes for each 'n'.
    - Determine round winners based on prime parity.
    - Compare Maria and Ben's wins for the overall winner.

    """

    # Check for edge cases
    if not nums or x < 1:
        return None

    # Find the maximum 'n' in the list 'nums'
    max_num = max(nums)

    # Create a sieve of Eratosthenes to filter prime numbers
    my_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False
    my_filter[0] = my_filter[1] = False

    # Count cumulative prime numbers
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y

    # Initialize player1's wins count
    player1 = 0

    # Calculate wins for player1 (Maria)
    for x in nums:
        player1 += my_filter[x] % 2 == 1

    # Determine the overall winner
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"

