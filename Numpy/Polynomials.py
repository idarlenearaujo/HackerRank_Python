import numpy as np

# array A
arrayA = np.array([float(i) for i in input().split()])
# Ponto p
pont = int(input())
# result
print(np.polyval(arrayA, pont))