import numpy as np
np.dot(2, 5)
np.dot([1, 2], [3, 4])

A=np.array([[1, 2],[3, 4]])
B=np.array([[5, 6], [7, 8]])
np.vdot(A, B)
np.dot(A, B)
np.matmul(A, B)
np.inner(A, B)
np.outer([1, 2], [3, 4])

print(np.outer(A,B))
