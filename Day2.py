#!/bin/python3

import sys

# funcao para calcular total
def calculo(arg1, arg2, arg3):
    tip = arg1 * (arg2 / 100)
    tax = arg1 * (arg3 / 100)

    totalCost = arg1 + tip + tax
    totalCost = round(totalCost)

    return totalCost


if __name__ == "__main__":
    # entrada
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    # resultado da funcao
    result = calculo(meal_cost, tip_percent, tax_percent)

    # mostra na tela a resposta
    print('The total meal cost is {} dollars.'.format(result))