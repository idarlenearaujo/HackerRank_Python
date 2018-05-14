import numpy as np

# dimensão
N, M = map(int, input().split())
# array A / B
a, b = (np.array([input().split() for i in range(N)],int) for _ in range(2))
# print
print('{}\n{}\n{}\n{}\n{}\n{}\n'
      .format(a + b, a - b, a * b, a // b, a % b, a ** b))
