import numpy as np

np.set_printoptions(legacy='1.13')

# dimensão ( N, M e k )
# matrix identidade
print(np.eye(*map(int, input().split())))
