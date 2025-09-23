#!/usr/bin/python3
"""
Calculate how many square units of water will be retained after it rains.
"""


def rain(walls):
    """
    Calculate the amount of rainwater retained.
    Args:
        walls (list): List of non-negative integers representing wall heights.
    Returns:
        int: Total amount of water retained.
    """
    if not walls or len(walls) < 3:
        return 0  # Need at least 3 walls to trap water

    n = len(walls)
    max_left = [0] * n
    max_right = [0] * n

    # Fill max_left
    max_left[0] = walls[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], walls[i])

    # Fill max_right
    max_right[-1] = walls[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], walls[i])

    # Calculate trapped water
    water = 0
    for i in range(n):
        trapped = min(max_left[i], max_right[i]) - walls[i]
        if trapped > 0:
            water += trapped

    return water
