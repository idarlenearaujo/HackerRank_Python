import numpy

# função
def arrays(arr):
    return (numpy.array(arr, float))[::-1]

# entrada
arr = input().strip().split()
result = arrays(arr)
print(result)
