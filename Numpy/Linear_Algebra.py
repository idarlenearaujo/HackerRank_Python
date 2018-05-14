import numpy as np

# linhas
N = int(input())
# array A
arrayA = np.array([list(map(float, input().split())) for i in range(N)])
# calcular determinante
print(round(np.linalg.det(arrayA), 2))