#!/usr/bin/python3

"""
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing locked boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
"""
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the locked boxes.
            Each box is numbered sequentially from 0 to n - 1, where n is the total number of boxes.
            Each inner list contains the keys present in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Get the total number of boxes
    n = len(boxes)

    # Create a list to track the unlocked state of each box
    unlocked = [False] * n

    # Mark the first box as unlocked
    unlocked[0] = True

    # Iterate through each box
    for box in range(n):
        # Check if the current box is unlocked
        if unlocked[box]:
            # Iterate through the keys in the current box
            for key in boxes[box]:
                # Check if the key corresponds to a valid box and if the box is currently locked
                if key < n and not unlocked[key]:
                    # Set the corresponding box as unlocked
                    unlocked[key] = True

    # Check if all boxes are unlocked
    return all(unlocked)

