import numpy as np
A = np.array([1, 2, 3, 4, 5, 6, 7, 8])
cond = A%2 == 0
cond

np.extract(cond. A)
A[cond]

#numpy.where(condition[, x, y])
np.where(cond)
np.where(cond, A, 0)
np,where(cond, 0, A)
np.where(cond, 1, -1)

B = A*10
B
np.where(cond,A, B)
