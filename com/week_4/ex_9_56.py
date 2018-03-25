import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10.0, 10.0, num=51)
m, c = 3, -10
y = m*x + c
e = np.random.normal(0, 10.0, x.size)
y1 = y + e
A = np.vstack([x, np.ones(len(x))]).T
p,residuals, r, s = np.linalg.latsq(A, y1)
m1, c1 = p
y2 = m1*x + c1

plt.plot(x, y, "b-", label = "y = 3x - 10")
plt.plot(x, y1, "ko", label = "y1 = 3x - 10 + N(0, 10.0)")
plt.plot(x, y2, "r-", label = "y2 = {:+.2f}x {:+.2f}".format(m1, c1))

plt.title("Least square solution: residuals {:2f}".format(residuals[0]))
plt.legend(loc="best")
plt.savefig("ex0956.png")
plt.show()