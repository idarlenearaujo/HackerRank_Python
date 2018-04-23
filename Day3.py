#!/bin/python3

import sys

# entrada
N = int(input().strip())

# se impar
if N % 2 != 0:
    print('Weird')
# se par e entre 2 - 5
elif (N % 2 == 0) and (2 <= N <= 5):
    print('Not Weird')
# se par e entre 6 - 20
elif (N % 2 == 0) and (6 <= N <= 20):
    print('Weird')
# se par e > 20
elif (N % 2 == 0) and (N > 20):
    print('Not Weird')
