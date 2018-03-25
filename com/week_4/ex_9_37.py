import numpy as np
L = np.array([[1, 0, 0], [1, 1, 0], [2, -4.5, 1]])
b = [7, 13, 5]
y = np.linalg.solve(L, b)
y

U = np.array([[1, 0, 0], [0, 2, -2], [0, 0, -9]])
x = np.linalg.solve(U, y)
x

A = np.dot(L, U)
A
x2 = np.linalg.solve(A, b)
x2

