import numpy as np
#zeros(shape, dtype=float, order = 'C')
A1 = np.zeros(6)
A1
A2 = np.zeros((2, 3))
A2
A3 = np.zeros((2, 3), dtype=np.int32)
A3
A4 = np.zeros((2, 3), dtype=np.int64, order= 'C')
A4

#ones(shape, dtype=None, order = 'C')
B = np.ones((2, 3))
B

#empty(shape, dtype=None, order = 'C')
C = np.empty((2, 3))
C

#full(shape, fill_value, dtype=None, order='C')
A = np.full((2, 3), 10, dtype = np.int32)