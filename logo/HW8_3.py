import numpy as np
z = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 3, 5, 4])
x = np.setdiff1d(z, y)
print(x)
