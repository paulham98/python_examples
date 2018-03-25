import numpy as np
#arange([start,] stop[, step,], dtype=None)
np.arange(3)
np.arange(3.0)
np.arange(3, 10)
np.arange(3, 10, 2)

A = np.arange(3)
A
A.dtype
B = A.dtype
B = A.astype(np.float64)
B
B.dtype

