#!/bin/python3
import sys

# variavel
lista = []

# numero de numeros no array
# array
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# inverter posicoes
arr.reverse()

# mostrar na tela resposta
for i in range(n):
    print(arr[i], end=" ")
