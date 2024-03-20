#!/usr/bin/python3
# Using nested loops to iterate through all possible combinations of two digits
for i in range(10):
    for j in range(i + 1, 10):  # Start from i+1 to avoid duplicates and combinations with the same digits
        # Print the combination with two digits
        print("{:02d}, ".format(i * 10 + j), end='')
