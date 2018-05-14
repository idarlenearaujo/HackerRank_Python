import numpy as np

N = int(input())
# array A / B
arrayA, arrayB = (np.array([input().split() for i in range(N)], int) for _ in range(2))
# prod
print(np.dot(arrayA, arrayB))
