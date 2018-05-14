import numpy as np

N, M = map(int, input().split())
# array A
arrayA = np.array([list(map(int, input().split())) for i in range(N)])
# sum sob eixo 0
# prod
print(np.prod(np.sum(arrayA, axis=0)))
