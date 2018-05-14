import numpy as np

# entrada N, M
N, M = map(int, input().split())
# lista
array = np.reshape(np.array([[int(i) for i in input().split()] for _ in range(N)]), (N, M))
# transposta
print(array.transpose())
# inteira
print(array.flatten())
