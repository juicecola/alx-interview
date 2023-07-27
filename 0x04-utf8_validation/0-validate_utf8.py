#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

"""


def validUTF8(data):
    """
    Check if the given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing individual bytes.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    # Initialize the number of expected continuation bytes for the current character
    expected_continuation_bytes = 0

    # Define bit patterns for UTF-8 encoding
    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    # Loop over each byte in the input data
    for byte in data:
        # Initialize a mask to check for leading 1's in the current byte
        leading_one_mask = 1 << 7

        # If we are not currently expecting any continuation bytes
        if expected_continuation_bytes == 0:
            # Count the number of leading 1's in the current byte to determine
            # the number of continuation bytes for the current character
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1

            # If the byte is not a multi-byte sequence, move to the next byte
            if expected_continuation_bytes == 0:
                continue

            # If the number of continuation bytes is not between 2 and 4,
            # the sequence is invalid
            if expected_continuation_bytes < 2 or expected_continuation_bytes > 4:
                return False

        # If we are expecting continuation bytes
        else:
            # Check that the byte starts with a "10" prefix and not a "11" prefix
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        # Decrement the expected number of continuation bytes for the current character
        expected_continuation_bytes -= 1

    # If we have processed all bytes and are not expecting any more continuation bytes,
    # the sequence is valid
    return expected_continuation_bytes == 0
