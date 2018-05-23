#!/bin/python3
import sys

# entrada e transformacao do int em boolean
n = int(input().strip())
n = list(bin(n)[2:])

# variaveis
p, soma = 0, 1

# percorrer o binario
for i in n:

    if p == 0:
        p = 1

    else:
        if first == i:
            soma += int(i)
        else:
            p = 0

    first = i

print(soma)