import numpy as np
A = np.arange(12).reshape((4, 3))
A
A[A <= 5] = -1
rowsum = A.sum(-1)
rowsum
rows = A.sum(-1) > 0
rows
columns = [0, 2]
columns
A[np. ix_(rows, columns)]

A = np.array([[0, 3, 5], [3, 5, 5], [3, 3, 3]])
mask = np.array([False, False, False, True, False, False])
A1 = mask[A]
A1
