import numpy as np
A = np.arange(10)
np.random.shuffle(A)
A

np.sort(A)

A

A.sort()
A
np.random.shuffle(A)
A
A[::-1].sort()
A

np.searchsorted([1, 3, 5], 3)
np.searchsorted([1, 3, 5], 3, side = 'right')
A = np.array([[0, 3, 5], [3, 5, 5], [3, 3, 3]])
label = [0, 3, 5]
np.searchsorted(label, A)
