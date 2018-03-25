import numpy as np
np.add(1.0, 2.0)
x1 = np.arange(9.0).reshape((3, 3))
x1
np.add(x1, 10)
np.add(x1, x1)
np.add(x1, x1, x1)
x1
x2 = np.arange(3.0)
x2
np.add(x1, x2)
b = broadcast(x1, x2)
b.shape