#!/usr/bin/python3

def minOperations(n: int) -> int:
    """Return the minimal number of operations to reach n H's.

    Rules:
    - If n < 2, it's impossible, so return 0.
    - For n >= 2, sum of prime factors of n.
    """
    if n < 2:
        return 0

    operations = 0
    current_number = 2
    while n > 1:
        while n % current_number == 0:
            operations += current_number
            n //= current_number
        current_number += 1
    return operations


if __name__ == "__main__":
    print(minOperations(12))
