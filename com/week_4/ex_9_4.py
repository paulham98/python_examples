import numpy as np
#identity(n, dtype=None)
D = np.identity(3)
D
#eye(N, M=None, k=0, dtype=<class 'float'>)
E1 = np.eye(3, dtype=int)
E1

E2 = np.eye(3, k=1, dtype=int)
E2

E3 = np.eye(3, k=-1, dtype=int)
E3
