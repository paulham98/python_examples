import numpy as np
#histogram(a, bins=10, range=None,nirmed=False, weights=None, density=None)
A = np.random.random_integers(1, 6, size=20)
A
np.histogram(A, bins=[0, 1, 3, 6])

hist, bin_edges = np.histogram(A, bins=[0, 1, 3, 6], density=True)
hist
bin_edges
hist.sum()
np.diff(bin_edges)
np.sum(hist*np.diff(bin_edges))
