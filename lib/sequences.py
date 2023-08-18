#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        return []
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while len(sequence) < length:
        next = sequence[-1] + sequence[-2] 
        sequence.append(next)
    else:
        return(print_fibonacci(length - 1) + print_fibonacci(length - 2))

print(print_fibonacci(9))

