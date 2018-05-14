#!/bin/python3
import sys

# number
n = int(input().strip())

# loop com produtos
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, (n * i)))
