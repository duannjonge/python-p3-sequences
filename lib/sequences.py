#!/usr/bin/env python3

def print_fibonacci(length):
    nums = []  # Initialize an empty list to store the Fibonacci sequence
    a, b = 0, 1  # Initialize the first two Fibonacci numbers

    for _ in range(length):
        nums.append(a)  # Add the current Fibonacci number to the list
        a, b = b, a + b  # Calculate the next Fibonacci number

    print(nums)

print_fibonacci(9)
