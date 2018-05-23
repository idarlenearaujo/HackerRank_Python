#!/bin/python3
import sys

def factorial(n):
    # se n = 0
    if n == 0:
        return 0
    # se n = 1
    if n == 1:
        return 1
    # se n > 1 recursivo
    if n > 1:
        return factorial(n - 1) * n

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)