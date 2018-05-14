import numpy as np

N, M, P = map(int, input().split())
# array A / B
arrayA = np.array([list(map(int, input().split())) for i in range(N)])
arrayB = np.array([list(map(int, input().split())) for i in range(M)])
# concatenação
print(np.concatenate([arrayA, arrayB]))
