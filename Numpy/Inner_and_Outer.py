import numpy as np

# array A / B
arrayA, arrayB = (np.array([int(i) for i in input().split()]) for _ in range(2))
# produ interno
# produ externo
print('{}\n{}'.format(np.inner(arrayA, arrayB), np.outer(arrayA, arrayB)))
