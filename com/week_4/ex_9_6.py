import numpy as np
nx, ny = 3, 2
X = np.linspace(0, 10, nx)
X
Y = np.linspace(0, 10, ny)
Y
x, y = np.meshgrid(X, Y)
x
y

z = np.sqrt(x**2 + y**2)
z

x1, y1 = np.meshgrid(X, Y, sparse=True)
x1
y1
z1 = np.sqrt(x1**2 + y1**2)
z1
