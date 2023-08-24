#!/usr/bin/python3
"""
Interview Question: Fewest Number of Coins Needed
to Meet a Given Amount Total
"""

def makeChange(coins, total):
    """
    Return the fewest number of coins needed to meet the given total amount.
    
    Args:
        coins (list): List of coin denominations available.
        total (int): The total amount to be achieved using coins.
    
    Returns:
        int: The minimum number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0
    
    # Sort the coin denominations in descending order for efficient use
    coins.sort(reverse=True)
    
    change = 0  # Initialize the count of coins used for change
    
    # Iterate through coin denominations to find the minimum coins needed
    for coin in coins:
        if total <= 0:
            break
        
        # Calculate the maximum number of current coin denomination that fits
        temp = total // coin
        
        # Add the count of current coin denomination to the total change count
        change += temp
        
        # Update the remaining total amount after using the current coin denomination
        total -= (temp * coin)
    
    # If the total amount couldn't be achieved using available coins
    if total != 0:
        return -1
    
    return change

