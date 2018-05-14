import numpy as np

N, M = map(int, input().split())
# array A / B
arrayA = np.array([list(map(int, input().split())) for i in range(N)])
# media aritmetica sob eixo 1
# variance sob eixo 0
# desvio padrão sob eixo None
print(np.mean(arrayA, axis=1))
print(np.var(arrayA, axis=0))
print(np.std(arrayA, axis=None))
