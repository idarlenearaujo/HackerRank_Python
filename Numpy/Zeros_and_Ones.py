import numpy as np

# dimensão
tupla = tuple(map(int, input().split()))
# arrays
# print
print(np.zeros(tupla, dtype=np.int), np.ones(tupla, dtype=np.int), sep='\n')
