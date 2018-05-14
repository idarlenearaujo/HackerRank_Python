import numpy as np

np.set_printoptions(legacy='1.13')
# array A
a = np.array([float(i) for i in input().split()])
# print
# floor -> não arredonda
# ceil -> arredonda todos para mais
# rint -> arredonda apenas acima de .5
print('{}\n{}\n{}'.format(np.floor(a), np.ceil(a), np.rint(a)))
